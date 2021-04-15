from django.db import models


class Coli(models.Model):
    content = models.TextField(blank=False, null=False)