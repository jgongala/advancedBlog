# Generated by Django 5.0.2 on 2024-03-24 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advancedBlog', '0012_remove_post_postfragment'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='images/'),
        ),
    ]
