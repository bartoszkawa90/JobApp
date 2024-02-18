from django.db import models


class JobOffer(models.Model):
    title = models.CharField("Title", max_length=240)
    responsibilities = models.CharField("Responsibilities", max_length=1240)
    requirements = models.CharField("Requirements", max_length=1240)
    link = models.URLField("Link", max_length=250)

    def __str__(self):
        return self.title
