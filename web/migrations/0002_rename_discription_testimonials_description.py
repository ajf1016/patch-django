# Generated by Django 3.2.9 on 2021-11-20 10:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testimonials',
            old_name='discription',
            new_name='description',
        ),
    ]
