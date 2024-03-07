from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    email = models.EmailField()
    is_active = models.BooleanField()

    class Meta:
        db_table = 'users'

class Landlord(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    phone_number = models.CharField(max_length=20, null=True)
    properties_owned = models.SmallIntegerField(default=0)
    date_of_birth = models.DateField()
    date_joined = models.DateTimeField()
    user = models.OneToOneField(User, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'landlords'

class Tenant(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.EmailField(null=True)
    phone_number = models.CharField(max_length=20, null=True)
    landlords = models.ManyToManyField(Landlord)

    class Meta:
        db_table = 'tenants'

class Location(models.Model):
    country = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    zip_code = models.IntegerField()

    class Meta:
        db_table = 'locations'

class Property(models.Model):
    name = models.CharField(max_length=150)
    tag = models.CharField(max_length=50, null=True)
    rent_amount = models.IntegerField()
    location = models.ForeignKey(Location, on_delete=models.CASCADE)

    class Meta:
        db_table = 'properties'

class PropertyTenant(models.Model):
    start_date = models.DateField()
    end_date = models.DateField()
    deposit_amount = models.IntegerField()
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    tenant = models.ForeignKey(Tenant, on_delete=models.CASCADE)

    class Meta:
        db_table = 'properties_tenants'
        constraints = [
            models.UniqueConstraint(fields=['property', 'tenant'], name='unique_property_tenant')
        ]

class Payment(models.Model):
    date = models.DateField()
    amount_paid = models.IntegerField()
    property = models.ForeignKey(Property, null=True, on_delete=models.SET_NULL)
    tenant = models.ForeignKey(Tenant, null=True, on_delete=models.SET_NULL)

    class Meta:
        db_table = 'payments'