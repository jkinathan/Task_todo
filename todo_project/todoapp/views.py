from django.shortcuts import render
from django.views.generic import ListView
from .models import Category, TodoList
# Create your views here.

class TodoListView(ListView):
    model = TodoList
    template_name = "todolist.html"
    fields = ('title','content','created','due_date','category')
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
