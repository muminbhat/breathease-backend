# Generated by Django 5.0.3 on 2024-03-10 17:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Appointment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(max_length=254)),
                ('phone_number', models.CharField(max_length=155)),
                ('comments', models.TextField()),
                ('in_process', models.BooleanField(default=False)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]