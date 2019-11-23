from django import forms

from shared_app.models import UserProfile


class UserProfileForm(forms.Form):
    class Meta:
        model = UserProfile
        fields = ('user_img', 'phone_number', 'address', 'date_of_birth', 'bio')
