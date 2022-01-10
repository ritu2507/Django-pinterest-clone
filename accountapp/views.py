from django.http import HttpResponse
from django.shortcuts import render

# 동작들 작성

def hello_world(request):
    return HttpResponse('hello world!')