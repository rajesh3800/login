from django.shortcuts import render,HttpResponse
from app.models import *

# Create your views here.
def home(request):
    d={'name':'rajesh',
       'age':22,
       'pay':1500} 
    return render(request,'home.html',d)

def login(request):
    if request.method=='POST':
        users = Details.objects.all()
        user = request.POST.get('user')
        ps = request.POST.get('ps')
        for ur in users:
            if ur.username == user:
                if ur.password == ps:
                    d={'ur':ur}
                    return render(request,'home.html', d)
                return HttpResponse('invalid password')
        else:
            return HttpResponse('invalid Username')
                
        
    return render(request,'login.html')


def register(request):
    if request.method=='POST':
        em=request.POST.get('em')
        user=request.POST.get('user')
        ps=request.POST.get('ps')
        
        CDO=Details(email=em,username=user,password=ps)
        CDO.save()
        
        
        return render(request,'login.html')
    return render(request,'register.html')
