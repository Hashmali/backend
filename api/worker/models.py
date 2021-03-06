from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.utils import timezone
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings
from django.core.validators import RegexValidator
from django.contrib.auth.models import PermissionsMixin


class UserManager(BaseUserManager):

  def create_user(self, phone, password,id_img="",pay_per_day="",work_license_expire="",work_license_type="",work_license_israel="",driving_license_img="",id_no="",age=0,address="",email="",is_superuser=False, is_staff=False, is_admin=False,**extra_fields):
    if not phone:
        raise ValueError('Users must have a phone')
    now = timezone.now()
    user = self.model(
        phone=phone,
        is_superuser=is_superuser,
        is_staff=is_staff, 
        id_img=id_img,
        address=address,
        age=age,
        email=email,
        pay_per_day=pay_per_day,
        work_license_expire=work_license_expire,
        work_license_type=work_license_type,
        work_license_israel=work_license_israel,
        driving_license_img=driving_license_img,
        id_no=id_no,
        is_active=True,
        is_admin=is_admin, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user
  def create_superuser(self, phone, password,id_img="",pay_per_day="",work_license_expire="",work_license_type="",work_license_israel="",driving_license_img="",id_no="",age=0,address="",email="",is_superuser=True, is_staff=True, is_admin=True,**extra_fields):
    if not phone:
        raise ValueError('Users must have a phone')
    now = timezone.now()
    user = self.model(
        phone=phone,
        is_superuser=True,
        is_staff=True, 
        id_img=id_img,
        address=address,
        age=age,
        email=email,
        pay_per_day=pay_per_day,
        work_license_expire=work_license_expire,
        work_license_type=work_license_type,
        work_license_israel=work_license_israel,
        driving_license_img=driving_license_img,
        id_no=id_no,
        is_active=True,
        is_admin=True, 
        last_login=now,
        date_joined=now, 
        **extra_fields
    )
    user.set_password(password)
    user.save(using=self._db)
    return user


class User(AbstractBaseUser,PermissionsMixin):

  id_img=models.URLField(default="")


  first_name = models.CharField(max_length=50, default='worker')

  second_name = models.CharField(max_length=50, default='worker')

  phone = models.CharField(max_length=11,unique=True,validators=[RegexValidator(
            regex='^[0][5][0|2|3|4|5|6|9]{1}[-]{0,1}[0-9]{7}$',
            message='wrong Phone number',
            code='invalid_phone'
        ),])


  username = None


  id_no=models.CharField(max_length=10,null=True,blank=True)

  

  driving_license_img=models.URLField(default="")

  work_license_israel=models.CharField(max_length=50,null=True,blank=True)

  work_license_type=models.CharField(max_length=50,null=True,blank=True)

  work_license_expire=models.CharField(max_length=50,null=True,blank=True)

  age=models.IntegerField(null=True,blank=True)

  address=models.CharField(max_length=100,null=True,blank=True)

  pay_per_day=models.CharField(max_length=100,null=True,blank=True)


  email = models.EmailField(null=True,blank=True)

  image = models.URLField(default="https://res.cloudinary.com/dj42j4pqu/image/upload/v1619305524/plfj8pvkj9pizrv9to57.png")

  is_staff =models.BooleanField(default=False)

  is_admin=models.BooleanField(default=False)

  
  is_active = models.BooleanField(default=True)

  is_superuser=models.BooleanField(default=False)

  last_login = models.DateTimeField(null=True, blank=True)

  date_joined = models.DateTimeField(auto_now_add=True)
    
  #token = models.CharField(max_length=100, default=0)
  class Meta:
        ordering = ('phone',)
  objects = UserManager()

  USERNAME_FIELD = 'phone'

  REQUIRED_FIELDS = ['first_name','second_name',]

  def __str__(self):
    if  self.first_name and self.second_name :
      return self.first_name+" "+self.second_name
    return self.first_name  

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
  if created:
    Token.objects.create(user=instance)