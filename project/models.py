from django.db import models
from users.models import Profile

# Create your models here.
class Neighbourhood(models.Model):
    name =models.Charfield(max_length=50)
    location = models.Charfield(max_length=100)
    admin = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='hood')
    logo = models.ImageField(upload_to='logo/')
    description = models.TextField()
    health_number = models.IntegerField(null=True, blank=True)
    police_number = models.IntegerField(null=True, blank=True)
    occupant_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f'{self.name}hood'

    def save_neighbourhood(self):
        self.save()

    def delete_neighbourhood(self):
        self.delete()
    @classmethod
    def find_neighbourhood(cls, neighbourhood_id):
        return cls.objects.filter(id=neighbourhood_id)

class Business(models.Model):
    name = models.Charfield(max_length=100)
    email = models.EmailField(max_length=100)
    description = models.TextField(blank=True)
    neighbourhood = models.ForeignKey(Neighbourhood, on_delete=models.CASCADE, related_name='business')
    user = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='owner')

    def __str__(self):
        return f'{self.name}Business'

    def save_business(self):
        self.save()

    def save_business(self):
        self.save()

class Post(models.Model):
    title = models.Charfield(max_length=100, null=True)
    post = models.TextField()