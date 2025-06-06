# Generated by Django 5.2.1 on 2025-05-11 23:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='note',
            name='user',
        ),
        migrations.AddField(
            model_name='note',
            name='profile',
            field=models.ForeignKey(default=None, help_text='The profile this note belongs to.', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='notes', to='notes.profile'),
        ),
    ]
