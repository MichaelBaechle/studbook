# -*- coding: utf-8 -*-
from django import forms

class StudForm(forms.Form):
    new_dog_name = forms.CharField()
    new_dog_pic = forms.ImageField()
    new_owner_name = forms.CharField()