# Generated by Django 5.0b1 on 2024-03-20 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advancedBlog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tag',
            field=models.CharField(default='blog post', max_length=150),
        ),
    ]
