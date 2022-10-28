from django.shortcuts import render,redirect
from .models import *
from django.views import View
from django.contrib.auth import authenticate
# Create your views here.


class LoginView(View):
    def get(self,request):
        return render(request, 'login.html')
    def post(self,request):
        if request.user.is_authenticated:
            return redirect('/www/blog/')
        else:
            return redirect('/www/login/')


class RegisterView(View):
    def get(self,request):
        return render(request,'register.html')
    def post(self,request):
        Muallifi.objects.create(
            ism = request.POST.get('ism'),
            yosh = request.POST.get('yosh'),
            kasb = request.POST.get('kasb'),
            user = request.user,
        )
        return redirect('/www/blog/')

class BlogView(View):
    def get(self,request):
        data = {
            'maqolalar': Maqola.objects.all(),
            'mualliflar': Muallifi.objects.all(),
        }
        return render(request, 'blog.html', data)

    def post(self,request):
        Maqola.objects.create(
            sarlavha = request.POST.get('sarlavha'),
            sana = request.POST.get('sana'),
            mavzu = request.POST.get('mavzu'),
            matn = request.POST.get('matn'),
            muallif = Muallifi.objects.get(id=request.POST.get('muallif')),
        )
        return redirect('/www/blog/')

class MaqolaView(View):
    def get(self,request,son):
        context = {
            'maqola': Maqola.objects.get(id=son)
        }
        return render(request, 'maqola.html', context)

