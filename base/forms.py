from django import forms
from django.forms import ModelForm
from .models import Room, Message

class CreateRoom(ModelForm):
    class Meta:
        model = Room
        exclude = ['host','created','updated']
        widgets={
            'name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Enter the name of the room'}),
            'host':forms.Select(attrs={'class':'form-control', 'placeholder':'Choise a host'}),
            'topic':forms.Select(attrs={'class':'form-control','placeholder':'Choise a topic'}),
            'description':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Enter the description of room'}),
        }  

class AddMessage(ModelForm):
    class Meta:
        model = Message
        fields = ['body']
        widgets = {
            'body':forms.Textarea(attrs={'class':'form-control', 'placeholder':'Write your message here ... ', 'style':'height: 100px;'})
        }
    