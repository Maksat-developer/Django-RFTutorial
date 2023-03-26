from django.db import models
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.utils import timezone
from .managers import UserManager


class UserModel(AbstractUser, PermissionsMixin):
    username = None
    email = models.EmailField(
        unique=True,
        null=True,
        db_index=True,
        verbose_name="Введите Email:")
    first_name = models.CharField(max_length=100, verbose_name="Введите Имя:")
    last_name = models.CharField(
        max_length=100,
        verbose_name="Введите Фамилию:")
    address = models.CharField(max_length=100, verbose_name="Введите аддресс:")
    date_joined = models.DateTimeField(
        default=timezone.now,
        verbose_name="Дата верификации пользователя:")

    is_active = models.BooleanField(
        default=False, verbose_name="Часть Персонала:")
    is_staff = models.BooleanField(
        default=False,
        verbose_name="Активный пользователь:")

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['first_name', 'last_name']

    objects = UserManager()

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self) -> str:
        return self.email


class UserProfile(models.Model):
    user = models.OneToOneField(
        UserModel,
        on_delete=models.CASCADE,
        primary_key=True,
        related_name='user_profile', verbose_name="Пользователь:")
    phone = models.CharField(
        max_length=255,
        blank=True,
        null=True,
        verbose_name="Телефонный номер:")
    is_verified = models.BooleanField(
        default=False, verbose_name="Верифицирован:")
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания профиля:")
    updated_at = models.DateTimeField(
        auto_now=True, verbose_name="Дата обновления профиля:")

    class Meta:
        verbose_name = 'Профиль пользователя:'
        verbose_name_plural = 'Профили пользователей:'

    def __str__(self) -> str:
        return self.user.email
