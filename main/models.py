from django.contrib.auth import get_user_model
from django.db import models
from django.utils import timezone

User = get_user_model()


class Tag(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    tags = models.ManyToManyField("Tag", blank=True, related_name="posts")
    category = models.ForeignKey(
        "Category", on_delete=models.CASCADE, related_name="posts"
    )
    editors_pick = models.BooleanField(default=False)
    trending_post = models.BooleanField(default=False)
    popular_post = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    def author_get(self):
        author_ = User.objects.filter(username=self.author).first()
        return author_

    def pictures(self):
        images = PostImages.objects.filter(post=self).all()
        return images

    def comments(self):
        r = Comment.objects.filter(post=self).all()
        return r


class PostImages(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="pictures")
    image = models.ImageField(upload_to="posts")

    def __str__(self):
        return f"Image for {self.post.title}"


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    reply = models.ForeignKey(
        "Reply",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
        related_name="replies",
    )

    date_comment = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"

    def author_get(self):
        author_ = User.objects.filter(username=self.author).first()
        return author_

    def replies_get(self):
        r = Reply.objects.filter(comment=self).all()
        return r


class Reply(models.Model):
    content = models.TextField()

    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, related_name="replies"
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="replies")
    date_reply = models.DateTimeField(default=timezone.now)

    def author_get(self):
        author_ = User.objects.filter(username=self.author).first()
        return author_


class InstagramPost(models.Model):
    picture = models.ImageField(upload_to="instagram_posts")

    def __str__(self):
        return f"Instagram Post {self.id}"


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name
