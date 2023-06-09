# Generated by Django 4.2.1 on 2023-05-17 06:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='allprice',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('stockid', models.CharField(max_length=10)),
                ('date', models.CharField(max_length=10)),
                ('price', models.DecimalField(decimal_places=0, default=0, max_digits=11)),
            ],
        ),
        migrations.CreateModel(
            name='allstock',
            fields=[
                ('stockid', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('stockname', models.CharField(max_length=15)),
            ],
        ),
    ]
