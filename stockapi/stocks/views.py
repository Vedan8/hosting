from django.shortcuts import render
from rest_framework import generics
from .models import StockData
from .serializers import StockDataSerializer

class StockDataListCreate(generics.ListCreateAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer

class StockDataRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = StockData.objects.all()
    serializer_class = StockDataSerializer
