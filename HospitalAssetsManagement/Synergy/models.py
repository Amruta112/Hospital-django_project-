from django.db import models
from django.contrib.auth.models import User

# # Create your models here.

class Hospital(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    hospital_name = models.CharField(max_length=250)
    contact = models.BigIntegerField()  
    address = models.CharField(max_length=200)
    pincode = models.IntegerField()
    admin_name = models.CharField(max_length=200)

    def __str__(self):
        return self.hospital_name


class Asset(models.Model):
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    asset_name = models.CharField(max_length=255)
    asset_Prise = models.CharField(max_length=255)
    purchase_date = models.DateField()
    warranty_start_date = models.DateField()
    contract_end_date = models.DateField()
    contract_type = models.CharField(max_length=100)
    installed_at = models.CharField(max_length=200)
    status = models.CharField(max_length=50)
  
    def __str__(self):
        return self.asset_name 
    

class Complaint_history(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Pending'),
        ('in_progress', 'In Progress'),
        ('resolved', 'Resolved'),
        ('closed', 'Closed'),
    ]
    hospital = models.ForeignKey(Hospital, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    problem_description = models.TextField()
    service_report = models.FileField(upload_to='service_reports/', blank=True, null=True)
    date_reported = models.DateField()
    date_resolved = models.DateField(blank=True, null=True)
    resolved = models.BooleanField(default=False)
    resolution_note = models.TextField(blank=True, null=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='pending')
    # status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='null')

    def __str__(self):
        return self.asset.asset_name
       
    
   
class PurchaseOrder(models.Model):
    assetname = models.CharField(max_length=200)
    discription = models.CharField(max_length=200)
    supplier = models.CharField(max_length=255)
    total_cost = models.DecimalField(max_digits=10, decimal_places=2)


    def __str__(self):
        return self.asset_name
 