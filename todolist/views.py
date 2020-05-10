from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from details.models import Faculty
from django.utils import timezone
from .models import TodoList, Category


def index(request): #the index view
    todos = TodoList.objects.filter(faculty=Faculty.objects.get(faculty_id= request.session.get('faculty_id', None))) #quering all todos with the object mana

    print("todos",todos)
    categories = Category.objects.all() #getting all categories with object manager
    if request.method == "POST": #checking if the request method is a POST
        if "taskAdd" in request.POST: #checking if there is a request to add a todo

            faculty=Faculty.objects.get(faculty_id= request.session.get('faculty_id', None))
            title = request.POST["description"] #title
            date = str(request.POST["date"]) #date
            category = request.POST["category_select"] #category
            content = title + " -- " + date + " " + category #content
            Todo = TodoList(title=title, content=content, due_date=date, category=Category.objects.get(name=category),faculty=faculty)
            Todo.save() #saving the todo
            return redirect("/") #reloading the page
        if "taskDelete" in request.POST: #checking if there is a request to delete a todo
            checkedlist = request.POST["checkedbox"] #checked todos to be deleted
            for todo_id in checkedlist:
                todo = TodoList.objects.get(id=int(todo_id)) #getting todo id
                todo.delete() #deleting todo
    notificationArr = []
    if(todos):
        for todo in todos:
            print(todo.due_date,timezone.now().strftime("%Y-%m-%d"))
            if str(todo.due_date) == str(timezone.now().strftime("%Y-%m-%d")):
                print(todo.due_date,timezone.now().strftime("%Y-%m-%d"))
                notificationArr.append(todo)
    return render(request, "index.html", {"todos": todos, "categories":categories,"notification":notificationArr,'request':request})

# def notification(request):
#     todos=TodoList.objects.all()
#     categories=Category.objects.all()
#     notificationArr=[]
#     for todo in todos:
#         if todo.due_date ==timezone.now().strftime("%Y-%m-%d"):
#             notificationArr.append(todo)
#     return render(request,"index.html")

