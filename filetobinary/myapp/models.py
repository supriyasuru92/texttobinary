from django.db import models

# Create your models here.

class fileupload(models.Model):
    field_name = models.FileField(upload_to='documents/', max_length=254)

