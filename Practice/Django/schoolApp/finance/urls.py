from django.urls import path
from finance.views import feeCollection
from finance.views import feeDuesReport
from finance.views import feeCollectionReport

urlpatterns = [
   
    path('feecoll/', feeCollection),
    path('collectionsreport/', feeCollectionReport),
    path('duesreport/', feeDuesReport),
]