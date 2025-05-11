from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from notes.models import Profile, Note
import random

User = get_user_model()


class Command(BaseCommand):
    help = "Create sample users, profiles, and notes."

    def handle(self, *args, **kwargs):
        # Clear old data
        Note.objects.all().delete()
        Profile.objects.all().delete()
        User.objects.filter(username__startswith="sampleuser").delete()

        for i in range(1, 3):
            user = User.objects.create_user(
                username=f"sampleuser{i}",
                email=f"user{i}@example.com",
                password="testpassword",
            )
            self.stdout.write(self.style.SUCCESS(f"Created User: {user.username}"))

            for j in range(1, 3):
                profile = Profile.objects.create(
                    user=user,
                    nickname=f"{user.username}_profile{j}",
                    bio=f"Bio of {user.username} profile {j}",
                )
                self.stdout.write(
                    self.style.SUCCESS(f"  Created Profile: {profile.nickname}")
                )

                num_notes = random.randint(3, 6)
                for k in range(1, num_notes + 1):
                    note = Note.objects.create(
                        profile=profile,
                        title=f"{profile.nickname} Note {k}",
                        content=f"This is note {k} for {profile.nickname}.",
                    )
                self.stdout.write(
                    self.style.SUCCESS(
                        f"    Created {num_notes} notes for {profile.nickname}"
                    )
                )

        self.stdout.write(self.style.SUCCESS("Sample data creation complete."))
