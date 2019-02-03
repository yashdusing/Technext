from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField
from multiselectfield import MultiSelectField
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
import datetime
from mptt.models import MPTTModel, TreeForeignKey

class Post(models.Model):
    title = models.CharField(max_length=500)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    writer = models.CharField(max_length=60)
    likes = models.ManyToManyField(User, related_name='likes')
    dislikes = models.ManyToManyField(User, related_name='dislikes')
    is_real = models.BooleanField(default=False)

    @property
    def total_likes(self):
        """
        Likes for the company
        :return: Integer: Likes for the company
        """

        return (self.likes.count()-self.dislikes.count())

    def __str__(self):
        return str(self.title)

    def get_absolute_url(self):
        return reverse('curr2', kwargs={'pk': self.pk})
