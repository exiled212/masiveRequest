from django.db import models

class Order(models.Model):
    pass

class Get(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Process(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)

class Pick(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)