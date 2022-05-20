from django import forms

from lk.models import Skill, Tag


class SkillForm(forms.ModelForm):
    class Meta:
        model = Skill
        fields = ('tag', 'name')


class NewSkillForm(forms.Form):
    tag = forms.ModelChoiceField(
        label="Existing tag",
        queryset=Tag.objects
    )
    new_tag = forms.CharField(
        label="New Tag name",
    )
    skill = forms.ModelChoiceField(
        label="Existing skill",
        queryset=Skill.objects
    )
    new_skill = forms.CharField(
        label="New Skill name",
    )
