from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from django.views.generic.list import ListView
from django.contrib.auth.models import User
from .forms import TaskForm
from .models import Task
from django.shortcuts import redirect
from django_filters.views import FilterView
from .filters import TasksFilter


class TasksDetailView(LoginRequiredMixin, DetailView):
    model = Task
    template_name = 'task_detail.html'


class TasksView(LoginRequiredMixin, FilterView):
    model = Task
    template_name = 'tasks.html'
    login_url = 'login'
    filterset_class = TasksFilter
    context_object_name = 'tasks'


class TasksCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Task
    form_class = TaskForm
    login_url = 'login'
    success_url = reverse_lazy('tasks')
    template_name = 'task_create.html'
    success_message = gettext('Задача успешно создана')

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    login_url = 'login'
    success_url = reverse_lazy('tasks')
    success_message = gettext('Задача успешно изменена')


class TasksDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks')
    login_url = 'login'
    success_message = gettext('Задача успешно удалена')

    def test_func(self):
        return self.get_object().creator.id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, 'Задачу может удалить только её автор')
        return redirect('tasks')
