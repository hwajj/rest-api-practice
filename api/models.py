from django.db import models


class Member(models.Model):
    name = models.CharField(max_length= 10)
    phone_number = models.CharField(max_length=13)
    address = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return '[{}] {}'.format(self.name, self.phone_number)