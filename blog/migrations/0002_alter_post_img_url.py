# Generated by Django 5.1.1 on 2024-10-06 11:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='img_url',
            field=models.URLField(max_length=300, null=True),
        ),
    ]
