from rest_framework import status, generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import TodoSerializer
from .models import Todo

class TodoCreateAPI(APIView):
    def post(self, request) :
        serializer = TodoSerializer(data=request.data)
        # ModelSerializer가 Todo 모델을 검증해준다.
        serializer.is_valid(raise_exception=True) # 예외 발생 시 Error를 발생시켜라
        todo = serializer.save()
        return Response(TodoSerializer(todo).data, status=status.HTTP_201_CREATED) # json으로 변경 / Dictionary 형태로 전달
    
class TodoListAPI(APIView):
    def get(self, request) : 
        todos = Todo.objects.all() # QuerySet = Object list
        serializer = TodoSerializer(todos, many=True) # data가 복수개일 때 (QuerySet일 때)
        return Response(serializer.data) # status의 default 값은 200 -> 생략 가능
    
class TodoRetrieveAPI(APIView) :
    def get(serlf, request, pk) : 
        try : 
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    
class TodoUpdateAPI(APIView) : 
    
    def put(self, request, pk) : 
        try : 
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data)
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
    
    def patch(self, request, pk) : 
        try : 
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        serializer = TodoSerializer(todo, data=request.data, partial=True) # 일부 수정 허용
        serializer.is_valid(raise_exception=True)
        todo = serializer.save()
        
        serializer = TodoSerializer(todo)
        return Response(serializer.data)
        # return Response(TodoSerializer(todo).data)
        
class TodoDeleteAPI(APIView) : 
    def delete(self, request, pk) :
        try : 
            todo = Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            return Response({"error":"해당하는 todo가 없습니다."}, status=status.HTTP_404_NOT_FOUND)
        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) # 204를 사용하면 data를 보낼 수가 없다.
    
class TodoGenericsCreateAPI(generics.CreateAPIView) : 
    serializer_class = TodoSerializer
    
class TodoGenericsListAPI(generics.ListAPIView) : 
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoGenericsListCreateAPI(generics.ListCreateAPIView) : 
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoGenericsRetrieveAPI(generics.RetrieveAPIView) : 
    queryset = Todo.objects.all()
    # 전체를 받지만 pk를 넘겨 원하는 객체 하나만 받을 수 있다.
    serializer_class = TodoSerializer
    
class TodoGenericsUpdateAPI(generics.UpdateAPIView) : 
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoGenericsDeleteAPI(generics.DestroyAPIView) : 
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
    
class TodoGenericsRetrieveUpdateDeleteAPI(generics.RetrieveUpdateDestroyAPIView) : 
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer