from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    """
    Custom user model for AeroDK AI.

    Additional user attributes and profile relationships
    will be implemented as the authentication module evolves.
    """

    pass