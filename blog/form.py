from django import forms

from .models import Comment, Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ("name", "email", "sub", "message")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["content"]
