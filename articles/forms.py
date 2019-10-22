from django import forms
from .models import Article
from .models import Comment


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = ['title', 'content']
        # '__all__' # 모든 필드를 보겠다


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['content']
