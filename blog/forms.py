from django import forms

from .models import Blog


class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)


class AddBlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "banner",
            "description"
        )
