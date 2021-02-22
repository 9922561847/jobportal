from django.http import HttpResponse
from django.shortcuts import render
from .models import register

# Create your views here.
def home(request):
    return render(request, 'home.html')

def log(request):
    return render(request,'log.html')
def register_data(request):
    return render(request,'register.html')
def reg(request):
    f1 = register()
    f1.name = request.POST['name']
    f1.mobile = request.POST['mobile']
    f1.email = request.POST['mail']
    f1.password = request.POST['pass']
    f1.file = request.POST['cv']
    f1.save()
    return render(request,'register.html')

def administrator(request):

    data = register.objects.all()
    return render(request, 'reg.html', {'x': data})
def logging(request):
    return render(request,'jobs.html')
def Home(request):
    return render(request,'home.html')
def editfunction(request,id):
    f2 =register.objects.get(id=id)
    if request.method == 'POST':
        f2.name = request.POST['name']
        f2.mobile = request.POST['mobile']
        f2.email = request.POST['mail']
        f2.password = request.POST['pass']
        f2.file = request.POST['cv']
        f2.save()
        data = register.objects.all()
        return render(request, 'reg.html', {'x': data})
    return render(request ,'editing.html',{'x':f2})
def deletefunction(request, id):
    f3 = register.objects.get(id=id)
    f3.delete()
    data = register.objects.all()
    return render(request, 'reg.html', {'x': data})


