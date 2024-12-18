from django import forms
from .models import Book,UserProfile
from django.contrib.auth.models import User

class NewForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('name','title','user_age','author','image')
        
    def __init__(self,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['image'].required  = False


class SingupForm(forms.ModelForm):
    password = forms.CharField()
    age = forms.IntegerField()
    email = forms.CharField(max_length=100)
    class Meta:
        model = User
        fields = ['username', 'password', 'email']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password"])
        if commit:
            user.save()
            UserProfile.objects.create(user=user, age=self.cleaned_data['age'])
        return user
        