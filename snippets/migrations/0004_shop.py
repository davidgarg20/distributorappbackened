# Generated by Django 3.0.3 on 2020-03-07 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0003_auto_20200307_1744'),
    ]

    operations = [
        migrations.CreateModel(
            name='Shop',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shop', models.CharField(max_length=100)),
                ('shopname', models.CharField(max_length=100)),
                ('ownersname', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('contactno', models.CharField(max_length=100)),
            ],
        ),
    ]
