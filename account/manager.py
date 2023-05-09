from django.contrib.auth.models import BaseUserManager


class UserManager(BaseUserManager):
    def create_user (self, first_name, last_name, email, password):
        
        #Create Normal user
        if not first_name:
            raise ValueError("First Name is required")
        if not last_name:
            raise ValueError("Last Name is required")
        if not email:
            raise ValueError("Email is required")
        
        user = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_superuser (self, first_name, last_name, email, password):
        
        #Create Superuser
        user = self.create_user(first_name, last_name, email,password)
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user