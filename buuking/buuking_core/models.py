from django.db import models
from django.contrib.auth.hashers import make_password
from django.utils.timezone import now


class Member(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    firstname = models.CharField(max_length=255)
    password_member = models.CharField(max_length=128)
    email = models.EmailField(max_length=255)
    phone = models.IntegerField()
    created_at = models.DateTimeField(default=now)
    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.password_member.startswith("pbkdf2_sha256$"):
            self.password_member = make_password(self.password_member)
        super().save(*args, **kwargs)


class Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)
    price = models.IntegerField()
    stock = models.PositiveIntegerField()


class TableBuuking(models.Model):
    id = models.AutoField(primary_key=True)
    num_total_people = models.PositiveIntegerField()
    location = models.IntegerField()


class Buuking(models.Model):
    id = models.AutoField(primary_key=True)
    member = models.ForeignKey(to=Member, on_delete=models.CASCADE, default=None)
    product = models.ForeignKey(to=Product, on_delete=models.CASCADE, default=None)
    table = models.ForeignKey(to=TableBuuking, on_delete=models.CASCADE, null=True, blank=True, default=None)
