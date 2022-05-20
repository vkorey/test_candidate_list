# Generated by Django 4.0.4 on 2022-05-20 18:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0009_alter_skill_candidate_alter_skill_skill_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tag', models.CharField(max_length=200, null=True, verbose_name='tag')),
            ],
        ),
        migrations.RenameField(
            model_name='skill',
            old_name='candidate',
            new_name='candidates',
        ),
        migrations.AlterField(
            model_name='skill',
            name='tag',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='skills', to='lk.tag'),
        ),
    ]
