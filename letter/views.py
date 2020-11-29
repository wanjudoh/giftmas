from django.shortcuts import render, redirect, get_object_or_404
from .forms import LetterForm
from .models import Letter
from django.http import HttpResponse
#import socket

# Create your views here.

def home(request):
    return render(request, 'home.html')

def new(request):
    if request.method == 'POST':
        form = LetterForm(request.POST)
        # gift = request.POST['gift']
        if form.is_valid():
            #if len(form.cleaned_data['pw']) < 4:
            #    return render(request, 'new.html', {'form':form, 'error':'비밀번호는 4자로 입력합니다.', 'gift':gift})
            letter = form.save(commit=False)
            letter.title = form.cleaned_data['title']
            letter.content = form.cleaned_data['content']
            letter.name = form.cleaned_data['name']
            letter.gift = 0
            letter.design = request.POST['design']
            #letter.sender = socket.gethostbyname(socket.gethostname()) #보내는사람 IP주소 저장
            letter.save()
            # return render(request, 'link.html', {'letter':letter})
            return render(request, 'gift.html', {'pk':letter.pk})
        else:
            return HttpResponse('알 수 없는 에러가 발생했습니다 ㅠㅠ 다시입력해주세요!')
    else:
        form = LetterForm()
        # gift = request.GET['gift']
        # return render(request, 'new.html', {'form':form, 'gift':gift})
        return render(request, 'new.html', {'form':form})

def gift(request):
    return render(request, 'gift.html')

def giftsave(request):
    if request.method == 'POST':
        gift = request.POST['gift']
        pk = request.POST['pk']
        letter = Letter.objects.get(pk=pk)
        if gift == '0':
            import random
            letter.gift = random.randint(1, 5)
        else:
            letter.gift = gift
        letter.save()
        return render(request, 'link.html', {'letter':letter})

def detail(request, letter_id):
    letter = get_object_or_404(Letter, pk=letter_id)

    # if request.method == 'GET':
    #     return render(request, 'detail.html', {'letter':letter, 'key':1})
    # else:
    #     if letter.pw == request.POST['pw']:
    #         return render(request, 'detail.html', {'letter':letter, 'key':0})
    #     else:
    #         return render(request, 'detail.html', {'letter':letter, 'key':1})
    
    return render(request, 'detail.html', {'letter':letter})