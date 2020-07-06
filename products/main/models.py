from django.db import models


class Aliment(models.Model):
    """Aliment object

    Args:
        models (object): aliment stored object

    Returns:
        str: aliment infos
    """

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    created_at = models.DateField()
    expires_at = models.DateField()
    stockreading = models.CharField(max_length=20)

    def __str__(self) -> str:
        return f"Name : {self.name} | created : {self.created_at} | expires : {self.expires_at}"


class UpdateDate(models.Model):
    """Updates actions

    Args:
        models (object): aliment scan dates

    Returns:
        str: aliment and dates
    """

    aliment_ref = models.ForeignKey(Aliment, on_delete=models.CASCADE)
    updated_at = models.DateTimeField()

    def __str__(self) -> str:
        return f"Name : {self.aliment_ref} | update : {self.updated_at}"