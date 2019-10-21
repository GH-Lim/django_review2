from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_POST, require_GET
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .models import Article, Comment
from .forms import ArticleForm, CommentForm


@require_GET
def index(request):
    articles = Article.objects.all()
    return render(request, 'articles/index.html', {'articles': articles})


@require_GET
def detail(request, article_pk):
    # 사용자가 url 에 적어보낸 article_pk 를 통해 디테일 페이지를 보여준다.
    # Article.objects.get(pk=article_pk)
    article = get_object_or_404(Article, pk=article_pk)
    comments = article.comments.all()
    form = CommentForm()
    context = {
        'article': article,
        'comments': comments,
        'form': form,
    }
    return render(request, 'articles/detail.html', context)


@login_required
def create(request):
    form = ArticleForm(request.POST or None)
    if form.is_valid():
        article = form.save()
        # article.save()
        article_pk = article.pk
        return redirect('articles:detail', article_pk)
    # else:  # GET
    #     # Article 을 생성하기 위한 페이지를 달라고 하는 요청
    #     form = ArticleForm()
    context = {'form': form}
    return render(request, 'articles/create.html', context)


@login_required
def update(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    form = ArticleForm(request.POST or None, instance=article)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article_pk)
    context = {'form': form}
    return render(request, 'articles/update.html', context)


@require_POST
def delete(request, article_pk):
    if request.user.is_authenticated:
        article = get_object_or_404(Article, pk=article_pk)
        article.delete()
    return redirect('articles:index')


@require_POST
def create_comment(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    if request.user.is_authenticated:
        form = CommentForm(request.POST or None)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.article = article
            comment.save()
    return redirect('articles:detail', article_pk)
    # context = {
    #     'article': article,
    #     'form': form,
    # }
    # return render(request, 'articles/detail.html', context)


@require_POST
def delete_comment(request, article_pk, comment_pk):
    if request.user.is_authenticated:
        comment = get_object_or_404(Comment, pk=comment_pk)
        comment.delete()
        return redirect('articles:detail', article_pk)
    return HttpResponse('Your are Unauthorized', status=401)  # 401 -> 인증되지 않았다
