from django.shortcuts import render,redirect
from .forms import CustomRegisterForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method=="POST":
        register_forms=CustomRegisterForm(request.POST)
        if register_forms.is_valid():
            register_forms.save()
            messages.success(request,("Created Successfully"))
        return redirect('todolist')
    else:
        register_forms=CustomRegisterForm()
    return render(request,'register.html',{'register_forms':register_forms})