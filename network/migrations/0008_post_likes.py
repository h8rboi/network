# Generated by Django 3.1.3 on 2022-01-26 04:28

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('network', '0007_auto_20220121_2235'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='Likes',
            field=models.ManyToManyField(null=True, related_name='liker', to=settings.AUTH_USER_MODEL),
        ),
    ]
