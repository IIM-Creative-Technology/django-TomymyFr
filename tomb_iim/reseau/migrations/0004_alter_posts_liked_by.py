# Generated by Django 4.0.3 on 2022-03-04 10:13

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('reseau', '0003_posts_liked_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='posts',
            name='liked_by',
            field=models.ManyToManyField(related_name='liked_by', to=settings.AUTH_USER_MODEL),
        ),
    ]
