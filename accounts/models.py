from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

class UserManager(BaseUserManager):
    def create_user(self, username, password=None, store=None, is_staff=False, is_admin=False, is_active=True): 
        if not username:
            raise ValueError("Username berilishi kerak!")
        if not password:
            raise ValueError('Parol kiritilishi kerak')
        if store == None:
            store = 0
        user = self.model(
            username=username,
            store = store,
        )

        user.set_password(password)
        user.is_active = is_active
        user.admin = is_admin
        user.staff = is_staff
        user.save(using=self._db)
        
        return user

    def create_staffuser(self, username, password=None):
        user = self.create_user(username, password=password, is_staff=True)
        return user

    def create_superuser(self, username, password=None):
        user = self.create_user(username, password=password, is_staff=True, is_admin=True)
        return user

class User(AbstractBaseUser):
    username = models.CharField(max_length=255, unique=True,verbose_name = "Xodim")
    store = models.IntegerField(verbose_name = "Truck")
    active = models.BooleanField(default=True)
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)


    USERNAME_FIELD = 'username'

    objects = UserManager()

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

