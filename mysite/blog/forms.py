from django import forms
from .models import Post, Comment,Contact


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)
        
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'title': forms.TextInput(attrs={'class': 'textinputclass'}),
            # 'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
        }


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

        widgets = {
            'author': forms.TextInput(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'}),
            # 'author': forms.TextInput(attrs={'class': 'textinputclass'}),
            # 'text': forms.Textarea(attrs={'class': 'editable medium-editor-textarea'}),
        }

class ContactForm(forms.ModelForm):
    class Meta :
        model = Contact
        fields = '__all__'
        widgets={
            "email": forms.EmailInput(attrs={'class':'form-control'}),
            "password": forms.PasswordInput( render_value =True, attrs={'class':'form-control'})
        }