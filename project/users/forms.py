from django import forms
from django.forms import ModelForm
from .models import Item

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
    contact = forms.IntegerField(label='',widget=forms.TextInput(
            attrs={'placeholder':'Contact Number'}
            )) 
    address = forms.CharField(label='', widget = forms.TextInput(
            attrs={'placeholder': 'Address'}
            ))


class LoginForm(forms.Form):
    email = forms.EmailField(max_length=100, label='', 
    		widget=forms.TextInput(
            attrs={'placeholder': 'Email Address'}
        	))
    password = forms.CharField(label='', widget=forms.PasswordInput(
	    	attrs={'placeholder': 'Password'}
	    	))
                    
class SellerForm(forms.Form):
    class Meta(ModelForm):
        model = Item
        fields = ['title','description','price','image','quantity','category']
    # CHOICES= (
    # ('1','Cars and Bikes'),
    # ('2','Home and Decoration'),
    # ('3','Mobile and Tablets'),
    # ('4','Home appliances'),
    # ('5','Fashion'),
    # ('6','Books'),
    # ('7','Sports and Fitness'),
    # ('8','Laptops and PCs'),
    # ('9','Toys and Kids Accessories'),
    # )

    # name = forms.CharField(max_length=100, label='',
    #         widget=forms.TextInput(
    #         attrs={'placeholder': 'Name', 'class':'form-control'}
    #         ))
    # price = forms.IntegerField(label='',
    #          widget=forms.TextInput(
    #         attrs={'placeholder': 'Price (In Rupees)', 'class':'form-control'}
    #         ))

    # quantity = forms.IntegerField(label='',
    #          widget=forms.TextInput(
    #         attrs={'placeholder': 'Enter Quantity', 'class':'form-control'}
    #         ))

    # image = forms.ImageField(widget=forms.FileInput())

    # description = forms.TextInput(attrs={'placeholder': 'Enter Product Description', 'class':'form-control'}
    #         )

    # category = forms.CharField(label='',
    #          widget=forms.Select(
    #         choices=CHOICES
    #         ))
