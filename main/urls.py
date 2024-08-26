from django.urls import path

from .views import *


urlpatterns = [
    path("", index, name="index"),
    path("404", page_not_found, name="404"),
    path("comment", comment, name="comment"),
    path("search", search, name="search"),
    path("about-us", about_us, name="about-us"),
    path("contact", contact, name="contact"),
    path("tags", tags, name="tags"),
    path("categories", categories, name="categories"),
    path("post-details", post_details, name="post-details"),
    path("authors", authors, name="authors"),
    path("author-single", author_single, name="author-single"),
    path("privacy-policy", privacy_policy, name="privacy-policy"),
    path("terms-conditions", terms_conditions, name="terms-conditions"),
]
