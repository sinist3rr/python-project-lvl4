from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import CreateView, DeleteView, DetailView, UpdateView
from .forms import TaskForm
from .models import Task
from django.shortcuts import redirect
from django_filters.views import FilterView
from .filters import TasksFilter
from users.models import TaskUser


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
    success_message = gettext('SuccessCreateTask')

    def form_valid(self, form):
        form.instance.creator = TaskUser.objects.get(id=self.request.user.id)
        return super().form_valid(form)


class TasksUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_update.html'
    login_url = 'login'
    success_url = reverse_lazy('tasks')
    success_message = gettext('SuccessUpdateTask')


class TasksDeleteView(LoginRequiredMixin, UserPassesTestMixin,
                      SuccessMessageMixin, DeleteView):
    model = Task
    template_name = 'task_delete.html'
    success_url = reverse_lazy('tasks')
    login_url = 'login'
    success_message = gettext('SuccessDeleteTask')

    def delete(self, request, *args, **kwargs):
        obj = self.get_object()
        messages.success(self.request, self.success_message % obj.__dict__)
        return super(TasksDeleteView, self).delete(request, *args, **kwargs)

    def test_func(self):
        return self.get_object().creator.id == self.request.user.id

    def handle_no_permission(self):
        messages.error(self.request, gettext('CannotDeleteTask'))
        return redirect('tasks')
