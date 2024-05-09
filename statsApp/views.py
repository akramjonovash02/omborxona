from django.shortcuts import render, redirect
from django.views import View
from  .models import *


class Stats(View):
    def get(self, request):
        current_user = request.user
        if current_user.is_authenticated and isinstance(current_user, Tarqatuvchi):
            statistiklar = Sotuv.objects.filter(tarqatuvchi=current_user)
            return render(request, 'statistikalar.html', {'statistiklar': statistiklar})
        return redirect('login')
