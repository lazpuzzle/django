from django.shortcuts import render
from django.http import HttpResponse
from .models import Staff, Product, ContactUs
# Create your views here.
def Homepage(request):
    product = Product.objects.all()
    context = {"product": product}
    return render(request, 'myapp/home.html', context)

def About(request):
    return render(request, 'myapp/about.html')

def Allservice(request):
    return render(request, 'myapp/allservice.html')

def Contact(request):
    namelist = Staff.objects.all()
    context = {'namelist':namelist}
    
    if request.method == 'POST':
        newcontact = ContactUs()
        data = request.POST.copy()
        newcontact.name = data.get('name')
        newcontact.title = data.get('title')
        newcontact.detail = data.get('detail')
        newcontact.email = data.get('email')
        newcontact.save()
        context['alert'] = 'success'
    
    
    return render(request, "myapp/contact.html", context)

def Store(request):
    return render(request, "myapp/store.html")