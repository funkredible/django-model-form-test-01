from django.shortcuts import render
from .models import Article, Comment
from .forms import CommentForm
from django.http import HttpResponseRedirect

# 参考
# https://docs.djangoproject.com/en/1.8/topics/forms/å


def article(request, id):
    article = Article.objects.get(pk=id)
    comment_list = Comment.objects.filter(article__pk=id).order_by('-pk')

    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        comment_form = CommentForm(request.POST)
        # check whether it's valid:
        if comment_form.is_valid():
            # process the data in form.cleaned_data as required
            # redirect to a new URL:
            comment_form.save()
            return HttpResponseRedirect('/article/' + id + '/')
    elif request.method == 'GET':
        comment_form = CommentForm(initial={'article': id})

    context = {
        'article': article,
        'comment_form': comment_form,
        'comment_list': comment_list,
    }

    return render(request, 'article-detail.html', context)
