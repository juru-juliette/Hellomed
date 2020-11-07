from django.contrib.auth import get_user_model

# check for unique email and username
user = get_user_model()

# class LoginForm(forms.Form):
#     username =forms.charField()
#     password =forms.charField(
#         widget= forms.PasswordInput(
#             attrs ={
#                 "class": "form-control",
#                 "id": "user-password"
#             }
#         )
#     )

# def clean_username(self):
#     username =self.cleaned.data.get("username")
#     qs = User.objects.filter(username__iexact =username_) 
#     # thisIsMyUsername ==thisismyusername
#     if not qs.exits():
#         raise forms.ValidationError("this is an invalid user.
#         ")
        
#     return username