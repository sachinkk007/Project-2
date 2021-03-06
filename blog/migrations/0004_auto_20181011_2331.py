# Generated by Django 2.0.5 on 2018-10-11 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_post_tags'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='img',
            field=models.ImageField(blank=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='post',
            name='profile',
            field=models.FileField(blank=True, upload_to='files'),
        ),
    ]
