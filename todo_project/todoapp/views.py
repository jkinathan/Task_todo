from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Category, TodoList

# Create your views here.

def index(request): #function based view
    todos = TodoList.objects.all() #quering all todos with the object manager
    categories = Category.objects.all() #getting all categories with object manager
    
    if request.method == "POST":
        #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo
            
            titler = request.POST["description"] 
            dater = str(request.POST["date"]) 
            categoryr = request.POST["category_select"] #category
            contentr = titler + " -- " + dater + " " + categoryr #content
            Todo = TodoList(title=titler, content=contentr, due_date=dater, category=Category.objects.get(name=categoryr))
            Todo.save() #saving the todo 
            
            return redirect("/") #reloading the page
        
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    return render(request, "index.html", {"todos": todos, "categories":categories})