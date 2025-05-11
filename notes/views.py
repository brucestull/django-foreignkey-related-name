# notes\views.py

from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Explanation, Profile, Note
from .forms import ExplanationForm, ProfileForm, NoteForm

# ------------------------------
# Explanation Views
# ------------------------------


# Expected template: explanation_list.html
class ExplanationListView(ListView):
    model = Explanation


# Expected template: explanation_detail.html
class ExplanationDetailView(DetailView):
    model = Explanation


# Expected template: explanation_form.html
class ExplanationCreateView(CreateView):
    model = Explanation
    form_class = ExplanationForm
    success_url = reverse_lazy("explanation-list")


# Expected template: explanation_form.html
class ExplanationUpdateView(UpdateView):
    model = Explanation
    form_class = ExplanationForm
    success_url = reverse_lazy("explanation-list")


# Expected template: explanation_confirm_delete.html
class ExplanationDeleteView(DeleteView):
    model = Explanation
    success_url = reverse_lazy("explanation-list")


# ------------------------------
# Profile Views
# ------------------------------


# Expected template: profile_list.html
class ProfileListView(ListView):
    model = Profile


# Expected template: profile_detail.html
class ProfileDetailView(DetailView):
    model = Profile


# Expected template: profile_form.html
class ProfileCreateView(CreateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("profile-list")


# Expected template: profile_form.html
class ProfileUpdateView(UpdateView):
    model = Profile
    form_class = ProfileForm
    success_url = reverse_lazy("profile-list")


# Expected template: profile_confirm_delete.html
class ProfileDeleteView(DeleteView):
    model = Profile
    success_url = reverse_lazy("profile-list")


# ------------------------------
# Note Views
# ------------------------------


# Expected template: note_list.html
class NoteListView(ListView):
    model = Note


# Expected template: note_detail.html
class NoteDetailView(DetailView):
    model = Note


# Expected template: note_form.html
class NoteCreateView(CreateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note-list")


# Expected template: note_form.html
class NoteUpdateView(UpdateView):
    model = Note
    form_class = NoteForm
    success_url = reverse_lazy("note-list")


# Expected template: note_confirm_delete.html
class NoteDeleteView(DeleteView):
    model = Note
    success_url = reverse_lazy("note-list")
