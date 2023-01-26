
from django.db import models
from django.core.urlresolvers import reverse
from django.utils.text import slugify
from datetime import date

from content.models import TimeStamped, ViewCounterMixin


class Blog(models.Model):
    name = models.CharField(
        max_length=80,
        verbose_name="Navn"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
        editable=True,
    )

    created = models.DateField(
        editable=False,
        verbose_name="Opprettet"
    )

    class Meta:
        verbose_name = "Blogg"
        verbose_name_plural = "Blogger"
        db_table = "content_blog"

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = date.today()
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('blog', kwargs={'blog': self.slug})


class BlogPost(TimeStamped, ViewCounterMixin, models.Model):
    blog = models.ForeignKey(
        Blog,
        related_name="posts",
        verbose_name="Blogg"
    )

    title = models.CharField(
        max_length=80,
        verbose_name="Tittel"
    )

    slug = models.SlugField(
        unique=True,
        blank=True,
        editable=True,
    )

    content = models.TextField(
        verbose_name="Innhold",
        help_text="Her kan du skrive i Markdown"
    )

    list_image = models.ImageField(
        upload_to="blogpics",
        verbose_name="Listebilde",
        help_text="Bilde som vises i listevisningen av bloggene",
        blank=True,
        null=True
    )

    class Meta:
        verbose_name = "Post"
        verbose_name_plural = "Poster"
        db_table = "content_blogpost"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('blog_post', kwargs={'blog': self.blog.slug, 'slug': self.slug})
