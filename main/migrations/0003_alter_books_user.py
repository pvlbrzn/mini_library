# Generated by Django 4.2.17 on 2024-12-24 22:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_alter_books_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='books',
            name='user',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Почта пользователя'),
        ),
    ]
