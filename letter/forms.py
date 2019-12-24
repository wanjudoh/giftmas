from django import forms
from .models import Letter

class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        fields = ['title', 'name', 'content']
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
            )
        }