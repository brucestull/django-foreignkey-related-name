# notes\urls.py

from django.urls import path
from . import views

urlpatterns = [
    # ------------------------------
    # Explanation URLs
    # ------------------------------
    path("explanations/", views.ExplanationListView.as_view(), name="explanation-list"),
    path(
        "explanations/<int:pk>/",
        views.ExplanationDetailView.as_view(),
        name="explanation-detail",
    ),
    path(
        "explanations/create/",
        views.ExplanationCreateView.as_view(),
        name="explanation-create",
    ),
    path(
        "explanations/<int:pk>/update/",
        views.ExplanationUpdateView.as_view(),
        name="explanation-update",
    ),
    path(
        "explanations/<int:pk>/delete/",
        views.ExplanationDeleteView.as_view(),
        name="explanation-delete",
    ),
    # ------------------------------
    # Profile URLs
    # ------------------------------
    path("profiles/", views.ProfileListView.as_view(), name="profile-list"),
    path(
        "profiles/<int:pk>/", views.ProfileDetailView.as_view(), name="profile-detail"
    ),
    path("profiles/create/", views.ProfileCreateView.as_view(), name="profile-create"),
    path(
        "profiles/<int:pk>/update/",
        views.ProfileUpdateView.as_view(),
        name="profile-update",
    ),
    path(
        "profiles/<int:pk>/delete/",
        views.ProfileDeleteView.as_view(),
        name="profile-delete",
    ),
    # ------------------------------
    # Note URLs
    # ------------------------------
    path("notes/", views.NoteListView.as_view(), name="note-list"),
    path("notes/<int:pk>/", views.NoteDetailView.as_view(), name="note-detail"),
    path("notes/create/", views.NoteCreateView.as_view(), name="note-create"),
    path("notes/<int:pk>/update/", views.NoteUpdateView.as_view(), name="note-update"),
    path("notes/<int:pk>/delete/", views.NoteDeleteView.as_view(), name="note-delete"),
]
