from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
import uuid

from django.db.models.deletion import CASCADE
from users.models import Profile

class Posts(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    meta_title = models.CharField(max_length=200, unique=True)
    meta_description = models.CharField(max_length=300, unique=True)
    body = RichTextUploadingField(config_name='default')
    featured_image = models.ImageField(upload_to='media/featured_images', null=True, blank=True)
    og_image = models.ImageField(upload_to='og_images', blank=True, null=True)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag', blank=True)
    category = models.ManyToManyField('Category', blank=True)
    created = models.DateField(auto_now_add=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    updated_at = models.DateField(auto_now=True)

    search_engine_visibility = models.BooleanField(
        default=False, 
        verbose_name="Search engine visibility",
        help_text="Discourage search engines from indexing this post",
        )#Discourage search engines from indexing this site


    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name = " Post"
        verbose_name_plural = " Posts"


    def __str__(self):
        return self.title

class Pages(models.Model):
    title = models.CharField(max_length=300, unique=True)
    slug = models.SlugField(max_length=300, unique=True)
    meta_title = models.CharField(max_length=200, unique=True)
    meta_description = models.CharField(max_length=300, unique=True)
    body = RichTextUploadingField(config_name='default')
    featured_image = models.ImageField(upload_to='media/featured_images', null=True, blank=True)
    og_image = models.ImageField(upload_to='og_images', blank=True, null=True)
    owner = models.ForeignKey(
        Profile, null=True, blank=True, on_delete=models.CASCADE)
    #tags = models.ManyToManyField('Tag', blank=True)
    created = models.DateField(auto_now_add=True)
    vote_total = models.IntegerField(default=0, null=True, blank=True)
    vote_ratio = models.IntegerField(default=0, null=True, blank=True)
    updated_at = models.DateField(auto_now=True)

    search_engine_visibility = models.BooleanField(
        default=False, 
        verbose_name="Search engine visibility",
        help_text="Discourage search engines from indexing this page",
        )#Discourage search engines from indexing this site

    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name = " Page"
        verbose_name_plural = " Pages"


    def __str__(self):
        return self.title

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name = " Tag"
        verbose_name_plural = " Tags"

    def __str__(self):
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default=uuid.uuid4, unique=True,
                          primary_key=True, editable=False)

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.name
