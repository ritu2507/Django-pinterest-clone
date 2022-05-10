from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from accountapp.views import hello_world, AccountCreateView, AccountDetailView, AccountUpdateView, AccountDeleteView

app_name = "accountapp"

#5강 10분 다시보기

urlpatterns = [
    #path에 url, view 연결
    
    #함수형 view path 형식
    path('hello_world/', hello_world, name='hello_world'),


    #로그인 페이지 연결
    path('login/', LoginView.as_view(template_name='accountapp/login.html'), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),

    #클래스형 view path 형식
    path('create/', AccountCreateView.as_view(), name='create'),
    path('detail/<int:pk>', AccountDetailView.as_view(), name='detail'),
    path('update/<int:pk>', AccountUpdateView.as_view(), name='update'),
    path('delete/<int:pk>', AccountDeleteView.as_view(), name='delete'),
]