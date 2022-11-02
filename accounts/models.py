from cProfile import label
from random import choices
from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from ckeditor.fields import RichTextField
from PIL import Image


class profile(models.Model):
    liste_util=(('association','مجتمع مدني'),('employe','موظف في البلدية'),('cartiers',' رئيس حي'),('organisme','هيئة نظامية'),('citoyen','مواطن'))
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    list_ch=models.CharField(max_length=100,choices=liste_util)
    phone=models.CharField(max_length=30)
    cv_user=models.FileField(upload_to='profile',null=True,blank=True)
   # photo = models.ImageField(blank=True,null=True° width_field=100,)
    photo = ResizedImageField(size=[300, 300])
    bio_p=models.TextField(max_length=1000)
    def __str__(self):
        return self.list_ch

        
class Requette_a(models.Model):
     
    Titre=models.CharField(max_length=150 ,blank=True,null=True)
    content = RichTextField(config_name='awesome_ckeditor',blank=True,null=True)
    lettre=models.TextField(max_length=500,blank=True,null=True)
    join_f=models.FileField(upload_to='requette',blank=True,null=True)
    photo = models.ImageField(blank=True,null=True)


class Requette_u(models.Model):
    userrr=models.ForeignKey(profile,on_delete=models.CASCADE)
    userr=models.ForeignKey(User,on_delete=models.CASCADE)
    lot_terrain=models.BooleanField()
    Titre=models.CharField(max_length=150 )
    content = RichTextField(config_name='awesome_ckeditor')
    lettre=models.TextField(max_length=500,blank=True,null=True)
    join_f=models.FileField(upload_to='requette',blank=True,null=True)
    photo = models.ImageField(blank=True,null=True)
    created_r = models.DateTimeField(auto_now_add=True)
    def __str__(self):
            return self.Titre

'''
class City(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self): #show the actual city name on the dashboard
        return self.name

    class Meta: #show the plural of city as cities instead of citys
        verbose_name_plural = 'cities'
'''
class News(models.Model):
    page_n=models.URLField(max_length=200)
    photo_n=ResizedImageField(size=[200, 600])
    desc_n=models.CharField(max_length=250)
    created_n = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.desc_n
'''
class sos_c(models.Model): 
    fname = models.CharField(max_length=200, blank=True, null=True)
    lname = models.CharField(max_length=200, blank=True, null=True)

    attendance = models.IntegerField(blank=True, null=True)
   
    zipcode = models.CharField(max_length=200,blank=True, null=True)
    city = models.CharField(max_length=200,blank=True, null=True)
    country = models.CharField(max_length=200,blank=True, null=True)
    adress = models.CharField(max_length=200,blank=True, null=True)
    latitude = models.CharField(max_length=200,blank=True, null=True)
    longitude = models.CharField(max_length=200,blank=True, null=True)


    def __str__(self):
        return self.fname
     '''