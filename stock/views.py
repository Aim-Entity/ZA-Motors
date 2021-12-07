from django.shortcuts import render
from django.views.generic import DetailView, ListView
from .models import Car
from .filters import CarFilter


class StockAllListView(ListView):
    template_name = "stock/stock.html"
    queryset = Car.objects.all()

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['filter'] = CarFilter(
            self.request.GET, queryset=self.get_queryset())

        return context


class StockAllDetailView(DetailView):
    template_name = "stock/stock_detail.html"
    queryset = Car.objects.all()
