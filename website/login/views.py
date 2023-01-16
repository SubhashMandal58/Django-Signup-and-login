from django.shortcuts import render
from .models import Cred
from django.http import HttpResponse

# Create your views here.
def index(request):
    if request.method == 'POST':
        mail = request.POST['email']
        user = request.POST['username']
        passw = request.POST['password']
        confirm = request.POST['conpass']
        
        if confirm == passw:
            new_user= Cred(email=mail, username=user, password=passw)
            new_user.save()
        else:
            return HttpResponse('Error,password doesnot match')
        
    return render(request,'index.html')

