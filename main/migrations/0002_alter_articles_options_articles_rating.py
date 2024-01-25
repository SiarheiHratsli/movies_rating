# Generated by Django 4.2.9 on 2024-01-25 00:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='articles',
            options={'verbose_name': 'article', 'verbose_name_plural': 'articles'},
        ),
        migrations.AddField(
            model_name='articles',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='rating'),
        ),
    ]
