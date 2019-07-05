# Generated by Django 2.2.2 on 2019-07-02 03:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('student_name', models.CharField(max_length=30, null=True, verbose_name='Student Name')),
                ('department', models.CharField(blank=True, choices=[('ise', 'info science'), ('mh', 'mech'), ('cv', 'civil')], max_length=30, null=True, verbose_name='Department')),
            ],
        ),
    ]
