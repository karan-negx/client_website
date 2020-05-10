from datetime import datetime
from django.db import models
from customer.models import Customer

class Product(models.Model):
    name = models.CharField(max_length = 100)
    default_code = models.CharField(max_length = 30, blank = True)
    barcode = models.CharField(max_length = 50,blank =True, default = "")
    description = models.TextField(max_length = 200, blank = True)
    type = models.CharField(max_length = 10,choices = [
        ("service","Service"),
        ("consumable","Consumable"),
        ("stockable","Stockable")], default = "stockable")
    rental = models.BooleanField(default=False)
    categ_id = models.ForeignKey("Category", on_delete = models.PROTECT, default = 1)
    #list price price define by the user for template/ the price at which the product will be solved.
    sell_price = models.DecimalField(max_digits = 10,decimal_places = 4,default= 1)
    # basic price of the product whenever no price is defined.
    standard_price = models.DecimalField(max_digits = 10,decimal_places = 4, default= 1)
    #cost price / manufacturing price of the product
    cost_price = models.DecimalField(max_digits = 10,decimal_places = 4, default= 1)
    qty_available = models.PositiveSmallIntegerField(default = 1)
    sale_ok = models.BooleanField(default=False)
    company_id = models.ForeignKey(Customer, on_delete = models.PROTECT, blank = True, null = True)
    is_product_variant = models.BooleanField(default = False)
    attribute_ids = models.ManyToManyField("Attribute", blank = True)
    attribute_value_ids = models.ManyToManyField("AttributeValue", blank = True)
    product_variant_ids = models.ManyToManyField("ProductVariant",blank=True)
    product_variant_id = models.ForeignKey("ProductVariant", related_name = "product_variant_of",
        on_delete = models.PROTECT,blank= True, null = True)
    image = models.ImageField(blank = True)
    weight = models.DecimalField(max_digits=6, decimal_places=3, blank = True, null = True)
    volume = models.DecimalField(max_digits=6, decimal_places=3, blank=True, null = True)

    # upload product images to the uploads folder.

    def image_directory_path(self, instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
        date = datetime.now().strftime("%d%m%Y")
        return '{}/{}/{}'.format(instance.name,date, filename)

    images = models.FileField(upload_to=image_directory_path, blank = True)

    def __str__(self):
        return self.name



class ProductVariant(Product):
    attribute_id = models.ForeignKey("Attribute", on_delete = models.PROTECT)
    attribute_value_id = models.ForeignKey("AttributeValue", on_delete = models.PROTECT)
    template_id = models.ForeignKey("Product",related_name = "product_variant_template_id_of", on_delete = models.PROTECT, blank = True)

    def __str__(self):
        return self.name

    
class Category(models.Model):
    name = models.CharField(max_length = 50)
    parent_id = models.OneToOneField("Category",on_delete = models.PROTECT,blank = True, null = True)
    description = models.TextField(max_length = 200, blank = True)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length = 30)
    value_ids = models.ManyToManyField("AttributeValue", blank = True)
    description = models.TextField(max_length = 200,blank = True)

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    name = models.CharField(max_length = 30)
    description = models.TextField(max_length = 200,blank = True)

    def __str__(self):
        return self.name

    