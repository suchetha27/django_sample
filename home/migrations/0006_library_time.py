# Generated by Django 2.2.2 on 2019-07-02 06:45

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_library_book'),
    ]

    operations = [
        migrations.AddField(
            model_name='library',
            name='time',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
