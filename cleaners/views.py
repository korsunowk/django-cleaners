from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Cleaner
from .forms import CleanerForm


class CleanerList(ListView):
    model = Cleaner


class CleanerDetail(DetailView):
    model = Cleaner


class CleanerCreation(CreateView):
    model = Cleaner
    form_class = CleanerForm
    success_url = reverse_lazy('cleaners:list')


class CleanerUpdate(UpdateView):
    model = Cleaner
    form_class = CleanerForm
    success_url = reverse_lazy('cleaners:list')


class CleanerDelete(DeleteView):
    model = Cleaner
    success_url = reverse_lazy('cleaners:list')
