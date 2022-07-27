from django.db import models

# Create your models here.


class Establishment(models.Model):
    direction = models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    rating = models.PositiveSmallIntegerField()
    description = models.TextField()

    class meta:
        constraints = [
            models.UniqueConstraint(
                fields=["direction", "name"],
                name="unique_direction_name",
            )
        ]
