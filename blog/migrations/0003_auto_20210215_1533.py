# Generated by Django 3.1.4 on 2021-02-15 20:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_post_cover_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='cover_image',
            field=models.ImageField(upload_to='blog_covers'),
        ),
    ]
