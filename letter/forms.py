from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['title', 'name', 'content', 'pw']
        widgets = {
            'title' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '편지 제목',
                    'rows' : '1',
                }
            ),
            'content' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '편지를 작성해주세요 :)',
                }
            ),
            'name' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '받는 사람',
                    'rows' : '1',
                }
            ),
            'pw' : forms.Textarea(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : '4자리 비밀번호 설정',
                    'rows' : '1',
                }
            )
        }