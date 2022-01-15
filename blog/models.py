from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MinLengthValidator

content_validator = MinLengthValidator(
    limit_value=30, message='Content should be at least 300 characters long!')
# Create your models here.


class Blog(models.Model):
    title = models.CharField(max_length=250)
    content = models.TextField(validators=[content_validator])
    date_published = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_detail', kwargs={'pk': self.pk})
