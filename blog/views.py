from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from blog.models import Post
from django.shortcuts import redirect
from blog.forms import CommentForm
import logging
from django.urls import reverse
# Create your views here.

logger = logging.getLogger(__name__)

def post_table(request):
    return render(
        request, "post-table.html", {"post_list_url": reverse("post-list")}
    )

def index(request):
    posts = Post.objects.filter(published_at__lte=timezone.now()).select_related("author")
    logger.debug("Got %d posts", len(posts))
    return render(request, "index.html", {"posts": posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    if request.user.is_active:
        if request.method == "POST":
            comment_form = CommentForm(request.POST)

            if comment_form.is_valid():
                comment = comment_form.save(commit=False)
                comment.content_object = post
                comment.creator = request.user
                comment.save()
                return redirect(request.path_info)
        else:
            comment_form = CommentForm()
    else:
        comment_form = None
    return render(request, "post-detail.html", {"post": post,"comment_form": comment_form })

