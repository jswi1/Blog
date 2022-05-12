from django.db import models

class Maqola(models.Model):
    sarlavha = models.CharField(max_length=200)
    sana = models.DateField(auto_now_add=True)
    matn = models.TextField()
    rasm = models.FileField(blank=True)

    def __str__(self):
        return self.sarlavha

class Intervyu(models.Model):
    link = models.URLField()
    sana = models.DateField(auto_now_add=True)
    sarlavha = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.sarlavha} ({self.sana})"
