# Generated by Django 2.0.1 on 2018-11-01 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classroom', '0005_remove_quiz_report'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='report',
            field=models.FileField(blank=True, null=True, upload_to=''),
        ),
    ]
