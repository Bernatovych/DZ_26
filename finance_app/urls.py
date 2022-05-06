from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path
from finance_app import views


urlpatterns = [
    path('', views.home, name='home'),
    path('period_report/', views.period_report, name='period_report'),
    path('category_list/', views.CategoryListView.as_view(), name='category_list'),
    path('category_add/', views.CategoryAddView.as_view(), name='category_add'),
    path('category_update/<int:pk>/', views.CategoryUpdateView.as_view(), name='category_update'),
    path('category_delete/<int:pk>/', views.CategoryDeleteView.as_view(), name='category_delete'),
    path('expens_add/', views.ExpensAddView.as_view(), name='expens_add'),
    path('income_add/', views.IncomeAddView.as_view(), name='income_add'),

]