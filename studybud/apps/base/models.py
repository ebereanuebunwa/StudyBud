from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


# A room will be the child of a topic 
class Topic(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self) -> str:
        return self.name  # 


# A room will be the child of a topic
class Room(models.Model):
    host = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True)  # on_delete: when the topic is deleted, 
    name = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True) # nullable and blankable fields 
    # participants = models.ManyToManyField('Participant', blank=True)
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-updated_at', '-created_at']

    def __str__(self):
        return self.name


# Each room will have messages 
class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  #
    room = models.ForeignKey(Room, on_delete=models.CASCADE)  # if a room gets deleted, all messages will be deleted.
    body = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[:50] + '...'
