from django.db import models


class Industry(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'industries'


class Company(models.Model):
    name = models.CharField(max_length=100)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'companies'


class Person(models.Model):
    name = models.CharField(max_length=100)
    companies = models.ManyToManyField(Company)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'persons'
