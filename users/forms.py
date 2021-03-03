from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError
from django.forms import ModelForm, CharField, PasswordInput, EmailField, TextInput


class RegistrationForm(ModelForm):
    password2 = CharField(label='Password confirmation', widget=PasswordInput)

    class Meta:
        model = get_user_model()
        fields = ('email', 'fullname', 'is_instructor', 'password')

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')

        if password and password2 and password != password2:
            raise ValidationError('Passwords do not match.')

        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(AuthenticationForm):
    username = EmailField(widget=TextInput(
        attrs={'class': 'form-control', 'type': 'text', 'name': 'username', 'placeholder': 'E-mail'}
    ), label='E-mail')
    password = CharField(widget=PasswordInput)

    class Meta:
        fields = ('username', 'password')
