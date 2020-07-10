from django.contrib.auth.models import User
from django.db import models
from django.utils.html import format_html
from django.conf import settings
from crum import get_current_user
from datetime import datetime
from datetime import date
from django.core.validators import MaxValueValidator
from django.contrib.sessions.models import Session
# from datetime import datetime


# Create your models here.
User = settings.AUTH_USER_MODEL

# Model to store the list of logged in users

class UserSession(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    session = models.OneToOneField(Session, on_delete=models.CASCADE)

class Profile(models.Model):
    user = models.OneToOneField(User,blank=True, null=True, on_delete = models.CASCADE)
    name = models.CharField(max_length=200,null=True)
    is_director = models.BooleanField(default=False)
    is_standard = models.BooleanField(default=False)
    is_management = models.BooleanField(default=False)
    is_principal = models.BooleanField(default=False)
    is_new = models.BooleanField(default=False)
    def __str__(self):
        return  self.name

class Pv(models.Model):
    accounts =(
        ('Sub CF','Sub CF'),
        ('Special','Special'),
        ('Directors','Directors'),
        ('Operations','Operations'),
        ('LSGDP','LSGDP'),
        ('DWAP','DWAP'),
        ('Capacity(USD)','Capacity(USD)')
        )
    acc =(
    ('Yes','Yes'),
    ('No', 'No')
    )

    source =(
            ('GOG','GOG'),
            ('Others', 'Others')
          )
    pv =(
        ('General','General'),
        ('Honorarium','Honorarium')
       )
    center=(
        ('Cost Center 1','Cost Center 1'),
        ('Cost Center 2','Cost Center 2'),
        ('Cost Center 3','Cost Center 3'),
        ('Cost Center 4','Cost Center 4'),
        ('Cost Center 5','Cost Center 5')
           )
    stat =(
        ('Completed','Completed'),
        ('Returned','Returned'),
        ('Cancelled','Cancelled')
    )
    IA_System_Code = models.AutoField(primary_key = True)
    IA_code = models.CharField(max_length = 150)
    Date_recieved = models.DateField(validators=[MaxValueValidator(limit_value=date.today)])
    Pv_reference = models.CharField(unique = True, max_length = 120)
    Source_of_Funding = models.CharField(max_length=50, choices = source)
    Cost_center = models.CharField(max_length=50, choices = center)
    Payee = models.CharField(max_length=500,blank=True, null=True)
    Description = models.CharField(max_length = 500)
    Account_code = models.CharField(max_length=350)
    Gross_amount = models.DecimalField(max_digits=19, decimal_places=2)
    Withholding_tax = models.DecimalField(max_digits=19, decimal_places=2)
    Net_amount = models.DecimalField(max_digits=19, decimal_places=2)
    Status = models.CharField(max_length = 60, choices = stat )
    Remarks =models.CharField(max_length = 500, blank = True)
    Acc_Impress = models.CharField(max_length = 350,choices=acc)
    Date_returned =models.DateField(null=True,blank = True)
    Type_of_accounts= models.CharField(max_length = 100, choices = accounts)
    Type_of_pv = models.CharField(max_length = 20, choices = pv)
    returned_to_chest = models.DecimalField(max_digits=19, decimal_places=2,default= 0.00)
    createds = models.DateTimeField(default= datetime.now,null=True)
    created_by = models.ForeignKey('auth.User', blank=True, null=True, default=None,on_delete=models.CASCADE,related_name='create')
    modifieds = models.DateTimeField(null=True,validators=[MaxValueValidator(limit_value=date.today)])
    modified_by = models.ForeignKey('auth.User', blank=True, null=True,default=None ,on_delete=models.CASCADE,related_name='modified')
    worker = models.ForeignKey(Profile,null=True, on_delete=models.SET_NULL)
    class Meta():
            ordering = ["-IA_System_Code"]

    def save(self,   *args, **kwargs):
        user = get_current_user()
        if user and not user.pk:
            user = None
        if not self.pk:
            self.created_by = user

            self.created = datetime.now()
        else:
            self.modified_by = user
            self.modified = datetime.now()
        super(Pv, self).save(*args, **kwargs)


    def __str__(self):
        return self.Pv_reference + "--- " + self.Description + "--- " + self.Type_of_pv


class Grade(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Staff(models.Model):
    name = models.CharField(max_length = 300)
    rank = models.ForeignKey(Grade, on_delete=models.CASCADE, blank=True)
    amount = models.DecimalField(max_digits=19, decimal_places=2)
    Pv_reference = models.ForeignKey('Pv',on_delete=models.CASCADE, related_name='Pvreference')
    Date_added = models.DateTimeField(default= datetime.now)

    def __str__(self):
        return self.name






 # class Grade(models.Model):
