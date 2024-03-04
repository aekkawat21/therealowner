from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile, Item 


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['email', 'username', 'password1', 'password2']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['age', 'phone_number']

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['brand', 'model', 'color', 'category', 'image', 'serial_number','store_date_of_purchase', 'store_of_purchase', 'warranty', 'previous_owner']
        widgets = {
            'store_date_of_purchase': forms.DateInput(format=('%Y-%m-%d'), attrs={'type': 'date'}),
        }

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'email', 'age', 'gender', 'phone_number']

class EmailUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True, help_text='Enter a new email address')

    class Meta:
        model = User
        fields = ('email',)

class ContactChannelsForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone_number', ]


class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'age', 'gender','picture']

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['picture', ] 




