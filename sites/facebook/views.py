from django.shortcuts import render
from facebook.forms import FacebookForm

# Create your views here.
def facebook_login(request):
    fm = FacebookForm()
    return render(request,"facebook/index.html",{"form":fm})