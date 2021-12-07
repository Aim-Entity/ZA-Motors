from django.urls import path
from . import views

urlpatterns = [
    path("", views.StockAllListView.as_view(), name="stock"),
    path("item/<str:slug>", views.StockAllDetailView.as_view(), name="stock-detail")
]
