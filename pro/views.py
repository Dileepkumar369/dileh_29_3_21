from django.shortcuts import render
from django.http import HttpResponse
def rend_demo(request):
    return render(request,"sam.html")
def sam_demo(request):
    return render(request,"html_demo/sample.html")