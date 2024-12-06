from django.shortcuts import render, redirect
from .models import Product, Income, Cost, User, Staffdailywork
from .forms import ProductForm, CostForm, UserForm, WorkForm
from django.utils.dateparse import parse_date
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.hashers import make_password

@login_required(login_url="login")
def logout_view(request):
    logout(request=request)
    return redirect("login")


# Bosh sahifa ko'rinishi
@login_required(login_url="login")
def home(request):
    dbProduct = Product.objects.all()  # Barcha mahsulotlarni olish
    context = {
        "Products": dbProduct
    }
    try:
        q = request.GET.get("search_q")
        if q != '':
            q_maxsulotlar = Product.objects.filter(name__icontains = q)
            context["Products"] = q_maxsulotlar
    except:
        pass
    return render(request, 'index.html', context)

# Mahsulotni ko'rish va uni sotish
@login_required(login_url="login")
def korish_product(request, pk):
    maxsulot = Product.objects.get(pk=pk)  # Tanlangan mahsulotni olish
    if request.method == "POST":
        soni = request.POST.get("soni")  # Foydalanuvchi kiritgan mahsulot soni
        narxi = request.POST.get("narxi")  # Foydalanuvchi kiritgan mahsulot narxi
        maxsulot.quantity -= int(soni)  # Mahsulot sonini kamaytirish
        maxsulot.save()  # O'zgarishni saqlash
        
        income = Income()
        income.name = maxsulot.name
        income.price = float(narxi)
        income.quantity = int(soni)  # Mahsulot miqdorini butun son shaklida saqlash
        income.save()  # Daromadni saqlash

        if maxsulot.quantity == 0:
            maxsulot.delete()  # Agar mahsulot soni nol bo'lsa, o'chirib tashlash
        return redirect('home')  # Bosh sahifaga qaytish
    context = {
        "Product": maxsulot
    }
    return render(request, 'korish_product.html', context)

# Mahsulot qo'shish ko'rinishi
@login_required(login_url="login")
def qoshish_product(request):
    forms = ProductForm()
    forms = ProductForm(request.POST, request.FILES) # Tasvirlar bilan birga ma'lumotlarni qabul qilish
    if request.method == "POST":  
        if forms.is_valid():
            forms.save()  # Agar forma to'g'ri bo'lsa, mahsulotni saqlash
            return redirect("home")  # Bosh sahifaga qaytish
    return render(request, 'qoshish_product.html', {"forms":forms})

# Foyda hisoblash funksiyasi
def foyda(income, xarajat, xarid):
    ziyon = xarid + xarajat
    foyda = income - ziyon
    qarz = foyda < 0  # Qarzdami yoki yo'qligini aniqlash
    return {"foyda": foyda, "qarz": qarz}

# Daromad va xarajatlarni ko'rish
@login_required(login_url="login")
def income(request):
    income = Income.objects.all()  # Barcha daromadlarni olish
    cost = Cost.objects.all()  # Barcha xarajatlarni olish
    xaridlar = Product.objects.all()  # Barcha mahsulotlar

    xaridsumma = []

    for xarid in xaridlar:
        xaridsumma.append(xarid.price * xarid.quantity)  # Har bir mahsulotning umumiy narxini hisoblash
    jamixarid = sum(xaridsumma)  # Umumiy xarid summasi

    summalar = []
    for summa in income:
        summalar.append(summa.price * summa.quantity)  # Har bir daromadning umumiy narxini hisoblash
    jamisumma = sum(summalar)  # Umumiy daromad summasi

    xarajat = []
    for xarajatsumma in cost:
        xarajat.append(xarajatsumma.price)  # Har bir xarajat summasi
    jamixarajat = sum(xarajat)  # Umumiy xarajat summasi

    # Foyda hisoblash
    foydafunc = foyda(income=jamisumma, xarajat=jamixarajat, xarid=jamixarid)

    context = {
        "income": income,
        "jamisumma": jamisumma,
        "cost": cost,
        "jamixarajat": jamixarajat,
        "jamixarid": jamixarid,
        "foyda": foydafunc["foyda"],
        "qarz": foydafunc["qarz"]
    }
    return render(request, "income.html", context)

