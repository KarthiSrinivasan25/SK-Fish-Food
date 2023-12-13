# Generated by Django 4.0.5 on 2022-09-14 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_client_details'),
    ]

    operations = [
        migrations.CreateModel(
            name='client_requirement_details',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('fish_variety', models.CharField(max_length=200)),
                ('fish_quantity', models.PositiveBigIntegerField(null=True)),
                ('culture_operation_type', models.CharField(max_length=200)),
                ('input_type', models.CharField(max_length=200)),
                ('food_variety', models.CharField(max_length=200)),
            ],
        ),
    ]