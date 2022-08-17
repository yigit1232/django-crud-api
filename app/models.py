from django.db import models
from autoslug import AutoSlugField

def custom_slug(value):
    value = value.replace('ı', 'i')
    value = value.replace(' ', '-')
    return value


class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(slugify=custom_slug,unique=True,populate_from='title',null=True,blank=True)

    class Meta:
        db_table='posts'
        verbose_name='Post'
        verbose_name_plural='Posts'

    def __str__(self):
        return self.title

    def get_detail_url(self):
        return f"http://127.0.0.1:8000/api/post/detail/{self.slug}/"