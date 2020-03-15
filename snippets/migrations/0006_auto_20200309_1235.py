# Generated by Django 3.0.3 on 2020-03-09 12:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('snippets', '0005_delete_orderdetail'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Snippet',
        ),
        migrations.AlterField(
            model_name='order',
            name='orderamount',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='payment',
            name='paymentdate',
            field=models.DateTimeField(),
        ),
    ]
