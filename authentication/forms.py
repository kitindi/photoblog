from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class LoginForm(forms.Form):
    username = forms.CharField(max_length=63,widget=forms.TextInput(attrs={"class": "bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500"}))
    # This code snippet is defining a form field for the password in a Django form.
    password = forms.CharField(max_length=63, widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder': '••••••••'}), required=True)
    


class SignupForm(UserCreationForm):
    
#     email = forms.EmailField(
# max_length=100,
# required = True,
# help_text='Enter Email Address',
# widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
# )
# first_name = forms.CharField(
# max_length=100,
# required = True,
# help_text='Enter First Name',
# widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
# )
# last_name = forms.CharField(
# max_length=100,
# required = True,
# help_text='Enter Last Name',
# widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
# )
# username = forms.CharField(
# max_length=200,
# required = True,
# help_text='Enter Username',
# widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}),
# )
# password1 = forms.CharField(
# help_text='Enter Password',
# required = True,
# widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}),
# )
# password2 = forms.CharField(
# required = True,
# help_text='Enter Password Again',
# widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password Again'}),

# ) 

    
    
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':''}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':''}))
    password_confirmation = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500', 'placeholder':''}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-primary-600 focus:border-primary-600 block w-full p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500'}))
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ('username', 'email', 'role')