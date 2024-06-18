from .models import BookReview, Profile, BookInstance
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


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['photo']

class DateInput(forms.DateInput):
    input_type = "date"

class BookInstanceCreateUpdateForm(forms.ModelForm):
    class Meta:
        model = BookInstance
        fields = ['book', 'status', 'reader', 'due_back']
        widgets = {'due_back': DateInput}
