# Generated by Django 4.0.2 on 2022-02-19 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100, unique=True)),
                ('product_price', models.FloatField()),
                ('stock', models.IntegerField()),
                ('image_url', models.CharField(max_length=255)),
                ('crated_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]