from django.contrib.auth.forms import UserCreationForm


class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        #초기화
        super().__init__(*args, **kwargs)

        #초기화 이후에 username은 바꾸지 못하도록 : username 수정이 서버에 반영되지 않음
        self.fields['username'].disabled = True