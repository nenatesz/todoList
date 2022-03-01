from django.http.response import HttpResponseRedirect
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User

from .forms import createNewList
from .models import ToDoList, Item

# Create your views here.

def index(response, id):
    ls = ToDoList.objects.get(id=id)
    # item = ls.item_set.get(id=1)
    if response.method == "POST":
        print(response.POST)
        # this is a custom form
        # get buttons using the name attribute
        if response.POST.get("save"):
            # the information ({name:[value]} pairs) in the form linked to the button gets added as a dictionary
            for item in ls.item_set.all():
                # get the checkbox using the name attribute
                if response.POST.get("c" + str(item.id)) == "clicked":
                    item.complete = True
                else:
                    item.complete = False
                item.save()

        elif response.POST.get("newItem"):
            txt = response.POST.get("new")
            # validate to ensure that the field is not empty
            if len(txt) > 2:
              ls.item_set.create(text=txt, complete=False)
            else:
                print("Invalid Input")
              
    return render(response, "main/list.html", {"ls": ls})

def home(response):
    return render(response, "main/home.html", {})

def create(response):
    if response.method == "POST":
        # default response method is get, so we have to set a condition to allow fro a post method
        form = createNewList(response.POST)
        if form.is_valid():
            # clean incoming data on the form
            n = form.cleaned_data["name"]
            t = ToDoList(name=n)
            t.save()
            response.user.todolist.add(t)
           
        # if post method is successful, redirect
        return HttpResponseRedirect("/%i" %t.id)

    else:
        form = createNewList()
    return render(response, "main/create.html", {"form": form})

def view(response):
    
    return render(response, "main/view.html", {})