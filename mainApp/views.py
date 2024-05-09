from django.shortcuts import render, redirect, get_object_or_404
from django.views import View

from mainApp.models import *


class Bolimlar(View):
    def get(self, request):
        return render(request, "bo'limlar.html")

class Mahsulotlar(View):
    def get(self, request):
        if request.user.is_authenticated and request.user.is_superuser == False:
            mahsulotlar = Mahsulot.objects.filter(tarqatuvchi=request.user)
            context = {
                'mahsulotlar': mahsulotlar
            }
            return render(request, "mahsulotlar.html", context)
        return redirect('/login')



class Mijozlar(View):
    def get(self, request):
        current_user = request.user
        if current_user.is_authenticated and isinstance(current_user, Tarqatuvchi):
            mijozlar = Mijoz.objects.filter(tarqatuvchi=current_user)
            return render(request, 'mijozlar.html', {'mijozlar': mijozlar})
        return redirect('login')

class MahsulotDeleteView(View):
    def get(self,request, pk):
        if request.user.is_authenticated:
            mahsulot = get_object_or_404(Mahsulot, id=pk)
            if mahsulot.user == request.user:
                mahsulot.delete()
                return redirect('mahsulotlar/')
            return redirect('logout')
        return redirect('login')