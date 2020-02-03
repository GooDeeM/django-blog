from django.shortcuts import render, get_object_or_404
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic.edit import UpdateView
from django.urls import reverse_lazy

from . import forms, models

def index(request):
    return render(request, 'main/index.html')


@login_required
def profile(request):
    return render(request, 'main/profile.html')

class BlogLoginView(LoginView):
    template_name = 'main/login.html'

class BlogLogoutView(LoginRequiredMixin, LogoutView):
    template_name = 'main/logout.html'

class ChangeUserInfoView(SuccessMessageMixin, LoginRequiredMixin, UpdateView):
    model = models.BlogUser
    template_name = 'main/change_user_info.html'
    form = forms.ChangeUserInfoForm
    fields = ('username', 'email', 'first_name', 'last_name')
    success_url = reverse_lazy('main:profile')
    success_message = 'Особисті дані користувача змінено'

    def dispatch(self, request, *args, **kwargs):
        self.user_id = request.user.pk
        return super().dispatch(request, *args, **kwargs)

    def get_object(self, queryset=None):
        if not queryset:
            queryset = self.get_queryset()
        return get_object_or_404(queryset, pk=self.user_id)

class BlogPasswordChangeView(SuccessMessageMixin, LoginRequiredMixin,
                             PasswordChangeView):
    template_name = 'main/password_change.html'
    success_url = reverse_lazy('main:profile')
    success_message = 'Ваш пароль змінено!'