# Generated by Django 5.0.7 on 2024-09-06 17:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_alter_data_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='data',
            name='image',
            field=models.ImageField(blank=True, max_length=2000, null=True, upload_to=''),
        ),
    ]