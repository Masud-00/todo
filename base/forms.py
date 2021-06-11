from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django import forms
from django.contrib.auth.models import User
from  .models import Task

class Registetion(UserCreationForm):
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter Password'}) )
    password2=forms.CharField(label='Password again',widget=forms.PasswordInput(attrs={'class':"form-control",'placeholder':'Enter  Password again'}))
 
    class Meta:
        model=User
        fields=['username','first_name','last_name','email',]
        widgets={
           'username':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Username'}),
           'first_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Firstname'}),
            'last_name':forms.TextInput(attrs={'class':'form-control','placeholder':'Enter your Lastname'}),
            'email':forms.EmailInput(attrs={'class':'form-control','placeholder':'Enter your Email'}),
               
       }



class Taskform(forms.ModelForm):
    class Meta:
        model=Task
        fields=["title","descriptions","complete"]
        widgets={
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'descriptions':forms.TextInput(attrs={'class':'form-control'})
          
     }
        


class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control','placeholder':'Enter your username'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'autofocus':True,'class':'form-control','placeholder':'Enter your username'}))

