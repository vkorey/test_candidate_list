from django import forms

from lk.fields import ListTextWidget
from lk.models import Skill, Tag


class FormForm(forms.Form):
    tags = forms.CharField(label='Тэги', required=True)
    skills = forms.CharField(label='Навыки', required=True)

    def __init__(self, *args, **kwargs):
        skill_list = kwargs.pop('data_list', None)
        super(FormForm, self).__init__(*args, **kwargs)
        
        self.fields['tags'].widget = ListTextWidget(data_list=Tag.objects.all(), name='tag_list')
        self.fields['skills'].widget = ListTextWidget(data_list=Skill.objects.all(), name='skill_list')

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
