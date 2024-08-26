from django.conf import settings
from django.core.mail import send_mail
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .models import *


# Create your views here.


def index(request):
    tags_ = Tag.objects.all()
    categories_ = Category.objects.all()
    editors_picks = Post.objects.filter(editors_pick=True).all()
    trending_posts = Post.objects.filter(trending_post=True).all()
    popular_posts = Post.objects.filter(popular_post=True).all()
    recent_posts = Post.objects.filter().order_by("-date_posted")[:3]
    instagram_posts = InstagramPost.objects.all()

    categories_count = {}

    for category in categories_:
        c = Post.objects.filter(category__name=category.name).count()
        categories_count[category.name] = c

    context = {
        "tags": tags_,
        "categories": categories_count,
        "editors_picks": editors_picks,
        "trending_posts": trending_posts,
        "popular_posts": popular_posts,
        "recent_posts": recent_posts,
        "instagram_posts": instagram_posts,
    }
    return render(request, "index.html", context=context)


def comment(request):
    post_id = request.GET["post_id"]
    type_ = request.GET["type"]

    if request.method == "POST":
        comment_ = request.POST["comment"]

        if type_ == "default":
            post = Post.objects.get(id=post_id)
            Comment.objects.create(post=post, author=request.user, content=comment_)

        else:
            comment_id = request.GET["comment_id"]
            _comment_ = Comment.objects.get(id=comment_id)

            Reply.objects.create(
                comment=_comment_, author=request.user, content=comment_
            )

    return HttpResponseRedirect("post-details?post_id={}#form-title".format(post_id))


def search(request):
    if request.method == "POST":
        query = request.POST.get("q")

        if query:
            results = Post.objects.filter(
                title__icontains=query,
            ).all()

            if results:
                return render(
                    request, "search-result.html", {"results": results, "query": query}
                )

        return render(request, "search-not-found.html", context={"query": query})

    else:
        query = request.GET.get("q")

        if query == "None":
            results = [Post.objects.first()]
            query = results[0].title

            if results:
                return render(
                    request, "search-result.html", {"results": results, "query": query}
                )

    return render(request, "search-not-found.html", context={"query": query})


def post_details(request):
    post_id = request.GET["post_id"]

    if post_id == "None":
        post = Post.objects.first()

    else:
        post = Post.objects.filter(id=request.GET["post_id"]).first()

    return render(request, "post-details.html", context={"post": post})


def about_us(request):
    return render(request, "about-us.html")


def contact(request):
    if request.method == "POST":
        name = request.POST["name"]
        email = request.POST["email"]
        message = request.POST["message"]

        Contact.objects.create(name=name, email=email, message=message)

        send_mail(
            subject=f"New contact message from {name}",
            message=message,
            from_email=email,
            recipient_list=[settings.DEFAULT_CONTACT_EMAIL],
            fail_silently=True,
        )

    return render(request, "contact.html")


def privacy_policy(request):
    return render(request, "privacy-policy.html")


def terms_conditions(request):
    return render(request, "terms-conditions.html")


def tags(request):
    tag = request.GET.get("tag")

    if tag == "None":
        posts = [Post.objects.first()]
        tag = "Tags"

    else:
        posts = Post.objects.filter(tags__name=tag).all()

    recent_posts = Post.objects.filter().order_by("-date_posted")[:3]

    tags_ = Tag.objects.all()
    categories_ = Category.objects.all()

    categories_count = {}

    for category in categories_:
        c = Post.objects.filter(category__name=category.name).count()
        categories_count[category.name] = c

    return render(
        request,
        "tags.html",
        context={
            "posts": posts,
            "recent_posts": recent_posts,
            "tags": tags_,
            "categories": categories_count,
            "tag": tag,
        },
    )


def categories(request):
    tag = request.GET.get("tag")
    posts = Post.objects.filter(category__name=tag).all()

    recent_posts = Post.objects.filter().order_by("-date_posted")[:3]

    tags_ = Tag.objects.all()
    categories_ = Category.objects.all()

    categories_count = {}

    for category in categories_:
        c = Post.objects.filter(category__name=category.name).count()
        categories_count[category.name] = c

    return render(
        request,
        "tags.html",
        context={
            "posts": posts,
            "recent_posts": recent_posts,
            "tags": tags_,
            "categories": categories_count,
            "tag": tag,
        },
    )


def authors(request):
    users = User.objects.all()
    authors_ = {}

    for user in users:
        posts_count = Post.objects.filter(author=user).count()
        authors_[user] = posts_count

    return render(request, "authors.html", context={"authors": authors_})


def author_single(request):
    author_id = request.GET["author_id"]

    if author_id == "None":
        author = User.objects.first()

    else:
        author = User.objects.get(id=author_id)

    posts_count = Post.objects.filter(author=author).count()
    posts = Post.objects.filter(author=author).order_by("-date_posted")
    return render(
        request,
        "author-single.html",
        context={"author": author, "posts": posts, "posts_count": posts_count},
    )


def page_not_found(request):
    return render(request, "404.html")
