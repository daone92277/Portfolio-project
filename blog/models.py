from django.db import models


class Blog(models.Model):
    image = models.ImageField(upload_to="images/")
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField(max_length=500)

    def summary(self):
        return self.body[:100]

    #def pub_date_pretty(self):
     #   return self.pub_date.strftime("%b %e %y")

    def __str__(self):
        return self.title
 