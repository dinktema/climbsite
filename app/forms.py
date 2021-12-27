from django import forms
from django.core.exceptions import ValidationError
import re
from .models import Post, Climber
from django.contrib.auth.forms import UserCreationForm


class AddPost(forms.Form):
    title = forms.CharField(max_length=50, label='Title')
    subtitle = forms.CharField(max_length=200, label='Subtitle')
    content = forms.CharField(widget=forms.Textarea, max_length=5000, label='content')
    image = forms.ImageField(label='Post image')
    post_type = forms.ChoiceField(choices=Post.POST_TYPES, label="Post type")
    location = forms.CharField(max_length=100, label='Location')

    def clean_subtitle(self):
        t = self.cleaned_data['title']
        s = self.cleaned_data['subtitle']

        if t == s:
            raise ValidationError("Title and subtitle should differ")

        return s


class AddClimber(UserCreationForm):
    name = forms.CharField(max_length=20, label='Name', widget=forms.TextInput(attrs={"class": "form-control"}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label='Approwe the password', widget=forms.PasswordInput(attrs={"class": "form-control"}))
    email = forms.EmailField(max_length=30, label='Email', widget=forms.TextInput(attrs={"class": "form-control"}))
    image = forms.ImageField(label='Userpick')

    def clean_name(self):
        n = self.cleaned_data['name']

        flag = Climber.objects.get(name=n)
        if flag:
            raise ValidationError("User with this name does exist")

    def clean_password(self):
        password = self.cleaned_data['password']
        password2 = self.cleaned_data['password2']

        while True:
            if (len(password) < 8):
                flag = False
                break
            elif not re.search("[a-z]", password):
                flag = False
                break
            elif not re.search("[A-Z]", password):
                flag = False
                break
            elif not re.search("[0-9]", password):
                flag = False
                break
            elif not re.search("[_@$]", password):
                flag = False
                break
            elif re.search("\s", password):
                flag = False
                break
            else:
                flag = True
                break

        if not flag or password != password2:
            raise ValidationError("Not a Valid Password")
        else:
            return password
