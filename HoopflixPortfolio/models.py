from django.db import models

class contactForm(models.Model):
    FullName = models.CharField(max_length=200)
    Email = models.EmailField()
    Message = models.TextField()

    def __str__(self):
        return self.Email
