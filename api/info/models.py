from django.db import models
from api.worker.models import User
class Car(models.Model):
    license_no=models.CharField(max_length=100,null=True)
    license_expiry_date=models.DateTimeField()
    insurance_expiry_date=models.DateTimeField()
    insurance_age=models.IntegerField(blank=True)
    image=models.URLField(default="")
    def __str__(self):
        if not self.license_no:
            return "no license number"
        return self.license_no


class Info(models.Model):
    company_name=models.CharField(max_length=100,null=False)
    logo=models.URLField(default="https://res.cloudinary.com/dj42j4pqu/image/upload/v1619305524/plfj8pvkj9pizrv9to57.png")
    manager=models.OneToOneField(User,related_name='manager',on_delete=models.CASCADE,null=True)
    deputy_director=models.OneToOneField(User,related_name='deputy_director',on_delete=models.CASCADE,null=True)    
    car=models.ManyToManyField(Car,blank=True)
    def __str__(self):
        if not self.company_name:
            return "no name"
        return self.company_name


