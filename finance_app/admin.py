from django.contrib import admin
from .models import Income, Expens, Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name',)


@admin.register(Income)
class IncomeAdmin(admin.ModelAdmin):
    list_display = ('money', 'date')
    list_filter = ('date',)


@admin.register(Expens)
class ExpensAdmin(admin.ModelAdmin):
    list_display = ('category', 'money', 'date')
    list_filter = ('category', 'date')
