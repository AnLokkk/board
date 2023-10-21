from allauth.account.forms import SignupForm
from django.core.mail import send_mail
from django.contrib.auth.models import Group, User
from D16.models import Post


class CustomSignupForm(SignupForm):
    def save(self, request):
        user = super().save(request)
        login_users = Group.objects.get(name='login_users')
        user.groups.add(login_users)
        Post.objects.create(author=User.objects.get(pk=user.id))
        send_mail(
            subject='Добро пожаловать!!!',
            message=f'{user.username}, вы успешно зарегистрировались!',
            from_email=None,
            recipient_list=[user.email],
        )
        return user


