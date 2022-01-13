from django.db import models


class Comic(models.Model):
    idComic = models.IntegerField()
    digitalId = models.IntegerField(null=True)
    title = models.CharField(max_length=100, null=True)
    issueNumber = models.IntegerField(null=True)
    variantDescription = models.CharField(max_length=100, null=True)
    description = models.TextField(blank=True)
    modified = models.DateTimeField(auto_now=True, null=True)
    isbn = models.CharField(max_length=50, null=True)
    upc = models.CharField(max_length=50, null=True)
    diamondCode = models.CharField(max_length=50, null=True)
    ean = models.CharField(max_length=50, null=True)
    issn = models.CharField(max_length=50, null=True)
    format = models.CharField(max_length=50, null=True)
    pageCount = models.IntegerField(null=True)

    def __str__(self):
        return self.title