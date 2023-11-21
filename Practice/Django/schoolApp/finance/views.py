from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def feeCollection(req):
    return render(req, 'finance/feecollect.html')

def feeDuesReport(req):
    return render(req, 'finance/feeDuesReport.html')

def feeCollectionReport(req):
    return render(req, 'finance/collectionsreport.html')