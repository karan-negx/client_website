from django import forms

class SignUpForm(forms.Form):

    email = forms.EmailField(label = "E-Mail", max_length = 40)
    password = forms.CharField(label = "Password",max_length = 20)


class LoginForm(forms.Form):
     
    username = forms.CharField(label = "Username", max_length = 40)
    password = forms.CharField(label = 'Password', max_length = 30)


class CustomerForm(forms.Form):

    manager = forms.CharField(max_length = 30)
    username = forms.CharField(max_length = 40)
    company_name = forms.CharField(max_length = 100)
    phone_number = forms.CharField(max_length = 15)
    email = forms.EmailField()
    account_number = forms.CharField(max_length = 30)
    ifsc_code = forms.CharField(max_length = 20)
    bank_name = forms.CharField(max_length = 30)
    creation_date = forms.DateTimeField()
    gst_number = forms.CharField(max_length = 20)
    street = forms.CharField(max_length = 50)
    zipcode = forms.CharField(max_length = 10)
    city = forms.CharField(max_length = 20)
    state = forms.CharField(max_length = 20)
    country = forms.CharField(max_length = 20)
    seller_id = forms.CharField(max_length = 20)
    password = forms.CharField(max_length = 20)

