from django.urls import path
from .views import StockDataListCreate, StockDataRetrieveUpdateDestroy

urlpatterns = [
    path('stock-data/', StockDataListCreate.as_view(), name='stock-data-list-create'),
    path('stock-data/<int:pk>/', StockDataRetrieveUpdateDestroy.as_view(), name='stock-data-detail'),
]
