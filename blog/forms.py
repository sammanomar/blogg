from django import forms

from .models import Blog

from django_summernote.fields import SummernoteTextFormField, SummernoteTextField

class TextForm(forms.Form):
    text = forms.CharField(widget=forms.Textarea, required=True)


class AddBlogForm(forms.ModelForm):
    description = SummernoteTextField
    
    class Meta:
        model = Blog
        fields = (
            "title",
            "category",
            "banner",
            "description",
        )
