# Generated by Django 2.2.2 on 2019-07-02 04:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_student_timestamp'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='section',
            field=models.CharField(blank=True, choices=[('a', 'A'), ('b', 'B'), ('c', 'C')], max_length=10, null=True, verbose_name='Section'),
        ),
        migrations.AlterField(
            model_name='student',
            name='department',
            field=models.CharField(blank=True, choices=[('ise', 'info science'), ('mh', 'mech'), ('cv', 'civil'), ('bt', 'biotech')], max_length=30, null=True, verbose_name='Department'),
        ),
    ]
