from django.db import models
from accounts.models import User


class Truck(models.Model):
    store_emp_id = models.ForeignKey('accounts.User', verbose_name = "Truck xodimi", default = 0, on_delete=models.SET_DEFAULT)
    name = models.CharField(max_length=255, verbose_name = "Truck nomi", default='unknow')

    def __str__(self):
        return self.name


class InfoByDate(models.Model):
    
    ADMINS = [
        ('LA', 'Luqmonjon akaga'),
        ('AA', 'Abdujalil akaga'),
    ]

    truck_id = models.ForeignKey('Truck', default=0, on_delete=models.SET_DEFAULT)
    date = models.DateField(auto_now_add=True)
    day = models.IntegerField(default=0)
    year = models.CharField(max_length=16, null=True)
    month = models.CharField(max_length=128, null=True)  
    total = models.IntegerField()
    card = models.IntegerField()
    
    cookers = models.IntegerField()
    sellers = models.IntegerField()
    cleaners = models.IntegerField()
    somsapazlar = models.IntegerField()
    suvchilar = models.IntegerField()
    ffcookers = models.IntegerField()

    expenses = models.IntegerField()

    un_expenses = models.IntegerField()
    unecomment = models.TextField(default='')
    page = models.TextField(default = '')
    admin_expenses = models.IntegerField()
    admin = models.CharField(max_length=2, choices=ADMINS, default='LA')
    total_left = models.IntegerField(default=0)

    @property
    def get_month(self):
        if self.date:
            return self.date.strftime("%B")
        return "No date entry"

    @property
    def get_total(self):
        total = self.total - self.card - self.cookers - self.sellers - self.cleaners - self.somsapazlar - self.suvchilar - self.ffcookers - self.expenses - self.un_expenses - self.admin_expenses 
        return total 


    def save(self, *args, **kwargs):
        self.total_left = self.get_total 
        super(InfoByDate, self).save(*args, **kwargs)  

    def __str__(self):
        return self.month



class Product(models.Model):

    categories = [
        ('Ovqat', 'Ovqat'),
        ('Suv', 'Suv'),
    ]

    truck = models.ForeignKey('Truck', default=0, on_delete=models.SET_DEFAULT)
    product_id = models.AutoField(primary_key=True)
    product = models.CharField(max_length=255)
    category = models.CharField(max_length=8, choices=categories, null=True, default='Ovqat')
    defect = models.IntegerField(default=0)

    yest_left = models.IntegerField(default=0)
    total_quantity = models.IntegerField(default=0)

    quantity = models.IntegerField()
    quantity_sold = models.IntegerField(default=0)
    left = models.IntegerField(default=0)
    price = models.IntegerField()
    extra = models.IntegerField(default=0)
    summ = models.IntegerField(default=0)   


    @property
    def get_total_left(self):
        return self.yest_left + self.quantity

    @property
    def get_sum(self):
        return self.quantity_sold * self.price

    @property
    def get_left(self):
        if self.defect == self.extra:
            return self.left
        elif self.defect > self.extra or self.defect < self.extra:
            return self.left - self.defect

    @property
    def get_sold(self):
        if (self.left > 0 and self.extra > self.defect) or (self.left > 0 and self.extra < self.defect):
            return self.total_quantity - self.left
        elif self.left > 0 and self.extra < self.defect:
            return self.total_quantity - self.left
        elif self.left == 0 and self.defect == 0:
            return 0
        elif self.defect == self.extra:
            return self.quantity_sold
        else:
            return self.quantity_sold

    def save(self, *args, **kwargs):
        self.total_quantity = self.get_total_left
        self.quantity_sold = self.get_sold
        self.left = self.get_left
        self.summ = self.get_sum
        super(Product, self).save(*args, **kwargs)  

    def __str__(self):
        return self.product

class Archive(models.Model):
    archive_truck_id = models.ForeignKey('Truck', default=0, on_delete=models.SET_DEFAULT)
    date = models.DateField(auto_now_add=True)
    year = models.CharField(max_length=16, null=True)
    month = models.CharField(max_length=128, null=True)
    page = models.TextField(default='')  
    comment = models.TextField(default='')

    def __str__(self):
        return self.archive_truck_id
