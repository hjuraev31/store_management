from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from . models import User
# User = get_user_model()


class UserAdminCreationForm(forms.ModelForm):

    password1 = forms.CharField(label='Parol', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Parolni qaytaring', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = '__all__'

    def clean_password2(self): 
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parollar togri kelmayapti!')
        return password2

    def save(self, commit=True): 
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user


class UserAdminChangeForm(forms.ModelForm):

    password = ReadOnlyPasswordHashField()

    class Meta:
        model = User
        fields = '__all__'

    def clean_password(self):
        return self.initial['password']


class LoginForm(forms.Form):
    username = forms.CharField(label='Foydalanuvchi', widget=forms.TextInput(attrs={'class': 'form-input',
                                                                           'placeholder': 'Foydalanuvchini kiriting'}))
    password = forms.CharField(label='Parol', widget=forms.PasswordInput(attrs={'class': 'form-input',
                                                                                   'placeholder': 'Parolni kiriting'}))


class RegistrationForm(forms.ModelForm):
    
    password1 = forms.CharField(label='Parol', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Parolni kiriting'}))
    password2 = forms.CharField(label='Parolni tasdiqlash', widget=forms.PasswordInput(attrs={'class': 'form-input', 'placeholder': 'Parolni tasdiqlang'}))

    class Meta:
        model = User
        fields = ['username','store']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-input', 'placeholder': 'Foydalanuvchini kiriting'})}

    def clean_password2(self):  # checking that the two passwords match
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('Parollar bir biriga togri kelmayapti')
        return password2

    def save(self, commit=True): # save the provided password in hashed format
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.is_active = False
            user.save()
        return user