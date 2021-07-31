from django import forms


class Students(forms.Form):
    name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    #rpassword = forms.CharField(label='Confirm Password', widget = forms.PasswordInput)
    agree = forms.BooleanField(label = "I agree")
