from django.db import models

# Create your models here.
class hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    email = models.EmailField()
    pno = models.BigIntegerField()


class bangjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    email = models.EmailField()
    pno = models.BigIntegerField()

class chennijobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    email = models.EmailField()
    pno = models.BigIntegerField()
class punejobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    eligibility = models.CharField(max_length=100)
    addr = models.CharField(max_length=100)
    email = models.EmailField()
    pno = models.BigIntegerField()
