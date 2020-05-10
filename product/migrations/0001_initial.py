# Generated by Django 3.0.6 on 2020-05-10 17:40

from django.db import migrations, models
import django.db.models.deletion
import product.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('customer', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Attribute',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='AttributeValue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(blank=True, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('parent_id', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='product.Category')),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('default_code', models.CharField(blank=True, max_length=30)),
                ('barcode', models.CharField(blank=True, default='', max_length=50)),
                ('description', models.TextField(blank=True, max_length=200)),
                ('type', models.CharField(choices=[('service', 'Service'), ('consumable', 'Consumable'), ('stockable', 'Stockable')], default='stockable', max_length=10)),
                ('rental', models.BooleanField(default=False)),
                ('sell_price', models.DecimalField(decimal_places=4, default=1, max_digits=10)),
                ('standard_price', models.DecimalField(decimal_places=4, default=1, max_digits=10)),
                ('cost_price', models.DecimalField(decimal_places=4, default=1, max_digits=10)),
                ('qty_available', models.PositiveSmallIntegerField(default=1)),
                ('sale_ok', models.BooleanField(default=False)),
                ('is_product_variant', models.BooleanField(default=False)),
                ('image', models.ImageField(blank=True, upload_to='')),
                ('weight', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('volume', models.DecimalField(blank=True, decimal_places=3, max_digits=6)),
                ('images', models.FileField(blank=True, upload_to=product.models.Product.image_directory_path)),
                ('attribute_ids', models.ManyToManyField(blank=True, to='product.Attribute')),
                ('attribute_value_ids', models.ManyToManyField(blank=True, to='product.AttributeValue')),
                ('categ_id', models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='product.Category')),
                ('company_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, to='customer.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='attribute',
            name='value_ids',
            field=models.ManyToManyField(blank=True, to='product.AttributeValue'),
        ),
        migrations.CreateModel(
            name='ProductVariant',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='product.Product')),
                ('attribute_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.Attribute')),
                ('attribute_value_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='product.AttributeValue')),
                ('template_id', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_variant_template_id_of', to='product.Product')),
            ],
            bases=('product.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='product_variant_id',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.PROTECT, related_name='product_variant_of', to='product.ProductVariant'),
        ),
        migrations.AddField(
            model_name='product',
            name='product_variant_ids',
            field=models.ManyToManyField(blank=True, to='product.ProductVariant'),
        ),
    ]