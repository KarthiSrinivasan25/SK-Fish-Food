# Generated by Django 4.0.5 on 2022-09-14 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0004_client_details_approve'),
    ]

    operations = [
        migrations.AddField(
            model_name='client_requirement_details',
            name='approve',
            field=models.BooleanField(default=False),
        ),
    ]
