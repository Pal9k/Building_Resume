from django.db import models
from django.utils.text import slugify
import random

# Create your models here.
class resume_info(models.Model):

    slug = models.SlugField(allow_unicode=True,unique=True)

    template = models.CharField(max_length=10,null=True,blank=True)

    name = models.CharField(max_length=100)
    title = models.CharField(max_length=100,null=True,blank=True)
    profile_summary = models.CharField(max_length=1500,null=True,blank=True)
    email = models.EmailField(max_length=254)
    address = models.CharField(max_length=1000,null=True,blank=True)
    mobileno = models.IntegerField(null=True,blank=True)

    Latest_Degree = models.CharField(max_length=25,null=True,blank=True)
    school_name = models.CharField(max_length=500,null=True,blank=True)
    university_name = models.CharField(max_length=500,null=True,blank=True)
    percentage = models.FloatField(null=True,blank=True)
    Passout_year = models.IntegerField(null=True,blank=True)

    company_name = models.CharField(max_length=100,null=True,blank=True)
    experience = models.IntegerField(default=0,null=True,blank=True)
    summary = models.CharField(max_length=1500,null=True,blank=True)
    skills = models.CharField(max_length=2000,null=True,blank=True)

    def save(self,*args,**kwargs):
        self.slug = slugify(self.name)
        super().save(*args,**kwargs)
        return self.slug
        # except:
        #     return redirect('home')
