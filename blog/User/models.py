from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db.models.signals import post_save
from django.dispatch import receiver
from rest_framework.authtoken.models import Token


class UserManager(BaseUserManager):

    def base_user_create_func(self, email, password, is_staff, is_superuser, **extra_fields):
        if not email:
            raise ValueError('Email is must to create an account.')
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            is_staff=is_staff,
            is_active=True,
            is_superuser=is_superuser,
            **extra_fields,
        )
        user.set_password(password)
        user.save()
        return user

    def create_user(self, email, password, **extra_fields):
        return self.base_user_create_func(email, password, False, False, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        return self.base_user_create_func(email, password, True, True, **extra_fields)


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


@receiver(post_save, sender=User)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)