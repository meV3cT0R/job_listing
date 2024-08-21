from django import forms


class SearchForm(forms.Form):
    search = forms.CharField(label="search", max_length=40, widget=forms.TextInput(attrs={
        "class" : "border border-2 rounded-lg"
    }),required=True)