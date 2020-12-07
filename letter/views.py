from django.shortcuts import render, redirect, get_object_or_404
from .forms import LetterForm
from .models import Letter, Gift
from django.http import HttpResponse


def home(request):
    return render(request, 'home.html')

def new(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        if form.is_valid():
            letter = form.save(commit=False)
            letter.title = form.cleaned_data['title']
            letter.content = form.cleaned_data['content']
            letter.name = form.cleaned_data['name']
            import random
            letter.gift = Gift.objects.get(pk=random.randint(1, 11))
            letter.design = request.POST['design']
            letter.save()
            return render(request, 'link.html', {'letter':letter})
        else:
            return HttpResponse('알 수 없는 에러가 발생했습니다 ㅠㅠ 다시입력해주세요!')
    else:
        form = LetterForm()
        return render(request, 'new.html', {'form':form})

def detail(request, letter_id):
    letter = get_object_or_404(Letter, pk=letter_id)
    return render(request, 'detail.html', {'letter':letter})