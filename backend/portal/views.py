from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from .models import Region


from django.views.generic import (
    ListView, CreateView, UpdateView
)

from .form import (
    RegionForm
)
# Create your views here.
# CRUD para Región

class regionListView(ListView):
    model = Region
    template_name = "inmuebles/region_list.html"
    context_object_name = "regiones"

class RegionCreateView(CreateView):
    models = Region
    form_class = RegionForm
    template_name = "inmuebles/region_form.html"
    success_url = reverse_lazy("region_list")


class RegionUpdateView(UpdateView):
    models = Region
    form_class = RegionForm
    template_name = "inmuebles/region_form.html"
    success_url = reverse_lazy("region_list")
