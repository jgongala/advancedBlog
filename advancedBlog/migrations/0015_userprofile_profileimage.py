# Generated by Django 5.0.2 on 2024-03-24 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advancedBlog', '0014_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='profileImage',
            field=models.ImageField(blank=True, null=True, upload_to='images/profileImage'),
        ),
    ]
