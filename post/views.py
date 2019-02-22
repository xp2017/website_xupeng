from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Post, Comment
from .forms import PostForm, CommentForm


def post_create(request):
    new_post = None
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        if post_form.is_valid():
            new_post = post_form.save(commit=False)
            new_post.save()
    else:
        post_form = PostForm()

    return render(request, 'post/question/create.html', {
                                                         'post_form': post_form,
                                                        'new_post': new_post})


def post_list(request):
    object_list = Post.published.all()

    paginator = Paginator(object_list, 15)
    page = request.GET.get('page')

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)

    return render(request, 'post/question/list.html', {'page': page, 'post': posts})


def post_detail(request, year, month, day, post):
    post = get_object_or_404(Post, slug=post, status='发布',
                             publish__year=year,
                             publish__month=month,
                             publish__day=day)

    comments = post.comments.filter(active=True)
    new_comment = None

    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            new_comment = comment_form.save(commit=False)
            new_comment.post = post
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, 'post/question/detail.html', {'post': post,
                                                         'comments': comments,
                                                         'new_comment': new_comment,
                                                         'comment_form': comment_form})