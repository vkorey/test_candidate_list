# Generated by Django 4.0.4 on 2022-05-19 19:14

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lk', '0003_rename_candidates_candidate_name'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='candidate',
            unique_together={('name', 'skills')},
        ),
    ]
