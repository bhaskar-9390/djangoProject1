from django.shortcuts import render
from django.http import HttpResponse
def input(request):
    return render(request,template_name,input.html)
def add(request):
    x=request.Get["t1"]
    y=request.Get["t2"]
    i=int(x)
    j=int(y)
    z=i+j
    res=HttpResponse("the sum is:"str(z))
    return res