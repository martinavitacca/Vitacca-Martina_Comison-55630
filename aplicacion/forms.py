from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SeinenForm(forms.Form):
    title = forms.CharField(max_length=100, disabled=True, required=False)
    chapter = forms.IntegerField(required=False)
    volume = forms.IntegerField(required=False)
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = forms.ChoiceField(label="Status: ", choices=ESTADO, required=False)


class ShounenForm(forms.Form):
    title = forms.CharField(max_length=100, disabled=True, required=False)
    chapter = forms.IntegerField(required=False)
    volume = forms.IntegerField(required=False)
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = forms.ChoiceField(label="Status: ", choices=ESTADO, required=False)


class ManhwaForm(forms.Form):
    title = forms.CharField(max_length=100, disabled=True, required=False)
    chapter = forms.IntegerField(required=False)
    volume = forms.IntegerField(required=False)
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = forms.ChoiceField(label="Status: ", choices=ESTADO, required=False)


class ShoujoForm(forms.Form):
    title = forms.CharField(max_length=100, disabled=True, required=False)
    chapter = forms.IntegerField(required=False)
    volume = forms.IntegerField(required=False)
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = forms.ChoiceField(label="Status: ", choices=ESTADO, required=False)


class MangaForm(forms.Form):
    title = forms.CharField(max_length=100, required=True)
    chapter = forms.IntegerField(required=True)
    volume = forms.IntegerField(required=True)
    READING = "Reading"
    PTR = "Plan to read"
    COMPLETED = "Completed"
    ESTADO = [
        (READING, "Reading"),
        (PTR, "Plan to read"),
        (COMPLETED, "Completed"),
    ]
    current_estado = forms.ChoiceField(label="Status: ", choices=ESTADO, required=True)


class UserRegisterForm(UserCreationForm):      
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget= forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserEditForm(UserCreationForm):
    email = forms.EmailField(label="Email")
    password1 = forms.CharField(label="Password", widget= forms.PasswordInput)
    password2 = forms.CharField(label="Confirm password", widget= forms.PasswordInput) 
    first_name = forms.CharField(label="Name", max_length=50, required=False)   
    last_name = forms.CharField(label="Last name", max_length=50, required=False)   

    class Meta:
        model = User
        fields = ['email', 'password1', 'password2', 'first_name', 'last_name']


class AvatarForm(forms.Form):
    imagen = forms.ImageField(required=True)
        