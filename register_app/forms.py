from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .models import User

class UserType1RegistrationForm(UserCreationForm):
    mobile_number = forms.CharField(max_length=15)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2', 'mobile_number']

    def clean_username(self):
        username = self.cleaned_data.get('username')
        #if not username.isdigit():
        #    raise forms.ValidationError("Username must be numeric for User Type 1.")
        return username

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'type1'
        if not self.cleaned_data['password1']:
            user.set_password(self.cleaned_data['mobile_number'])
        if commit:
            user.save()
        return user

class UserType2RegistrationForm(UserCreationForm):
    email = forms.EmailField()
    occupation = forms.CharField(max_length=50)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'occupation']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'type2'
        if commit:
            user.save()
        return user

class CustomAuthenticationForm(AuthenticationForm):
    user_type = forms.ChoiceField(choices=User.USER_TYPE_CHOICES)
