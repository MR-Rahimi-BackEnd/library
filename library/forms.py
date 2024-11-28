from django import forms
from .models import Book
from django.contrib.auth.models import User

class NewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','title','user_age','author')


class SingupForm(forms.ModelForm):
    password = forms.CharField()
    age = forms.IntegerField()
    class Meta:
        model = User
        fields = ['username', 'password', 'age']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
        return user
        