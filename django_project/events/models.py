from django.db import models

class Event(models.Model):
    EVENT_TYPE_CHOICES = [
        ('PUBLIC', 'Public'),
        ('PERSONAL', 'Personal'),
        ('PRIVATE', 'Private'),
    ]

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    slug = models.SlugField(max_length=255, blank=True, null=True)
    description = models.TextField()
    contact_phone = models.CharField(max_length=255, blank=True, null=True)
    start_time = models.TimeField(blank=True, null=True)
    end_time = models.TimeField(blank=True, null=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    timelines = models.JSONField(blank=True, null=True) 
    max_people_numbers = models.IntegerField(blank=True, null=True)
    country = models.CharField(max_length=255)
    region = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    coordinates = models.JSONField(blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    is_customized = models.CharField(max_length=255, blank=True, null=True)
    order_number = models.IntegerField(blank=True, null=True)
    type = models.CharField(max_length=10, choices=EVENT_TYPE_CHOICES, blank=True, null=True)
    is_featured = models.BooleanField(default=False)
    in_draft = models.BooleanField(default=False)
    owner = models.JSONField(blank=True, null=True)  
    meta_data = models.JSONField(blank=True, null=True)  
    category = models.JSONField(blank=True, null=True)
    followers = models.JSONField(blank=True, null=True)  

    def __str__(self):
        return self.title
