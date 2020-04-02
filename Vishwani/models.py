from django.db import models

class About(models.Model):
    img=models.ImageField(upload_to='media',default='')
    heading=models.CharField(max_length=50,default='')
    discription=models.TextField(blank=True,default='')

    def __str__(self):
        return self.heading

class Education(models.Model):
    Class=models.CharField(max_length=50,default='')
    School=models.TextField(blank=True,default='')
    Session=models.CharField(max_length=20,default='')
    Result=models.CharField(max_length=20,default='')

    def __str__(self):
        return self.Class

class Gallery(models.Model):
    Image=models.ImageField(upload_to='media/gallery',default='')