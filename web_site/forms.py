from .models import Comments, Category, Post
from django import forms


class AddCommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['body']
        widgets = {
            'body': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Оставьте свой комментарий'
            })
        }


class AddPostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'photo', 'category', 'author')

        widget = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'author': forms.TextInput(attrs={'class': 'form-control',
                                             'value': '',
                                             'id': 'author',
                                             'type': 'hidden'})
        }
