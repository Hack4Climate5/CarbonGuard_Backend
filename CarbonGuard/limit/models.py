from django.db import models


class Limit(models.Model):
    emission_limit = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"The emission limit is ${self.emission_limit}"
