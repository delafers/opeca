# Generated by Django 4.1.7 on 2023-10-02 19:43

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(max_length=511, verbose_name='Header')),
                ('description', models.CharField(max_length=511)),
                ('img', models.ImageField(upload_to='media/')),
                ('date', models.CharField(default=django.utils.timezone.now, max_length=4047, verbose_name='Date')),
                ('text', models.CharField(max_length=4047)),
                ('ref', models.CharField(max_length=5011)),
            ],
        ),
        migrations.CreateModel(
            name='NewsOld',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Header', models.CharField(max_length=511, verbose_name='Header')),
                ('description', models.CharField(max_length=511)),
                ('img', models.ImageField(upload_to='media/')),
                ('date', models.CharField(default=django.utils.timezone.now, max_length=4047, verbose_name='Date')),
                ('text', models.CharField(max_length=4047)),
                ('ref', models.CharField(max_length=5011)),
            ],
        ),
    ]
