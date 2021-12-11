from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils import timezone
from .models import Note

# Create your views here.
@login_required(login_url='User:login_user')
def index(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user, 'notes': Note.objects.all().filter(user_id=user.id)}
    return render(request, 'crud/index.html', context)

@login_required(login_url='User:login_user')
def noteview(request, note_id, username):
    note = get_object_or_404(Note, pk=note_id)
    user = get_object_or_404(User, username=username)
    context = {'user': user, 'note': note}
    print(timezone.now().date())
    return render(request, 'crud/note.html', context)

@login_required(login_url='User:login_user')
def add(request, username):
    user = get_object_or_404(User, username=username)
    context = {'user': user}
    return render(request, 'crud/add.html', context)

@login_required(login_url='User:login_user')
def addnote(request, username):
    user = get_object_or_404(User, username=username)
    new_note = Note.objects.create()
    new_note.title = request.POST['title']
    new_note.body = request.POST['body']
    new_note.date = request.POST['date']
    new_note.user_id = user.id
    new_note.save()
    return redirect('User:crud:index', username=user.username)

@login_required(login_url='User:login_user')
def edit(request, note_id, username):
    note = get_object_or_404(Note, pk=note_id)
    user = get_object_or_404(User, username=username)
    if request.method == "POST":
        note.title = request.POST['title']
        note.body = request.POST['body']
        note.date = request.POST['date']
        note.save()
        return redirect('User:crud:noteview', note_id=note.id, username=user.username)
    context = {'user': user, 'note': note}
    return render(request, 'crud/edit.html', context)