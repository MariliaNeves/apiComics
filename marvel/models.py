from django.db import models


class Serie(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    startYear = models.IntegerField(null=True)
    endYear = models.IntegerField(null=True)
    modified = models.DateTimeField(auto_now=True)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.title


class Comic(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100, null=True)
    issueNumber = models.IntegerField(null=True, blank=True)
    variantDescription = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(blank=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    isbn = models.CharField(max_length=50, null=True, blank=True)
    upc = models.CharField(max_length=50, null=True, blank=True)
    diamondCode = models.CharField(max_length=50, null=True, blank=True)
    ean = models.CharField(max_length=50, null=True, blank=True)
    issn = models.CharField(max_length=50, null=True, blank=True)
    format = models.CharField(max_length=50, null=True, blank=True)
    pageCount = models.IntegerField(null=True)
    serie = models.ForeignKey(Serie, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
