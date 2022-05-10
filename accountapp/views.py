from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy   #reverse은 함수형 뷰에서, reverse_lazy는 클래스형 뷰에서 사용


# 동작들 작성
from accountapp.forms import AccountUpdateForm


def hello_world(request):

    # 현재 존재하는 app의 temtplates에서 html 갖다씀
    return render(request, 'accountapp/hello_world.html')

    # return render(request, 'base.html') #base.html 페이지 로드 : templates의 html 갖다쓰려면 settings.py에 TEMPLATES 파일 수정 필요
    # return HttpResponse('hello world!') : hello world! 문구만 출력


# 함수형 뷰보다 간단 : django 기본 제공 템플릿들 사용
class AccountCreateView(CreateView):   #회원가입
    model = User          #django의 기본 제공 모델을 상속받아 사용
    form_class = UserCreationForm          #모델과 마찬가지로 django 기본 제공 템플릿 사용
    success_url = reverse_lazy('accountapp:hello_world')   #계정 만들기(class 기능) 성공 후에는 어느 url로 재연결 할것인가 경로지정
    template_name = 'accountapp/create.html' #회원 가입시 보일 html 지정

#세부 페이지 view
class AccountDetailView(DetailView):
        model = User
        context_object_name = 'target_user' # 내 계정의 user 이름을 target_user로 지정
        template_name = 'accountapp/detail.html'

#업데이트 view
class AccountUpdateView(UpdateView):   #회원가입
    model = User          #django의 기본 제공 모델을 상속받아 사용
    form_class = AccountUpdateForm         #forms.py에서 커스텀한 form 사용
    success_url = reverse_lazy('accountapp:hello_world')   #업데이트(class 기능) 성공 후에는 어느 url로 재연결 할것인가 경로지정
    template_name = 'accountapp/update.html' #업데이트시 보일 html 지정

#회원탈퇴 View
class AccountDeleteView(DeleteView):
    model = User
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'