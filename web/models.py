from django.db import models
import uuid

FAQ_TYPE=(
    ("rent_tracking","Rent Tracking"),
    ("new_deposite","New Deposite"),
    ("existing_deposite","Existing Deposite"),
    
)

class Testimonials(models.Model):
    name = models.CharField(max_length=50)
    designation = models.CharField(max_length=50)
    image = models.ImageField(upload_to="testimonials/")
    description = models.TextField(blank=True,null=True)
    
    def __str__(self):
        return self.name

 
class Promoter(models.Model):
    name = models.CharField(max_length=255)
    image = models.ImageField(upload_to="promoters/")
    
    def __str__(self):
        return self.name
    
class Faq(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    faq_type = models.CharField(max_length=128,choices=FAQ_TYPE)
    
    def __str__(self):
        return self.title
    
class Subscribe(models.Model):
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.email
    
class TestModel(models.Model):
    num = models.BigIntegerField()
    is_student = models.BooleanField(default=False)
    is_mentor = models.BooleanField(null=True)
    Dob = models.DateTimeField(blank=True,null=True)
    document = models.FileField(upload_to='documents/')
    # id = models.UUIDField(primary_key=True,default=uuid.uuid4(),editable=False)
    
    # def __unicode__(self):
    #     return self.id
    
class Car(models.Model):
    name = models.CharField(max_length=128)
    color = models.CharField(max_length=128)
    manufacture = models.ForeignKey("web.manufacturer",on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
class Manufacturer(models.Model):
    name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    phone = models.CharField(max_length=128)
    photo = models.ImageField(upload_to="profile/")
    user = models.OneToOneField("auth.user",on_delete=models.CASCADE)


class Student(models.Model):
    name = models.CharField(max_length=128)
    class_name = models.CharField(max_length=128)
    division = models.CharField(max_length=128)
    groups =models.ManyToManyField("web.StudentGroup")   
    
    def __str__(self):
        return self.name 
    
class StudentGroup(models.Model):
    name = models.CharField(max_length=128)
    color_name = models.CharField(max_length=128)
    
    def __str__(self):
        return self.name
