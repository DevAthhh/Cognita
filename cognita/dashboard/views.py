from lib2to3.fixes.fix_input import context

from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import CreateView

from .models import Entries


@login_required
def index(request):
    notes = Entries.objects.filter(author=request.user)
    return render(request, 'dashboard/index.html', context={'notes': notes})

@login_required
def note(request, note_id):
    notet = Entries.objects.filter(pk=note_id)
    print(notet)
    notes = Entries.objects.filter(author=request.user)
    return render(request, 'dashboard/index.html', context={'note': notet[0], 'notes': notes})

@login_required
def create(request):
    if request.method == 'POST':
        Entries.objects.create(name=request.POST.get('name'), author=request.user, is_published=True)
    return redirect('dashboard', permanent=True)