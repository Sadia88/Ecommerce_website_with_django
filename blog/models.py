from django.db import models

# Create your models here.
class Product(models.Model):
    post_id=models.AutoField(primary_key=True)
    title=models.CharField(max_length=200)
    head0=models.CharField(max_length=500)
    head1=models.CharField(max_length=500)
    head2=models.IntegerField(max_length=500)
    thumbnail=models.ImageField(upload_to='blog/images',default='')
   
    pub_date=models.DateField()
    def __str__(self):
        return self.title