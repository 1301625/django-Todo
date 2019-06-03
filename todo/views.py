from django.shortcuts import render
from .models import Todo
from django.http import JsonResponse

from django.views.decorators.csrf import csrf_exempt

"""
    목록을 불러오는 역할
    저장된 모든 할 일 데이터를 불러온 후에 하나씩 json데이터로 가공할 수 있게 사전형 데이터로 저장
    :return Json반환
"""
def todo_fetch(request):
    todos = Todo.objects.all()
    todo_list = []
    for index, todo in enumerate(todos, start=1):
        todo_list.append({'id': 'index', 'title': todo.title, 'completed': todo.completed})

    return JsonResponse(todo_list, safe=False)



