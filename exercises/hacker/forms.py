from django import forms
from .models import Post
from django.forms import Textarea

class CreatePost(forms.ModelForm):
    class Meta:
        model = Post
        fields = [
        	"title",
            "content",
        ]

        widgets = {
        	# "title":
            "content":Textarea(),
        }
