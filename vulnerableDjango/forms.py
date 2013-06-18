from django import forms

class MessageForm(forms.Form):
    name    = forms.CharField( required=True, max_length=16 )
    content = forms.CharField( required=True, 
                               max_length=256 )