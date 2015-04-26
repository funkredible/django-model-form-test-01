from django import forms
from .models import Comment


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'article']

        # CharFieldはデフォルトでtype=textなのでtextareaへ変更する。
        # Specifying widgets to use in the form with widgets https://docs.djangoproject.com/en/1.7/topics/forms/modelforms/#overriding-the-default-field-types-or-widgets

        # http://stackoverflow.com/questions/15795869/django-modelform-to-have-a-hidden-input
        # http://stackoverflow.com/questions/12097825/specifying-widget-for-model-form-extra-field-django
        # http://nanvel.name/weblog/three-ways-change-widget-django-modelform/
        widgets = {
            'text': forms.Textarea(),
            'article': forms.HiddenInput(),  # 外部キーをhiddenでhtml上にだす。
        }
