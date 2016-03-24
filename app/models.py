from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    score = models.IntegerField(default=0)


# method for creating profile
@receiver(post_save, sender='auth.User')
def create_profife(sender, **kwargs):
    user_instance = kwargs.get('instance')
    if kwargs.get('created'):
       UserProfile.objects.create(user=user_instance)

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
    value = models.IntegerField(default=5)

    class Meta:
        ordering = ['-time_created']

# method for updating user score
@receiver(post_save, sender=Question)
def udpate_user_score(sender, instance, **kwargs):
    instance.user.profile.score += instance.value
    print(instance.user.profile.score)
    instance.user.profile.save()


class Answer(models.Model):
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    related_question = models.ForeignKey(Question)
    user = models.ForeignKey('auth.User')
    score = models.IntegerField(default=0)
