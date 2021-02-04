from django.forms import ModelForm, Textarea, Select, CheckboxSelectMultiple
from .models import Post


class PostForm(ModelForm):
    class Meta:
        model = Post

        fields = ['headline', 'text', 'article_default_news',  'categories']
        widgets = {
            'text': Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите текст...'
            }),

            'article_default_news': Select(attrs={
                'class': 'custom-select',
                'option selected': 'Выбрать...'
            }),
            'categories': CheckboxSelectMultiple(attrs={
                'multiple class': 'form-control',
                'class': 'special',
                'size': '100',
            }),
        }