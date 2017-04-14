from django import forms

class UserForm(forms.Form):
    name = forms.CharField(max_length=100, label='',
    		widget=forms.TextInput(
            attrs={'placeholder': 'Name'}
        	))
    email = forms.EmailField(max_length=100, label='', 
    		widget=forms.TextInput(
            attrs={'placeholder': 'Email Address'}
        	))
    password = forms.CharField(label='', widget=forms.PasswordInput(
	    	attrs={'placeholder': 'Password'}
	    	))