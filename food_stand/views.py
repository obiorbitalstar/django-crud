from django.shortcuts import render
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .models import Menu
# Create your views here.

class HomeView(ListView):
    template_name = 'home.html'
    model = Menu
    
class DishDetailView(DeleteView):
    template_name = 'details.html'
    model = Menu
class DishCreateView(CreateView):
    template_name='create.html'
    model = Menu
    fields = ['dish_name','customer','price','description']
class DishUpdateView(UpdateView):
    template_name = 'update.html'
    model= Menu
    fields = ['dish_name','customer','price','description']
class DishDeleteView(DeleteView):
    template_name='delete.html'
    model = Menu
    success_url = reverse_lazy('home')
    