# Generated by Django 4.1.7 on 2023-10-02 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=511, verbose_name='description/name')),
                ('file', models.FileField(upload_to='media/behavior/')),
            ],
        ),
    ]
