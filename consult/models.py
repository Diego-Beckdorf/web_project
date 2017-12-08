from django.db import models

from doctor.models import Doctor
from pacient.models import Pacient


class Consult(models.Model):
    pacient = models.ForeignKey(Pacient)
    doctor = models.ForeignKey(Doctor)
    starting = models.DateTimeField()
    lenght = models.PositiveSmallIntegerField()


    def __unicode__(self):
        return '{0} consult on {1}'.format(self.pacient.__unicode__(), self.starting.__str__())
