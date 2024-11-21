from django import forms

class TiktokMP3Form(forms.Form):
    video_url = forms.URLField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Inserte el enlace de TikTok'}))

class InstagramMP4Form(forms.Form):
    video_url = forms.URLField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Inserte el enlace de Instagram'}))

class FacebookMP4Form(forms.Form):
    video_url = forms.URLField(label='', max_length=200, widget=forms.TextInput(attrs={'class': 'input', 'placeholder': 'Inserte el enlace de Facebook'}))