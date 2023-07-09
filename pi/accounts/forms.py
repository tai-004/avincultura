from django.contrib.auth.forms import User
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django import forms


from django.forms.widgets import FileInput


class AccountsForm(UserCreationForm):
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ['username','first_name', 'email', 'password1', 'password2']

    def clean_email(self):
        ins = self.cleaned_data['email']
        if User.objects.filter(email=ins).exists():
            raise ValidationError("O email {} já está em uso.".format(ins))

        return ins

