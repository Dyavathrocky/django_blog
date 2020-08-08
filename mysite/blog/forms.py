from django import forms

from .models import Comment

class EmailPostForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'email' ,'body')

        
    """name = forms.CharField(max_length=250)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False , widget=forms.Textarea)"""