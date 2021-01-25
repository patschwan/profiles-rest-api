from django.db import models
# Overwrite Standard User/Permission Model see offical docu
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
# wir importieren BaseUserManager um User=email abzuleiten
from django.contrib.auth.models import BaseUserManager


# wir nutzen BaseUserManager
class UserProfileManager(BaseUserManager):
    """Manager for User Profiles"""

    def create_user(self, email, name, password=None):
        """Create a new user profile"""
        if not email:
            raise ValueError('User must have an email address')

        # die Domain klein schreiben
        email = self.normalize_email(email)
        user = self.model(email=email, name=name)

        # so the PW is encrypted and not stored plain in DB
        user.set_password(password)
        # Standard Django saving to a DB aka multiple DBs (see docu)
        user.save(using=self._db)

        return user

    def create_superuser(self, email, name, password):
        """Create and save a new super user with the details"""
        # nope, self isn't missing here - it'S automatically added by python
        user = self.create_user(email, name, password)

        user.is_superuser = True # it's created by PermissionsMixin!
        user.is_staff = True
        user.save(using=self._db)

        return user


class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Database model for users in the system"""
    # email column in DB hinzufügen mit max_length und eindeutig
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # Django benötigt diese class wenn wir custom nutzen? (Ex 22)
    # objects "muss so geschrieben sein"
    objects = UserProfileManager()

    # instead of USername/PW we use email/PW
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def get_full_name(self):
        """Retrieve full name of user"""
        return self.name

    def get_short_name(self):
        """Retrieveshort name of user"""
        return self.name

    # some kind of default für Django Admin - Listet User by email
    def ___str___(self):
        """return string representation of our user"""
        return self.email
