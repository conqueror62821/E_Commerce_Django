# Generated by Django 4.2 on 2023-05-08 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webstore', '0008_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='image',
            field=models.ImageField(upload_to='static/images/'),
        ),
    ]