from django.db import models
from formapp.models import Realtors 
from django.contrib.auth.models import User


# Create your models here.
types=[
    ('BUY','buy'),
    ('SELL','sell'),
    ('RENTAL','rental'),
    ('LEASE','lease')   
]
cat=[
    ('1STORY','1story'),
    ('2STORY','2story'),
    ('3STORY','3story'),
    ('DUPLEX','duplex'),
    ('INDIVIDUAL','individual'),
    ('APARTMENT','apartment')
]
status=[
    ('soldout','SOLDOUT'),
    ('pending','PENDING')
]
class allproperties(models.Model):
    name=models.CharField(max_length=100) 
    property_type=models.CharField(choices=types)
    price=models.IntegerField()
    floors=models.CharField(max_length=100)
    category=models.CharField(choices=cat)
    age=models.IntegerField()
    area=models.CharField(max_length=100)
    city=models.CharField(max_length=100)
    no_of_rooms=models.IntegerField()
    no_of_bathrooms=models.IntegerField()
    balcony=models.BooleanField()
    attached_bathroom=models.BooleanField()
    owner_name=models.CharField(max_length=100)
    property_image=models.ImageField(upload_to='media/images/',blank=True,null=True)
    realtorname=models.ForeignKey(Realtors,related_name="realtorss",on_delete=models.CASCADE)
    verdict=models.CharField(max_length=100,choices=status)
    
    def __str__(self):
        return self.name
    
class Rooms(models.Model):
    rproperty=models.ForeignKey(allproperties,related_name="rallproperties",on_delete=models.CASCADE)
    room_pics=models.ImageField(upload_to='rooms/',blank=True,null=True)
    
class LivingArea(models.Model):
    lproperty=models.ForeignKey(allproperties,related_name="lallproperties",on_delete=models.CASCADE)
    living_pics=models.ImageField(upload_to='livingarea/',blank=True,null=True)
    
class Kitchen(models.Model):
    kproperty=models.ForeignKey(allproperties,related_name="kallproperties",on_delete=models.CASCADE)
    kitchen_pics=models.ImageField(upload_to='kicthen/',blank=True,null=True)
    
class Balcony(models.Model):
    bproperty=models.ForeignKey(allproperties,related_name="ballproperties",on_delete=models.CASCADE)
    balcony_pics=models.ImageField(upload_to='balcony/',blank=True,null=True)
    
class Bathroom(models.Model):
    btproperty=models.ForeignKey(allproperties,related_name="btallproperties",on_delete=models.CASCADE)
    bath_pics=models.ImageField(upload_to='bathroom/',blank=True,null=True)

class PropertyBooking(models.Model):
    property = models.ForeignKey(allproperties,on_delete=models.CASCADE)
    # realtor=models.ForeignKey(Realtors,on_delete=models.CASCADE)
    BOOK_CHOICES = (
        ('EMI','Book With EMI'),
        ('ADVANCE','Book Advance'),
    )
    booking_type = models.CharField(max_length=20,choices=BOOK_CHOICES)
    loan_amount = models.FloatField(null=True,blank=True)
    tenure = models.IntegerField(null=True,blank=True)
    emi_amount = models.FloatField(null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property.name
    
class Visit(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    area=models.ForeignKey(allproperties,on_delete=models.CASCADE)
    date=models.DateField()
    time=models.TimeField()
    maintainence=models.IntegerField(default=1000)
    water=models.IntegerField(default=500)
    
    
    
    def __str__(self):
        return self.user.username
    
# class Book(models.Model):
#     user=models.ForeignKey(User,on_delete=models.CASCADE)
#     property=models.ForeignKey(allproperties,on_delete=models.CASCADE)
#     rent=models.IntegerField()
#     advance=models.IntegerField()
#     token=models.IntegerField()
#     status=models.BooleanField(default=False)
    
#     def __str__(self):
#         return self.user.username 
    

    
    