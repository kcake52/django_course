from django.shortcuts import render
from django.http import HttpResponse
from .models import Todo


def todo_list(request):
    # return HttpResponse("Todo list")
    todos = Todo.objects.all()  # SELECT * FROM todo_todo -> Django Query

    search = request.GET.get("search")  # None

    if search:
        todos = todos.filter(name__icontains=search)

    # Dictionary 형태로 넘겨주기 (첫번째 인자 :request  두번째 : 템플릿  세번째 : 내용 (Context))
    return render(request, "todo/todo.html", {"todos": todos})


def todo_detail(request, pk):
    try:
        todo = Todo.objects.get(id=pk)
    except Todo.DoesNotExist:
        return HttpResponse("없는 페이지입니다.", status=404)
    return render(request, "todo/todo.html", {"todo": todo})


def todo_detail_name(request, name):
    todo = Todo.objects.filter(name__icontains=name)  # QuerySet
    first = todo.first()
    last = todo.last()

    if (todo is None):
        return HttpResponse("없는 페이지입니다.", status=404)
    return render(request, "todo/todo.html", {"todo": todo, "first": first, "last": last})
