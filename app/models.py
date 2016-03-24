from django.db import models


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')


class Tag(models.Model):
    tag = models.CharField(max_length=30)

    def __str__(self):
        return self.tag


class Question(models.Model):
    title = models.CharField(max_length=75)
    body = models.TextField()
    tag = models.ManyToManyField(Tag)
    user = models.ForeignKey('auth.User')
    time_created = models.DateTimeField(auto_now_add=True)
    value = models.IntegerField(default=0)

    class Meta:
        ordering = ['-time_created']


class Answer(models.Model):
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    related_question = models.ForeignKey(Question)
    user = models.ForeignKey('auth.User')
    score = models.IntegerField(default=0)
