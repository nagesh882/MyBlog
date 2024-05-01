# Generated by Django 5.0.3 on 2024-05-01 14:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('blog_id', models.BigAutoField(primary_key=True, serialize=False, unique=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
    ]