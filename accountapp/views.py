from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.utils.decorators import method_decorator
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.urls import reverse,reverse_lazy   #reverse은 함수형 뷰에서, reverse_lazy는 클래스형 뷰에서 사용


# 커스텀 import
from accountapp.decorators import account_ownership_required
from accountapp.forms import AccountUpdateForm

#method decorator들 목록을 배열로 넣기
has_ownership = [account_ownership_required, login_required]

@login_required
def hello_world(request):
        # main페이지 반환
        return render(request, 'accountapp/hello_world.html')


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
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountUpdateView(UpdateView):   #회원가입
    model = User          #django의 기본 제공 모델을 상속받아 사용
    context_object_name = 'target_user'
    form_class = AccountUpdateForm         #forms.py에서 커스텀한 form 사용
    success_url = reverse_lazy('accountapp:hello_world')   #업데이트(class 기능) 성공 후에는 어느 url로 재연결 할것인가 경로지정
    template_name = 'accountapp/update.html' #업데이트시 보일 html 지정

#회원탈퇴 View
@method_decorator(has_ownership, 'get')
@method_decorator(has_ownership, 'post')
class AccountDeleteView(DeleteView):
    model = User
    context_object_name = 'target_user'
    success_url = reverse_lazy('accountapp:login')
    template_name = 'accountapp/delete.html'