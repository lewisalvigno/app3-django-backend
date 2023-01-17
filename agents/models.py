from django.db import models

# Create your models here.
class Parking(models.Model):
    parkingName = models.CharField(max_length=100)
    parkingAddress = models.CharField(max_length=100)
    parkingPhone = models.CharField(max_length=100)
    parkingImage= models.ImageField(upload_to='images/')
    parkingCapacity = models.CharField(max_length=100)
    parkingPrice = models.CharField(max_length=100)
    default=''
    def __str__(self):
        return self.parkingName

class Paiement(models.Model):
    clientId = models.CharField(max_length=100)
    parking = models.CharField(max_length=100)
    duree = models.CharField(max_length=100)
    montant = models.CharField(max_length=100)
    date = models.CharField(max_length=100)
    periode = models.CharField(max_length=100)

    def __str__(self):
        return self.parking + ' ' + self.clientId
