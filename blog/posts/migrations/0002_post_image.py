# Generated by Django 3.1.2 on 2020-10-05 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='Pictures/None/No-img.jpg', upload_to='Pictures'),
        ),
    ]
