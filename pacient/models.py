from django.db import models


class Pacient(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    rut = models.CharField(max_length=12)
    birthdate = models.DateField()
    phone_number = models.CharField(max_length=15)
    email_address = models.EmailField()

    def __unicode__(self):
        return '{0}{1}'.format(self.first_name, self.last_name)
