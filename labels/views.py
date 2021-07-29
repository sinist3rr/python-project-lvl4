from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.shortcuts import redirect
from django.urls import reverse_lazy
from django.utils.translation import gettext
from django.views.generic import CreateView, DeleteView, UpdateView
from django.views.generic.list import ListView
from .forms import LabelForm
from .models import Label
from tasks.models import Task


class LabelsView(LoginRequiredMixin, ListView):
    model = Label
    template_name = 'labels.html'
    form_class = LabelForm
    login_url = 'login'


class LabelCreateView(LoginRequiredMixin, SuccessMessageMixin, CreateView):
    model = Label
    form_class = LabelForm
    login_url = 'login'
    success_url = reverse_lazy('labels')
    template_name = 'create_label.html'
    success_message = gettext('Метка успешно создана')


class LabelUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    model = Label
    form_class = LabelForm
    template_name = 'update_label.html'
    login_url = 'login'
    success_url = reverse_lazy('labels')
    success_message = gettext('Метка успешно изменена')


class LabelDeleteView(LoginRequiredMixin, DeleteView):
    model = Label
    template_name = 'delete_label.html'
    login_url = 'login'
    success_url = reverse_lazy('labels')
    success_message = gettext('Метка успешно удалена')

    def delete(self, *args, **kwargs):
        obj = self.get_object()
        if Task.objects.filter(labels__id=obj.id):
            messages.error(self.request, "Эта метка используется.")
            return redirect('labels')
        else:
            super(LabelDeleteView, self).delete(self.request, *args, **kwargs)
            return redirect(self.success_url)