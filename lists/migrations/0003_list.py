# Generated by Django 5.0.7 on 2024-08-21 23:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lists', '0002_alter_item_text'),
    ]

    operations = [
        migrations.CreateModel(
            name='List',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('list', models.TextField(default='')),
            ],
        ),
    ]
