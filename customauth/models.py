from django.db import models
from django.contrib.auth.models import(AbstractBaseUser, BaseUserManager)

# Create your models here.

class UserManager(BaseUserManager):
    def create_user(self, userid, password=None, is_active=True, is_staff=False, is_admin=False, is_manager=False, is_engineer=False):
        if not userid:
            raise ValueError("Users must have a vaild Username")
        if not password:
            raise ValueError("Users must have a password")
        user_obj = self.model(
            userid = userid
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.manager = is_manager
        user_obj.engineer = is_engineer
        user_obj.save(using=self._db)
        return user_obj
    
    def create_staffuser(self, userid, password=None):
        user = self.create_user(
            userid,
            password=password,
            is_staff=True
        )
        user.save(using=self._db)
        return user

    def create_superuser(self, userid, password=None):
        user = self.create_user(
            userid,
            password=password,
            is_staff=True,
            is_admin=True
        )
        user.save(using=self._db)
        return user

    def create_manager(self, userid, password=None):
        user = self.create_user(
            userid,
            password=password,
            is_manager=True
        )
        user.save(using=self._db)
        return user

    def create_engineer(self, userid, password=None):
        user = self.create_user(
            userid,
            password=password,
            is_engineer=True
        )
        user.save(using=self._db)
        return user


class User(AbstractBaseUser):
    userid = models.CharField(max_length=15, default='null', unique=True)
    active = models.BooleanField(default=True) #can login
    staff = models.BooleanField(default=True) #staff user non superuser
    admin = models.BooleanField(default=True) #superuser
    manager = models.BooleanField(default=False)
    engineer = models.BooleanField(default=False)
    rank = models.CharField(max_length=200, default='null')
    department = models.CharField(max_length=15, default='null')
    timestamp = models.DateTimeField(auto_now_add=True)

    USERNAME_FIELD = 'userid' #userid
    #USERNAME_FIELD and password are required by default
    REQUIRED_FIELDS = [] #python manage.py createsuperuser

    objects = UserManager()
    def __str__(self):
        return self.userid
    
    def has_perm(self, perm, obj=None):
        #"Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        #"Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active

    @property
    def is_manager(self):
        return self.manager

    @property
    def is_engineer(self):
        return self.engineer

