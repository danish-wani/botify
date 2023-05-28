from django import forms


class AuthenticationForm(forms.Form):
    username = forms.CharField(
        max_length=150, widget=forms.TextInput(
            attrs={
                "id": "username",
                "class": "w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:border-indigo-500"
            }
        )
    )
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "id": "password",
                "class": "w-full px-3 py-2 rounded-md border border-gray-300 focus:outline-none focus:border-indigo-500"
            }
        )
    )
