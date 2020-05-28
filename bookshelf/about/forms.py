from django import forms
from about.models import About


class AboutForm(forms.ModelForm):

    class Meta:
        model = About
        fields = ('header', 'text', 'image')

        widgets = {
            'header':forms.TextInput(attrs={'class':'textinputclass'}),
            'text':forms.Textarea(attrs={'class': 'editable medium-editor-textarea postcontent'}),
            'image':forms.ClearableFileInput(attrs={'multiple': True})
        }
