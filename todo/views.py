from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def todo_list(request) :
    # return HttpResponse("Todo list")
    todos = Todo.objects.all() # SELECT * FROM todo_todo -> Django Query
    return render(request, "todo.html", {"todos" : todos}) # Dictionary 형태로 넘겨주기 (첫번째 인자 :request  두번째 : 템플릿  세번째 : 내용 (Context))
