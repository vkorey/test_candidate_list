# Generated by Django 4.0.4 on 2022-05-20 19:06

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('lk', '0010_tag_rename_candidate_skill_candidates_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='skill',
            old_name='skill',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='tag',
            old_name='tag',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='skill',
            name='candidates',
            field=models.ManyToManyField(related_name='skills', to=settings.AUTH_USER_MODEL),
        ),
    ]
