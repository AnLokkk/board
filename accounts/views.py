from django.contrib.auth.models import User
from django.views.generic.edit import CreateView
from allauth.account.forms import SignupForm
from django.contrib.auth.decorators import login_required


class SignUp(CreateView):
    model = User
    form_class = SignupForm
    success_url = '/accounts/login'