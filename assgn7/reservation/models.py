from django.db import models

class ClientType(models.Model):
    name = models.CharField(max_length=100)

    def str(self):
        return self.name

class Client(models.Model):
    cid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    type = models.ForeignKey(ClientType, on_delete=models.CASCADE)

    def str(self):
        return self.name

class Product(models.Model):
    pid = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def str(self):
        return self.name

class Order(models.Model):
    oid = models.AutoField(primary_key=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    products = models.ManyToManyField(Product)
    order_date = models.DateField()

    def str(self):
        return f"Order #{self.oid} by {self.client.name}"