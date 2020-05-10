from django.db import models

class Customer(models.Model):

    manager = models.CharField(max_length = 30,blank=True)
    username = models.CharField(max_length = 40,blank = False)
    company_name = models.CharField(max_length = 100,blank=True)
    phone_number = models.CharField(max_length = 15,blank=True)
    email = models.EmailField()
    account_number = models.CharField(max_length = 30,blank=True)
    ifsc_code = models.CharField(max_length = 20,blank=True)
    bank_name = models.CharField(max_length = 30,blank=True)
    creation_date = models.DateTimeField(auto_now_add = True,blank=True)
    gst_number = models.CharField(max_length = 20,blank=True)
    street = models.CharField(max_length = 50,blank=True)
    zipcode = models.CharField(max_length = 10,blank=True)
    city = models.CharField(max_length = 20,blank=True)
    state = models.CharField(max_length = 20,blank=True)
    country = models.CharField(max_length = 20,blank=True)
    seller_id = models.CharField(max_length = 20,blank=True)
    password = models.CharField(max_length = 20,blank=True)

    def __str__(self):
        return self.username