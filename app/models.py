from django.db import models
from django.contrib.auth import get_user_model


USER = get_user_model()


class BaseModel(models.Model):

    """
    BaseModel for inheriting.
    """

    id = models.BigAutoField(
        primary_key=True,
        unique=True,
        verbose_name='Id'
    )

    created_from = models.ForeignKey(
        USER,
        null=False,
        blank=False,
        on_delete=models.CASCADE,
        verbose_name='Erstellt von'
    )

    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Erstellt am'
    )

    class Meta:
        abstract = True


class Status(models.TextChoices):
    UNPUBLISHED = 'UN', 'Unpublished'
    PUBLISHED = 'PU', 'Published'


class Post(BaseModel):

    """
    Model of a simple post for the website.
    """

    title = models.CharField(
        max_length=250,
        null=False,
        blank=False,
        unique=True,
        verbose_name='Titel'
    )

    status = models.CharField(
        max_length=2,
        null=False,
        blank=False,
        choices=Status.choices,
        default=Status.UNPUBLISHED,
        verbose_name='Status'
    )

    class Meta:
        app_label = 'app'
        indexes = [
            models.Index(
                fields=['title', 'status'],
                name='index-posts'
            ),
        ]
        ordering = ['-id']
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
    
    def __str__(self) -> str:
        return self.title[:50]

    def get_absolute_url(self):
        return f'posts/{self.id}/'
    
    def delete(self, *args, **kwargs):
        print(f'The post with the title {self.title} has been deleted!')
        super(Post, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        print(f'The post with the title {self.title} has been saved!')
        super(Post, self).save(*args, **kwargs)





