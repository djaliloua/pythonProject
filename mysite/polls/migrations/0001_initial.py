# Generated by Django 4.0.3 on 2022-04-06 22:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('firstname', models.CharField(max_length=30)),
                ('lastname', models.CharField(max_length=30)),
                ('description', models.TextField()),
                ('link', models.TextField(null=True)),
                ('photo', models.ImageField(upload_to='profiles')),
            ],
        ),
    ]