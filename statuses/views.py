from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .forms import StatusForm
from .models import Status
from django.shortcuts import redirect
from django.contrib import messages
from tasks.models import Task


class StatusesView(LoginRequiredMixin, ListView):
    model = Status
    template_name = 'statuses.html'
    form_class = StatusForm
    login_url = 'login'
    context_object_name = 'statuses'


class StatusCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Status
    form_class = StatusForm
    login_url = 'login'
    success_url = reverse_lazy('statuses')
    template_name = 'create_status.html'
    success_message = gettext('Статус успешно создан')


class StatusUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Status
    form_class = StatusForm
    template_name = 'update_status.html'
    login_url = 'login'
    success_url = reverse_lazy('statuses')
    success_message = gettext('Статус успешно изменён')


class StatusDeleteView(LoginRequiredMixin, DeleteView):
    model = Status
    template_name = 'delete_status.html'
    login_url = 'login'
    success_url = reverse_lazy('statuses')
    success_message = gettext('Статус успешно удалён')

    def delete(self, *args, **kwargs):
        obj = self.get_object()
        if Task.objects.all().filter(status_id=obj.id):
            messages.error(self.request, "Этот статус используется.")
            return redirect('tasks')
        else:
            super(StatusDeleteView, self).delete(self.request, *args, **kwargs)
            return redirect(self.success_url)