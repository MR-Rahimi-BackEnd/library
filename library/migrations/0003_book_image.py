# Generated by Django 5.1.4 on 2024-12-18 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_userprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='book_image/'),
        ),
    ]