from django.db import models
from django.urls import reverse
import uuid

# Create your models here.
class Flan(models.Model):
    flan_uuid = models.UUIDField(primary_key = True, default=uuid.uuid4)
    name = models.CharField(max_length=64)
    description = models.TextField(default=' ')
    image_url = models.URLField(max_length=200, unique=True, default=' ')
    slug = models.SlugField(max_length=50, unique=True, default=' ')
    is_private = models.BooleanField(default=False)

class ContactForm(models.Model):
    contact_form_uuid = models.UUIDField(primary_key = True, default=uuid.uuid4, editable=False )
    customer_email = models.EmailField(unique = True)
    customer_name = models.CharField(max_length = 64)
    message = models.TextField(default='Deje un mensaje')

    def get_absolute_url(self):
        """
        Retorna la url para acceder a una instancia particular de un flan.
        """
        return reverse('flan-detail', args=[str(self.id)])



