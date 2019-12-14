from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Chat(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True, )
    file = models.FileField(upload_to='files/', blank=True, null=True, )

    def __str__(self):
        return self.message



