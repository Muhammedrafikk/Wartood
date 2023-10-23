from django.db import models
from django.utils.safestring import mark_safe
# from tinymce.models import HTMLField

# Create your models here.

class Email(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
        
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name

class Enquiry(models.Model):
    image = models.ImageField(upload_to='photos')
    title = models.CharField(max_length=100)
    paragraph = models.TextField()  
    ICON_CHOICES = (
        ('dlicon design_compass', 'Design Compass Icon'),
        ('dlicon furniture_light', 'Furniture Light Icon'),
        ('dlicon design_design', 'Design Design Icon'),
        ('dlicon tech-2_firewall', 'Firewall Icon'),
        ('dlicon furniture_mixer', 'Furniture Mixer Icon'),
        ('dlicon transportation_bus', 'Transportation Bus Icon'),
    )
    icon = models.CharField(max_length=100, choices=ICON_CHOICES)
    
    def admin_photo(self):
        return mark_safe('<img src="{}" width="50" />'.format(self.image.url))
    admin_photo.short_description = 'Image'
    admin_photo.allow_tags = True

    # product_title = models.CharField(max_length=100)
    # product_details = HTMLField(blank=True, null=True)
    
    def __str__(self):
        return self.title
      
class EnquiryForm(models.Model):
    Product = models.CharField(max_length=100)
    Name = models.EmailField()
    Phone = models.CharField(max_length=100)
    Message = models.TextField()

    def __str__(self):
        return self.Product
