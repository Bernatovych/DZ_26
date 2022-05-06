from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from finance_app.forms import PeriodReportForm
from finance_app.models import Income, Expens, Category
from datetime import date
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.mixins import LoginRequiredMixin


@login_required
def home(request):
    user = request.user
    income = Income.objects.filter(user=user).filter(date=date.today()).aggregate(Sum('money'))['money__sum'] or 0
    expens = Expens.objects.filter(user=user).filter(date=date.today()).aggregate(Sum('money'))['money__sum'] or 0
    return render(request, 'home.html', {'income': income, 'expens': expens})


@login_required
def period_report(request):
    user = request.user
    form = PeriodReportForm()
    income = None
    all_expens = None
    category_expens = None
    search_time = None
    if request.method == 'POST':
        form = PeriodReportForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
            income = Income.objects.filter(user=user).filter(date__range=[start_date, end_date]).aggregate(Sum('money'))['money__sum'] or 0
            expens = Expens.objects.filter(user=user).filter(date__range=[start_date, end_date])
            category_expens = expens.values('category__name').annotate(money_sum=Sum('money')).order_by('-money_sum')
            all_expens = expens.aggregate(Sum('money'))['money__sum'] or 0
            search_time = f'{start_date} - {end_date}'
    return render(request, 'period_report.html', {'form': form, 'income': income, 'category_expens': category_expens,
                                                  'all_expens': all_expens, 'search_time': search_time})


class CategoryListView(LoginRequiredMixin, ListView):
    template_name = 'category_list.html'

    def get_queryset(self):
        return Category.objects.filter(user=self.request.user)


class CategoryAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Category
    fields = ['name']
    template_name = 'category_add.html'
    success_url = reverse_lazy('category_list')
    success_message = "Category %(name)s was created successfully"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(CategoryAddView, self).form_valid(form)


class CategoryUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Category
    fields = ['name']
    template_name = 'category_add.html'
    success_url = reverse_lazy('category_list')
    success_message = "Category %(name)s was updated successfully"


class CategoryDeleteView(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    model = Category
    template_name = 'category_delete.html'
    success_url = reverse_lazy('category_list')
    success_message = "Category was deleted successfully"


class ExpensAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Expens
    fields = ['money', 'category']
    template_name = 'sum_add.html'
    success_url = reverse_lazy('home')
    success_message = "Expens sum %(money)s was created successfully"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(ExpensAddView, self).form_valid(form)


class IncomeAddView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Income
    fields = ['money']
    template_name = 'sum_add.html'
    success_url = reverse_lazy('home')
    success_message = "Income sum %(money)s was created successfully"

    def form_valid(self, form):
        obj = form.save(commit=False)
        obj.user = self.request.user
        return super(IncomeAddView, self).form_valid(form)