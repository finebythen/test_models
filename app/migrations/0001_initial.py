# Generated by Django 3.1.14 on 2022-07-07 11:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False, unique=True, verbose_name='Id')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Erstellt am')),
                ('title', models.CharField(max_length=250, unique=True, verbose_name='Titel')),
                ('status', models.CharField(choices=[('UN', 'Unpublished'), ('PU', 'Published')], default='UN', max_length=2, verbose_name='Status')),
                ('created_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Erstellt von')),
            ],
            options={
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
                'ordering': ['-id'],
            },
        ),
        migrations.AddIndex(
            model_name='post',
            index=models.Index(fields=['title', 'status'], name='index-posts'),
        ),
    ]
