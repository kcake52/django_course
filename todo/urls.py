from django.urls import path
from .apis import *
from .views import *

# 127.0.0.1:8000/todo/
urlpatterns = [
    path("create/", TodoCreateAPI.as_view()),
    path("list/", TodoListAPI.as_view()),
    path("retrieve/<int:pk>/", TodoRetrieveAPI.as_view()),
    path("update/<int:pk>/", TodoUpdateAPI.as_view()),
    path("delete/<int:pk>/", TodoDeleteAPI.as_view()),
    path("list/", todo_list),  # 127.0.0.1:8000/todo/list
    # 127.0.0.1:8000/todo/<int:pk> / pk = 135 135번 todo를 찾아서 리턴
    path("<int:pk>/", todo_detail),
    # 127.0.0.1:8000/todo/<str:name> / name = 공부 todo를 찾아서 리턴
    path("<str:name>/", todo_detail_name),
]