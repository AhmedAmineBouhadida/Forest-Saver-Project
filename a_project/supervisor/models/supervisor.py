from django.contrib.auth.models     import User
from django.db                      import models
from django.contrib.auth.hashers    import make_password
from django.core.exceptions         import ValidationError

#* Definition de la classe SUpervisor :  

class Supervisor (models.Model):  
    first_name   = models.CharField(max_length = 25)
    last_name    = models.CharField(max_length = 25)
    phone_number = models.CharField(max_length = 12)
    username     = models.CharField(max_length = 30)
    password     = models.CharField(max_length = 100 )
    email        = models.CharField(max_length = 255 ,  unique = True )
    user         = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)


    def save (self , *args , **kwargs) : 
        if not self.pk : 
            #! Hachage du password pour le stockage
            self.password = make_password(self.password)
            if User.objects.filter(username = self.username).exists() : 
               raise ValidationError(f"Username {self.username} already exists.")
            self.user = User.objects.create_user(username=self.username, email=self.email, password=self.password)
        else:
            if self.user:
                self.user.username = self.username
                self.user.email = self.email
                self.user.set_password(self.password)
                self.user.save()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"