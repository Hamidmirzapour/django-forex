# Generated by Django 3.2.7 on 2021-09-30 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('base_currency', models.CharField(max_length=10)),
                ('quote_currency', models.CharField(max_length=10)),
            ],
        ),
    ]
