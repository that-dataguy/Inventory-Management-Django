# Generated by Django 3.1.5 on 2021-03-28 20:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0004_auto_20210328_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shirt',
            name='sale_date',
            field=models.DateField(auto_now=True),
        ),
    ]