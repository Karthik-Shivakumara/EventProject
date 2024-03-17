from django.db import models

class Event(models.Model):
    img= models.ImageField(upload_to='pic')
    name=models.CharField(max_length=50)
    desc=models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Booking(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_phone=models.CharField(max_length=10)
    name=models.ForeignKey(Event,on_delete=models.CASCADE)
    booking_date=models.DateField()
    booked_on=models.DateField(auto_now=True)



