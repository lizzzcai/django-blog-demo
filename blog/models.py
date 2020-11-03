from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    """
    data model to the category

    django request model to inher from models.Model class
    Category have a simple field name
    CharField indicate the data type of the name.
    CharField also identify the max length
    more data types:
    https://docs.djangoproject.com/en/2.2/ref/models/fields/#field-types
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    data model for the tag

    tag to tag the blog, similar to the category.
    """
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Post(models.Model):
    """
    data model for the post
    """
    # title of the post
    title = models.CharField(max_length=80)

    # content of the post
    # TextField is used to store content text
    body = models.TextField()

    # record the created time and modified time of the post
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # excerpt of the post, allow blank.
    excerpt = models.CharField(max_length=200, blank=True)

    # define the category and tags
    # we define that:
    # one post can have only one category, but one category can have multiple posts.
    # on_delete = models.CASCADE means once the category being deleted, all the post belong to it will be deleted.
    # for the tag, one post can have multiple tags and one tags can have multiple posts also. So we use ManyToManyField.
    # As the post can have no tag assigned also, so we set the blank is true.
    # please refer to https://docs.djangoproject.com/en/2.2/topics/db/models/#relationships for details.
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag, blank=True)

    # auther of the post. Here the User is came from django.contrib.auth.models.
    # django.contrib.auth is built-in application for django, which is used to handle user registration, login, etc.
    # here we use ForeignKey to link the post and user, because we rassume one post have one auther only,
    # but one auther may has multiple posts.
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
