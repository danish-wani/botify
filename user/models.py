import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser


class BotifyUser(AbstractUser):
    # Add your custom fields here
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date_of_birth = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.username} with id {self.id}"

    def __repr__(self):
        return f"BotifyUser(username='{self.username}', first_name='{self.first_name}'," \
               f"last_name='{self.last_name}'), email='{self.email}', is_staff='{self.is_staff}'," \
               f"is_active='{self.is_active}', date_joined='{self.date_joined}'"

    class Meta:
        db_table = "botify_user"

