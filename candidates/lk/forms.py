from django import forms

from lk.fields import ListTextWidget
from lk.models import Skill, Tag


class FormForm(forms.Form):
    tag = forms.CharField(label='Тэги', required=True)
    skill = forms.CharField(label='Навыки', required=True)

    def __init__(self, *args, **kwargs):
        super(FormForm, self).__init__(*args, **kwargs)

        self.fields['tag'].widget = ListTextWidget(
            data_list=Tag.objects.all(),
            name='tag_list'
        )
        self.fields['skill'].widget = ListTextWidget(
            data_list=Skill.objects.all(),
            name='skill_list'
        )
