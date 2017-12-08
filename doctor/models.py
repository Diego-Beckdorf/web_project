from datetime import timedelta

from django.db import models


class Doctor(models.Model):
    first_name = models.CharField(max_length=63)
    last_name = models.CharField(max_length=63)
    specialty = models.CharField(max_length=255)
    average_consult_duration = models.DurationField(default=timedelta(
        minutes=30))

    def __unicode__(self):
        return '{0} {1}'.format(self.first_name, self.last_name)
