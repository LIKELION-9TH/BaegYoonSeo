from django.shortcuts import redirect, render, get_object_or_404
from django.utils import timezone
from .models import Bgyoon

def home(request):
    bgyoons = Bgyoon.objects
    return render(request, 'home.html', {'bgyoons':bgyoons})

def detail(request, id):
    details = get_object_or_404(Bgyoon, pk=id)
    return render(request, 'detail.html', {'details':details})

def new(request):
    return render(request, 'new.html')

def create(request):
    bgyoon = Bgyoon()
    bgyoon.title = request.POST['title']
    bgyoon.pub_date = timezone.datetime.now()
    bgyoon.body = request.POST['body']
    bgyoon.image = request.FILES['image']
    bgyoon.save()
    return redirect('detail', bgyoon.id)

def edit(request, id):
    edit_bgyoon = Bgyoon.objects.get(id=id)
    return render(request, 'edit.html', {'bgyoon':edit_bgyoon})

def update(request, id):
    update_bgyoon = Bgyoon.objects.get(id=id)
    update_bgyoon.title = request.POST['title']
    update_bgyoon.body = request.POST['body']
    update_bgyoon.pub_date = timezone.now()
    update_bgyoon.save()
    return redirect('detail', update_bgyoon.id)

def delete(request, id):
    delete_bgyoon = Bgyoon.objects.get(id=id)
    delete_bgyoon.delete()
    return redirect('home')

def hobby(request):
    return render(request, 'hobby.html')

def place(request):
    return render(request, 'place.html')

def music(request):
    return render(request, 'music.html')

def picture(request):
    return render(request, 'picture.html')

