from django import forms
from .models import Product, Cost, User, Staffdailywork
from django.contrib.auth.forms import AuthenticationForm

class CustomLoginForm(AuthenticationForm):
        class Meta:
            model = User
            fields = ['username', 'password']
            widgets = {
                'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
                'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'})
             # Boshqa maydonlar uchun widgetlar ham qo'shishingiz mumkin
            }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mahsulot nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mahsulot haqida ma\'lumot', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Narxi'}),
            'quantity': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Miqdori'}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control'}),  # ImageField uchun widget
            # Boshqa maydonlar uchun widgetlar ham qo'shishingiz mumkin
        }



class CostForm(forms.ModelForm):

    class Meta:
        model = Cost
        fields = "__all__"
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Mahsulot nomi'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Mahsulot haqida ma\'lumot', 'rows': 5}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Narxi'})
            # Boshqa maydonlar uchun widgetlar ham qo'shishingiz mumkin
        }

class UserForm(forms.ModelForm):
    
    class Meta:
        model = User
        fields = ("username", "password", "email", "phoneNumber", "age", "role")
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter username'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Enter password'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Enter email'}),
            'phoneNumber': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter phone number'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter age'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
        }

class WorkForm(forms.ModelForm):
    
    class Meta:
        model = Staffdailywork
        fields = "__all__"
        widgets = {
            'name': forms.Select(attrs={'class': 'form-control'}),
            'price': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Maoshi'})
            # Boshqa maydonlar uchun widgetlar ham qo'shishingiz mumkin
        }