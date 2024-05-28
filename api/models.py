from django.db import models

# Create your models here.
class UserData(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)
    provider = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    countryCode = models.CharField(max_length=250)
    isp = models.CharField(max_length=250)
    lat = models.CharField(max_length=250)
    lon = models.CharField(max_length=250)
    org = models.CharField(max_length=250)
    query = models.CharField(max_length=250)
    region = models.CharField(max_length=250)
    regionName = models.CharField(max_length=250)
    status = models.CharField(max_length=250)
    timezone = models.CharField(max_length=250)
    zip = models.CharField(max_length=250)

    def __str__(self):
        return self.query

class UserInfo(models.Model):
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

