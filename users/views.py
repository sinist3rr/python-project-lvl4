from users.models import TaskUser
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


class UserCreateView(SuccessMessageMixin, CreateView):
    """User registration view."""

    template_name = 'signup.html'
    form_class = RegistrationForm
    success_url = reverse_lazy('login')
    success_message = gettext('SuccessCreateUser')


class UserListView(ListView):
    """User list view."""

    template_name = 'users.html'
    model = TaskUser
    context_object_name = 'users'


class UserLoginView(SuccessMessageMixin, LoginView):
    """User login view."""

    template_name = 'login.html'
    success_message = gettext('SuccessLoginUser')

    def get_success_url(self):
        return reverse_lazy('index')


class UserLogoutView(SuccessMessageMixin, LogoutView):
    """User logout view."""

    next_page = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated:
            messages.info(request, gettext('SuccessLogoutUser'))
        return super().dispatch(request, *args, **kwargs)


class UserUpdateView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, UpdateView):
    """Change user data view."""

    template_name = 'update.html'
    model = TaskUser
    form_class = RegistrationForm
    success_url = reverse_lazy('users')
    login_url = 'login'
    success_message = gettext('SuccessUpdateUser')

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, gettext('ErrorUserDoNotHaveRights'))
        return redirect('login')


class UserDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                     SuccessMessageMixin, DeleteView):
    """Delete user view."""

    model = TaskUser
    template_name = 'delete.html'
    login_url = 'login'
    success_url = reverse_lazy('users')
    success_message = gettext('SuccessDeleteUser')

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, self.success_message)
        return super(UserDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, gettext('ErrorUserDoNotHaveRights'))
        return redirect('login')
