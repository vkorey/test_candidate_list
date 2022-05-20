from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(
        'tag',
        max_length=200,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('name',)


class Skill(models.Model):
    candidates = models.ManyToManyField(
        User,
        related_name='skills',
    )
    tag = models.ForeignKey(
        Tag,
        on_delete=models.CASCADE,
        related_name="skills",
        null=True,
    )
    name = models.CharField(
        'название навыка',
        max_length=200,
        null=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ('tag', 'name',)
