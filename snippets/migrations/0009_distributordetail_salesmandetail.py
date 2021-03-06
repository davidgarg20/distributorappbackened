# Generated by Django 3.0.3 on 2020-03-12 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0008_orderdetail_amount'),
    ]

    operations = [
        migrations.CreateModel(
            name='DistributorDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('distributorid', models.CharField(max_length=100)),
                ('ownername', models.CharField(max_length=100)),
                ('firmname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='SalesmanDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salesmanid', models.CharField(max_length=100)),
                ('distributorid', models.CharField(max_length=100)),
                ('salesmanname', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