# Xarajat qo'shish ko'rinishi
@login_required(login_url="login")
def qoshish_cost(request):
    if request.method == "POST":
        form = CostForm(request.POST)  # Xarajat formasi
        if form.is_valid():
            form.save()  # Agar forma to'g'ri bo'lsa, saqlash
            return redirect("income")  # Daromad sahifasiga qaytish
    form = CostForm()
    return render(request, 'qoshish_cost.html', {"forms": form})

# Vaqt oralig'ida foyda hisoblash
def calculate_profit(request):
    if request.method == 'POST':
        # Foydalanuvchi tanlagan sanalarni olish
        start_date_str = request.POST.get('start_date')
        end_date_str = request.POST.get('end_date')

        # Sanalarni parsing qilish
        start_date = parse_date(start_date_str)
        end_date = parse_date(end_date_str)

        # Sanalar to'g'ri formatda ekanligini tekshirish
        if not start_date or not end_date:
            context = {
                'error': 'Sanalarni to\'g\'ri formatda kiriting.',
            }
            return render(request, 'income.html', context)

        # Sanalar oralig'idagi kirim va xarajatlarni olish
        incomes = Income.objects.filter(date__range=[start_date, end_date])
        costs = Cost.objects.filter(date__range=[start_date, end_date])

        # Hisoblash
        jami_income = sum(income.price * income.quantity for income in incomes)
        jami_cost = sum(cost.price for cost in costs)
        foyda = jami_income - jami_cost
        qarz = foyda < 0

        # Kontekstni shakllantirish
        context = {
            'foyda': foyda,
            'jamisumma': jami_income,
            'jamixarajat': jami_cost,
            'qarz': qarz,
            'start_date': start_date,
            'end_date': end_date,
            'income': incomes,
            'cost': costs,
        }

        return render(request, 'income.html', context)

    # GET so'rovlar uchun
    else:
        return render(request, "income.html")
    

def hodim_view(request):
    users = User.objects.all()
    context = {
        "users": users
    }
    return render(request, "staff.html", context)

def hodim_add(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            hodim = form.save(commit=False)  # Formadan ma'lumotlarni olish
            hodim.password = make_password(form.cleaned_data['password'])  # Parolni hash qilish
            hodim.save()  # Hodimni saqlash
            return redirect('hodim')  # Muvaffaqiyatli qo'shilgandan keyin redirect qilish
    else:
        form = UserForm()

    return render(request, 'staff_add.html', {'form': form})

def yangilash_hodim(request, pk):
    hodim = User.objects.get(pk=pk)
    if request.method == 'POST':
        form = UserForm(request.POST, instance=hodim)
        if form.is_valid():
            hodim = form.save(commit=False)
            
            # Parolni yangilash va hash qilish
            if 'password' in form.cleaned_data:
                hodim.password = make_password(form.cleaned_data['password'])  # Parolni hash qilish
            
            hodim.save()  # Yangilangan ma'lumotlarni saqlash
            return redirect('hodim')  # Yangilashdan so'ng redirect qilish
    else:
        form = UserForm(instance=hodim)

    return render(request, 'staff_add.html', {'form': form})

def dailywork(request):
    ish = Staffdailywork.objects.all()  # Barcha hodimlarning ishlarini olish
    context = {
        "ish": ish
    }
    return render(request, 'ish.html', context)

@login_required(login_url="login")
def dailywork_add(request):
    if request.method == "POST":
        form = WorkForm(request.POST)  # Xarajat formasi
        if form.is_valid():
            form.save()  # Agar forma to'g'ri bo'lsa, saqlash
            return redirect("dailywork")  # Daromad sahifasiga qaytish
        else:
            print(form.errors)
    else:
        form = WorkForm()  # GET so'rovi bo'lganda bo'sh forma
    return render(request, 'dailywork_add.html', {"forms": form})

