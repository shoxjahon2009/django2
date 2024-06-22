from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=100)
    content = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField()
    cat = models.ForeignKey('Category', models.PROTECT)

    def str(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=60)

    def str(self):
        return self.name


from django.db import models

# Create your models here.
