from django import forms
from .models import Comment
class CommentForm(forms.ModelForm):
    # user_name = forms.CharField(max_length=120)
    # user_email = forms.EmailField()
    # text = forms.CharField(widget=forms.Textarea, max_length=400)

    class Meta:
        model = Comment
        exclude = ["post"]
        labels = {
            "user_name": "Your Name",
            "user_email": "Your Email",
            "text": "Your Comment"
        }