# Generated by Django 3.1.5 on 2021-05-12 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0007_auto_20210408_0024'),
    ]

    operations = [
        migrations.CreateModel(
            name='Add_Sale',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('color', models.CharField(choices=[('White', 'White'), ('Black', 'Black')], max_length=10)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=3)),
                ('quantity', models.PositiveIntegerField()),
                ('invoice_number', models.CharField(max_length=10)),
                ('date', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Add_Stock',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(auto_now=True)),
                ('color', models.CharField(choices=[('White', 'White'), ('Black', 'Black')], max_length=10)),
                ('size', models.CharField(choices=[('S', 'Small'), ('M', 'Medium'), ('L', 'Large'), ('XL', 'Extra Large')], max_length=3)),
                ('quantity', models.PositiveIntegerField()),
                ('details', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='sales',
            name='item',
        ),
        migrations.DeleteModel(
            name='Product',
        ),
        migrations.DeleteModel(
            name='Sales',
        ),
    ]