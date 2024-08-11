from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Recipe(models.Model):
    user  = models.ForeignKey(User, on_delete=models.SET_NULL,null=True,blank=True)
    recipe_name = models.CharField(max_length=255)
    recipe_desc = models.TextField()
    recipe_rating = models.IntegerField()
    recipe_count = models.IntegerField(default=1)

    def __str__(self) -> str:
        return self.recipe_name
    
    
class Department(models.Model):
    department = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.department

    class Meta:
        ordering=['department']    

class StudentID(models.Model):
    student_id = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.student_id

class Student(models.Model):
    department = models.ForeignKey(Department,on_delete=models.CASCADE)
    student_id = models.OneToOneField(StudentID,on_delete=models.CASCADE)
    student_name = models.CharField(max_length=255)            
    student_email = models.EmailField(unique=True)            
    student_age = models.IntegerField(default=18)            
    student_address = models.TextField()            

    def __str__(self) -> str:
        return self.student_name
    
    class Meta:
        ordering=['student_name']    

