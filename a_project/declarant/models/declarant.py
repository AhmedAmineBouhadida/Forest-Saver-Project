from django.contrib.auth.models import User
from django.db import models

# Définition de la classe Declarant
class Declarant(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
    ]
    
    first_name = models.CharField(max_length=25, blank=True, default="Unknown")
    last_name = models.CharField(max_length=25, blank=True, default="Unknown")
    username = models.CharField(max_length=50, blank=True, default="Unknown")
    age = models.IntegerField(blank=True, default=0)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)

    # Représentation textuelle de l'objet declarant
    def __str__(self):
        return f'{self.first_name} {self.last_name}'

    def save(self, *args, **kwargs):
        if not self.pk and not self.user:
            self.user = User.objects.create_user(
                username=self.username,
                first_name=self.first_name,
                last_name=self.last_name
            )
        else:
            if self.user:
                self.user.username = self.username
                self.user.first_name = self.first_name
                self.user.last_name = self.last_name
                self.user.save()
        super().save(*args, **kwargs)

    # Supprimer l'utilisateur associé lors de la suppression du declarant
    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()
        super().delete(*args, **kwargs)
