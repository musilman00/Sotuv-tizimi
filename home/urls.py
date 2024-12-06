from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path("", views.home, name="home"),
    path("korish_product/<int:pk>", views.korish_product, name="korish_product"),
    path("qoshish_product/", views.qoshish_product, name="qoshish_product"),
    path("income/", views.income, name="income"),
    path("qoshish_cost/", views.qoshish_cost, name="qoshish_cost"),
    path("calculate_profit/", views.calculate_profit, name="calculate_profit"),
    path('login/', auth_views.LoginView.as_view(template_name="login.html"), name='login'),
    path('logout/', views.logout_view, name='logout'),  # Chiqish yo'li
    path("hodim",  views.hodim_view, name="hodim"),
    path("hodim_add",  views.hodim_add, name="hodim_add"),
    path("yangilash_hodim/<int:pk>",  views.yangilash_hodim, name="yangilash_hodim"),
    path("dailywork",  views.dailywork, name="dailywork"),
    path("dailywork_add",  views.dailywork_add, name="dailywork_add"),




]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
