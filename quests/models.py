from django.db import models


class Quest(models.Model):

    title = models.CharField(max_length=200)
    short = models.CharField(max_length=200)
    plot = models.TextField()
    footer = models.CharField(max_length=100)

    def __str__(self):
        return self.title


class Hero(models.Model):
    quests = models.ManyToManyField(Quest)
    #quests = models.ForeignKey(Quest, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    profession = models.CharField(max_length=200)
    image = models.FileField()
    exp = models.IntegerField(default=0)

    def __str__(self):
        return self.name


