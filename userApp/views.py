from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views import View


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect('bolimlar')
        return redirect('login')

class Logout(View):
    def get(self, request):
        logout(request)
        return redirect('/login')



