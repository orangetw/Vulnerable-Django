from django.db import models

class Messages(models.Model):
    name    = models.CharField( max_length=16 )
    content = models.CharField( max_length=256 )
    ip      = models.IPAddressField()
    time    = models.DateTimeField( auto_now_add=True )