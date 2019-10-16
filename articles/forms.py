from django import forms
from .models import Article


class ArticleForm(forms.ModelForm):
    
    class Meta:
        model = Article
        fields = '__all__' # 모든 필드를 보겠다