from django.db import models
from django.utils.text import slugify

# Create your models here.

class Category(models.Model):
    category_name =models.CharField(max_length=100)
    slug = models.SlugField(max_length= 200 , blank=True)
    
    def save(self,*args, **kwargs):
        self.slug = slugify(self.category_name)
        super(Category,self).save(*args, **kwargs)
        
    def __str__(self):
        return self.category_name
    
class QuantityVariant(models.Model):
        variant_name = models.CharField(max_length=100)
        
        def __str__(self):
          return self.variant_name
          
class colorVariant(models.Model):
        color_name = models.CharField(max_length=100)
        color_code = models.CharField(max_length=100)
        
        def __str__(self):
          return self.color_code
          return self.color_name
  
class sizeVariant(models.Model):
        size_name = models.CharField(max_length=100)
        
        def __str__(self):
          return self.size_name
           
class QualityVariant(models.Model):
        quality_name = models.CharField(max_length=100)
        
        def __str__(self):
          return self.quality_name
          
class PriceVariant(models.Model):
        Price_name = models.CharField(max_length=100)
        
        def __str__(self):
          return self.Price_name
      

                
class Product(models.Model):
    
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_name = models.CharField(max_length=100)
    image = models.ImageField(upload_to='static/products')
    price = models.CharField( max_length=20)
    description = models.TextField()
    stock= models.IntegerField(default=100)
    
    quantity_type = models.ForeignKey(QuantityVariant , blank=True, null=True , on_delete=models.PROTECT)
    color_type = models.ForeignKey(colorVariant , blank=True, null=True, on_delete=models.PROTECT)
    size_type = models.ForeignKey(sizeVariant , blank=True, null=True , on_delete=models.PROTECT)
    quality_type = models.ForeignKey(QualityVariant , blank=True, null=True , on_delete=models.PROTECT)
    price_type = models.ForeignKey(PriceVariant, blank=True, null=True , on_delete=models.PROTECT)
    

    def __str__(self):
        return self.product_name
    
    
class ProductImages(models.Model): 
        Product=models.ForeignKey(Product,on_delete=models.PROTECT)
        image = models.ImageField(upload_to='static/products')   