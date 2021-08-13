from django.contrib.auth.forms import UserCreationForm
from users.models import TaskUser


class RegistrationForm(UserCreationForm):
    """Customize the registration form."""

    class Meta:
        model = TaskUser
        fields = (
            'first_name',
            'last_name',
            'username',
            'password1',
            'password2',
        )
