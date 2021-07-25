from django.db import models

class Bgyoon(models.Model):
    title = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date_published')
    body = models.TextField()
    image = models.ImageField(upload_to = "bgapp/", blank = True, null = True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]