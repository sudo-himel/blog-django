# Generated by Django 3.1.4 on 2021-07-22 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20210319_0211'),
    ]

    operations = [
        migrations.CreateModel(
            name='Site',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('logo', models.ImageField(upload_to='Logo')),
                ('icon', models.ImageField(upload_to='Logo')),
                ('view', models.IntegerField(default=0)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='view',
            field=models.IntegerField(default=0),
        ),
    ]
