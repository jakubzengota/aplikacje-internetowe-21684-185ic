# Generated by Django 3.1.2 on 2020-11-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(blank=True, to='blog.Category'),
        ),
    ]
