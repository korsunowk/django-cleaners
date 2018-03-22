from django.core.urlresolvers import reverse_lazy

from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import (
    CreateView,
    UpdateView,
    DeleteView
)

from .models import Town


class TownList(ListView):
    model = Town


class TownDetail(DetailView):
    model = Town


class TownCreation(CreateView):
    model = Town
    success_url = reverse_lazy('towns:list')
    fields = ['name']


class TownUpdate(UpdateView):
    model = Town
    success_url = reverse_lazy('towns:list')
    fields = ['name']


class TownDelete(DeleteView):
    model = Town
    success_url = reverse_lazy('towns:list')
