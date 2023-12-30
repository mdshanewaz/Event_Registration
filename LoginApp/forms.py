from django.forms import ModelForm
from LoginApp.models import ProfileModel, User
from django.contrib.auth.forms import UserCreationForm

# Forms Stat here
class ProfileForm(ModelForm):
    class Meta:
        model = ProfileModel
        exclude = ('user',)

class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')