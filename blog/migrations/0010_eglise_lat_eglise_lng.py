# Generated by Django 4.1.7 on 2023-04-12 01:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_alter_motpresident_desc'),
    ]

    operations = [
        migrations.AddField(
            model_name='eglise',
            name='lat',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='eglise',
            name='lng',
            field=models.CharField(max_length=255, null=True),
        ),
    ]