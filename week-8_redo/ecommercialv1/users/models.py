from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager



# Create account model 
class MyAccountManager(BaseUserManager):
    
    def create_user(self, first_name, last_name, username, email, password= None):
        if not email:
            return ValueError("User must have an email address ")
        if not username:
            return ValueError("User must have a username")     # this field is actually not needed because, we are the one who is generating the username.
        # here we are creating an object called user 
        user = self.model(
            email       = self.normalize_email(email),
            username    = username,
            first_name  = first_name,
            last_name   = last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user # returning the object.
    
    def create_superuser(self, first_name, last_name, username, email, password):
        user = self.create_user( # calling the create use function for this operation.
                                email       =  self.normalize_email(email),
                                username    =  username,
                                password    =  password,
                                first_name  = first_name,
                                last_name   = last_name,
                                )
    # these are the must to be included field for a super user.
        user.is_admin       =   True
        user.is_active      =   True
        user.is_staff       =   True
        user.is_superuser   =   True
        user.save(using=self._db)
        return user





    
# these are the fields that a user creation model needed.
class Account(AbstractBaseUser):
    first_name  = models.CharField(max_length=50)
    last_name   = models.CharField(max_length=50)
    username    = models.CharField(max_length=50, unique=True)
    email       = models.EmailField(max_length=100, unique=True)
    phone_number= models.CharField(max_length=50)
    
    #required fields are, mandatory while creating a user creation model 
    
    date_joined     = models.DateField(auto_now_add=True)
    last_login      = models.DateField(auto_now=True)
    is_superuser    = models.BooleanField(default=False)
    is_admin        = models.BooleanField(default=False)
    is_staff        = models.BooleanField(default=False)
    is_active       = models.BooleanField(default=False)
    
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS  =['username','first_name','last_name']
    
    objects = MyAccountManager()       # we are using the MyAccountManager for management.                                     # to let the account know thar we are using the MyAccountManager to create user and superusers. 
    
    
    def __str__(self):
        return self.email
    
    def has_perm(self, perm, obj=None):                                     # admin has all the permissions do all the changes 
        return self.is_admin
    
    def has_module_perms(self, add_label):
        return True
    
    
        