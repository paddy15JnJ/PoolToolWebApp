from django.forms import ModelForm
from django.core.validators import validate_email
from .models import Contact

class CreateContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = ['LastName', 'Email']

    def clean_email(self):
        email = self.cleaned_data['Email']
        if User.objects.filter(email=email).exists():
            raise ValidationError("Email already exists")
        if not validate_email(email):
            raise ValidationError("This needs to be an email address")
        return email
