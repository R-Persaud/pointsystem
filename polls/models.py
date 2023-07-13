from django.db import models



# Create your models here.
class Employee (models.Model):
    empid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    position = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name

class Category (models.Model):
    cid = models.AutoField(primary_key=True)
    title = models.CharField(max_length=30)

class Responsibilities (models.Model):
    rid = models.AutoField(primary_key=True)
    #title = models.CharField(max_length=30)
    cid = models.ForeignKey(Category, on_delete=models.CASCADE, db_column='cid')
    criteria = models.TextField(default='None', blank=True)
    

    def __str__(self):
        return self.criteria

class has (models.Model):
   hid = models.AutoField(primary_key=True)
   empid = models.ForeignKey(Employee, on_delete=models.CASCADE, db_column='empid') 
   rid = models.ForeignKey(Responsibilities, on_delete=models.CASCADE, db_column='rid')
   #score = models.IntegerField()
   score = models.BooleanField(default=False)

class loginModel(models.Model):
    email = models.EmailField(null= False)
    password = models.CharField(max_length= 500)
    
    def __str__(self):
        return self.email


