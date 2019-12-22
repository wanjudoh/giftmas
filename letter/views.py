from django.shortcuts import render, redirect, get_object_or_404
from .forms import LetterForm
from .models import Letter
from django.http import HttpResponse
import socket

# Create your views here.

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
            letter.sender = socket.gethostbyname(socket.gethostname()) #보내는사람 IP주소 저장
            design = request.POST['design']
            gift = request.POST['gift']
            letter.design = design
            letter.gift = gift
            letter.save()
            return render(request, 'link.html', {'pk':letter.id, 'gift':letter.gift})
        else:
            return HttpResponse('폼이 유효하지 않다는데요..? 다시입력해보세요 ㅎ')
    else:
        gift = request.GET.get('gift')
        form = LetterForm()
        return render(request, 'new.html', {'form':form, 'gift':gift})

def gift(request):
    return render(request, 'gift.html')

def detail(request, letter_id):
    letter = get_object_or_404(Letter, pk=letter_id)
    if letter.sender == socket.gethostbyname(socket.gethostname()): # 내가 보낸사람
        return render(request, 'detail.html', {'letter':letter})
    elif letter.receiver == None: # 최초확인
        letter.receiver = socket.gethostbyname(socket.gethostname()) # 받는사람 저장
        letter.save()
        return render(request, 'detail.html', {'letter':letter})
    elif letter.receiver == socket.gethostbyname(socket.gethostname()): # 내가 받는사람
        return render(request, 'detail.html', {'letter':letter})
    else: # 보낸 사람도 받는 사람도 아님
        return render(request, 'detail.html', {'error':'읽을 권한이 없습니다.'})