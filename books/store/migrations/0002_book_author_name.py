# Generated by Django 3.2.8 on 2021-10-16 12:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='author_name',
            field=models.CharField(default='author', max_length=255),
            preserve_default=False,
        ),
    ]
