
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.views.generic import ListView

from .models import Entries


class Index(LoginRequiredMixin, ListView):
    """
    This is the main page,
    without an open note...

    TAGGING: this class can be removed
    """

    template_name: str = 'dashboard/index.html'
    extra_context: dict = {'title': 'MainPage'}
    context_object_name: str = 'notes'

    def get_queryset(self):
        return Entries.objects.filter(author=self.request.user)


class Note(ListView):
    """
    This is the main page
    with an open note that
    you can edit or just view...
    """

    template_name: str = 'dashboard/index.html'
    note_id: int = 0

    def get_queryset(self):
        self.note_id = self.kwargs['note_id']

    def get_context_data(self, **kwargs):
        current_note = Entries.objects.get(pk=self.note_id)
        context = super().get_context_data(**kwargs)
        context['title'] = current_note.name
        context['note'] = current_note
        context['notes'] = Entries.objects.filter(author=self.request.user)

        return context


# ----- everything below is a representation function -----

@login_required
def create(request):
    """
    This function creates
    an entry in the table
    so that it is displayed
    on the main page...

    :param request:
    :return:
    """

    if request.method == 'POST':
        Entries.objects.create(name=request.POST.get('name'), author=request.user, is_published=True)
    return redirect('dashboard', permanent=True)


def update(request, note_id):
    """
    This function is called
    when saving changes to an
    object, and is needed in
    order to make changes
    to the database...

    :param request:
    :param note_id:
    :return:
    """

    note: dict = Entries.objects.get(pk=note_id)
    note.content = request.POST.get('content')
    note.save()
    return redirect('note', note_id)
