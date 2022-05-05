from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)


class UserManager(BaseUserManager):
    def create_user(self, email, first_name, sex, birth_date, height, weight, goal, activity, password=None):
        if not email:
            raise ValueError('Не введена электронная почта')
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            sex=sex,
            birth_date=birth_date,
            height=height,
            weight=weight,
            goal=goal,
            activity=activity
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password=None):
        user = self.model(
            email=self.normalize_email(email)
        )
        user.set_password(password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Goal(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)


class Activity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=64)


class User(AbstractBaseUser):
    email = models.EmailField(
        max_length=255,
        unique=True
    )
    first_name = models.CharField(max_length=64, null=True)
    sex = models.CharField(max_length=1, null=True)  # 1m, 2f
    birth_date = models.DateField(null=True)
    height = models.IntegerField(null=True)
    weight = models.IntegerField(null=True)
    goal = models.CharField(max_length=1, null=True)
    activity = models.CharField(max_length=1, null=True)
    #goal = models.ForeignKey(Goal, on_delete=models.CASCADE)
    #activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email


