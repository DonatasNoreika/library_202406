from .models import BookReview
from django.contrib.auth.models import User
from django import forms


class BookReviewForm(forms.ModelForm):
    class Meta:
        model = BookReview
        fields = ['content']


class UserUpdateForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']
