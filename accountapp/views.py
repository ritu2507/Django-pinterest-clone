from django.http import HttpResponse
from django.shortcuts import render

# 동작들 작성

def hello_world(request):
    return render(request, 'base.html') #base.html 페이지 로드 : templates의 html 갖다쓰려면 settings.py에 TEMPLATES 파일 수정 필요
    # return HttpResponse('hello world!') : hello world! 문구만 출력 