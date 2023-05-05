from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    def __str__(self) -> str:
        return self.username

    def __repr__(self) -> str:
        return self.username