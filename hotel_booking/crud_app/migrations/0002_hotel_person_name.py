# Generated by Django 5.0.3 on 2024-03-15 10:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('crud_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='hotel',
            name='person_name',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
