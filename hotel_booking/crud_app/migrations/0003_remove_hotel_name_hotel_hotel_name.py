# Generated by Django 5.0.3 on 2024-03-15 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0002_hotel_person_name'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hotel',
            name='name',
        ),
        migrations.AddField(
            model_name='hotel',
            name='hotel_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
