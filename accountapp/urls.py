from django.urls import path

from accountapp.views import hello_world

app_name = "accountapp"

#5강 10분 다시보기

urlpatterns = [
    #path에 url, view 연결
    path('hello_world/', hello_world, name='hello_world')
]