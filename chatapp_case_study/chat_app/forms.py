from django import forms


class RegisterForm(forms.Form):
    name = forms.CharField(max_length=150)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        password_confirm = cleaned_data.get("password_confirm")

        if password != password_confirm:
            raise forms.ValidationError(
                "password and password confirmation do not match"
            )
