from django.shortcuts import render
from django.views import View
from .forms import UserRegisterForm

# Register and save user in database
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form}) # render register.html with form

    def post(self, request):
        pass