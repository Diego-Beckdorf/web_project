from django.db import models

from doctor.models import Doctor
from pacient.models import Pacient


class Record(models.Model):
    created_on= models.DateTimeField(auto_now=True)
    entry = models.CharField(max_length=255)
    created_by = models.ForeignKey(Doctor)
    pacient = models.ForeignKey(Pacient)

    def __unicode__(self):
        return '{0} record'.format(self.pacient.__unicode__())
