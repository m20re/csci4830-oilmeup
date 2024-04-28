from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    budget = forms.DecimalField(max_digits=10, decimal_places=2)

    class Meta(UserCreationForm.Meta):
        model = User
        fields = UserCreationForm.Meta.fields + ('budget',)

    # raises validation error if the username already exists within database
    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exists():
            raise ValidationError("This username is already taken. ")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
            user_profile = UserProfile(user=user, budget=self.cleaned_data['budget'])
            user_profile.save()
        return user