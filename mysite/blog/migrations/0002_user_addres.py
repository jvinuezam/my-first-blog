# Generated by Django 2.2.5 on 2019-09-08 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='addres',
            field=models.TextField(blank=True),
        ),
    ]