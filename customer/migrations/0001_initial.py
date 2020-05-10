# Generated by Django 3.0.6 on 2020-05-09 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('manager', models.CharField(blank=True, max_length=30)),
                ('company_name', models.CharField(blank=True, max_length=100)),
                ('phone_number', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('account_number', models.CharField(blank=True, max_length=30)),
                ('ifsc_code', models.CharField(blank=True, max_length=20)),
                ('bank_name', models.CharField(blank=True, max_length=30)),
                ('creation_date', models.DateTimeField(auto_now_add=True)),
                ('gst_number', models.CharField(blank=True, max_length=20)),
                ('street', models.CharField(blank=True, max_length=50)),
                ('zipcode', models.CharField(blank=True, max_length=10)),
                ('city', models.CharField(blank=True, max_length=20)),
                ('state', models.CharField(blank=True, max_length=20)),
                ('country', models.CharField(blank=True, max_length=20)),
                ('seller_id', models.CharField(blank=True, max_length=20)),
                ('password', models.CharField(blank=True, max_length=20)),
            ],
        ),
    ]