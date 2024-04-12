from django.shortcuts import render,redirect,get_object_or_404
import requests   
def bus_faq(request):
    return render(request,"bus_templates/com.html")
def bus_form(request):
    return render(request,"bus_templates/index.html")