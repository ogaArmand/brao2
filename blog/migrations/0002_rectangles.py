# Generated by Django 4.1.7 on 2023-04-09 19:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='rectangles',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libele', models.CharField(max_length=100)),
                ('X', models.IntegerField()),
                ('Y', models.IntegerField()),
                ('Largeur', models.IntegerField()),
                ('Hauteur', models.IntegerField()),
                ('create_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]