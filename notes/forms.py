# notes\forms.py

from django import forms
from .models import Explanation, Profile, Note


class ExplanationForm(forms.ModelForm):
    class Meta:
        model = Explanation
        fields = ["name", "description"]


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["user", "nickname", "bio"]


class NoteForm(forms.ModelForm):
    class Meta:
        model = Note
        fields = ["profile", "title", "content"]
