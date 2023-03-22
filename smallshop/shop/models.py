from django.db import models

# Create your models here.
## one
#reference object 
class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name
    
## many
#referred object
class Product(models.Model):

    product_name  = models.CharField(max_length=200)
    product_price = models.FloatField(default=0)
    #one to many relationship - one category Contain several products 
    product_category = models.ForeignKey(
        Category, on_delete=models.PROTECT,
        
        default=None, related_name="cat_id"
          )
    product_store_code = models.IntegerField(null=True)
    product_expiry_date = models.DateField(null=True)
    #product_image = models.ImageField(null=True)

    class Meta(): 
        db_table = 'product'

    def __str__(self):
        return self.product_name

