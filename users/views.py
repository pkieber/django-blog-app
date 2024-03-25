from django.shortcuts import redirect, render
from django.views import View
from .forms import UserRegisterForm

# Register and save user in database
class RegisterView(View):
    def get(self, request):
        form = UserRegisterForm()
        return render(request, "users/register.html", {"form": form}) # render register.html with form

    def post(self, request):
        form = UserRegisterForm(request.POST) # data includes username, email, password1, password2

        if form.is_valid():
            form.save()
            return redirect("index") # redirect to index page
        else:
            # Form is not valid, re-render the registration form with errors
            return render(request, "users/register.html", {"form": form})