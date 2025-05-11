from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Explanation(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.name


class Profile(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="profiles",
        help_text="The user this profile belongs to.",
    )
    nickname = models.CharField(max_length=100)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Profile: {self.nickname} (of {self.user.username})"


class Note(models.Model):
    profile = models.ForeignKey(
        Profile,
        on_delete=models.CASCADE,
        related_name="notes",
        help_text="The profile this note belongs to.",
        default=None,
        null=True,
    )
    title = models.CharField(max_length=255)
    content = models.TextField()

    def __str__(self):
        return f"{self.title} (by {self.profile.nickname})"
