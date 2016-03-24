from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField('auth.User', related_name='profile')
    score = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


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

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-time_created']

# method for updating user score
@receiver(post_save, sender=Question)
def udpate_user_score(sender, instance, **kwargs):
    instance.user.profile.score += instance.value
    instance.user.profile.save()

VOTE_OPTION_CHOICES = (("up", "upvote"), ("down", "downvote"))


class Vote(models.Model):
    answer = models.ForeignKey('app.Answer')
    user = models.ForeignKey('UserProfile')
    vote_choice = models.CharField(max_length=12, choices=VOTE_OPTION_CHOICES, null=True)
    
    class Meta:
        unique_together = (('user', 'vote_choice'),)


class Answer(models.Model):
    body = models.TextField()
    time_created = models.DateTimeField(auto_now_add=True)
    related_question = models.ForeignKey(Question)
    user = models.ForeignKey('auth.User')
    score = models.IntegerField(default=0) # don't want users to edit this
    votes = models.ManyToManyField(UserProfile, through="app.Vote")

    def __str__(self):
        return self.body

# method for updating answer score
@receiver(post_save, sender=Vote)
def udpate_answer_score(sender, instance, **kwargs):
    related_user = User.objects.get(profile=instance.answer.user.profile)
    print(related_user)
    print(instance.vote_choice)
    if instance.vote_choice == "up":
        print('here')
        related_user.profile.score += 10
        related_user.profile.save()
        instance.answer.score += 1
        instance.answer.save()
    elif instance.vote_choice == "down":
        related_user.profile.score -= 5
        related_user.profile.save()
        instance.answer.score -= 1
        instance.answer.save()
        instance.user.score -= 1
        instance.user.save()
