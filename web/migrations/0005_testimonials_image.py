# Generated by Django 3.2.9 on 2021-11-22 05:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0004_faq'),
    ]

    operations = [
        migrations.AddField(
            model_name='testimonials',
            name='image',
            field=models.ImageField(default='empty', upload_to='testimonials/'),
            preserve_default=False,
        ),
    ]