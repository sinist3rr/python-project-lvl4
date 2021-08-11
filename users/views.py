from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from users.forms import RegistrationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.shortcuts import redirect
from django.utils.translation import gettext
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


class UserCreateView(CreateView):
    """User registration view."""

    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')


class UserListView(ListView):
    """User list view."""

    template_name = 'users.html'
    model = User
    context_object_name = 'users'


class UserLoginView(SuccessMessageMixin, LoginView):
    """User login view."""

    template_name = 'login.html'
    success_message = gettext('Вы залогинены')

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    """User logout view."""

    next_page = reverse_lazy('index')
    success_message = gettext('Вы разлогинены')


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, UpdateView):
    """Change user data view."""

    template_name = 'update.html'
    model = User
    form_class = RegistrationForm
    success_url = reverse_lazy('users')
    login_url = 'login'
    success_message = gettext('Пользователь успешно изменён')

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав')
        return redirect('login')


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):
    """Delete user view."""

    model = User
    template_name = 'delete.html'
    login_url = 'login'
    success_url = reverse_lazy('index')
    success_message = gettext('Пользователь успешно удалён')

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, 'У вас нет прав')
        return redirect('login')
