from django.forms import ModelForm
from .models import *


class PostForm(ModelForm):
    class Meta:
        model = Post
        fields = ["username", "gender", "text"]

    # this function will be used for the validation
    def clean(self):

        # data from the form is fetched using super function
        super(PostForm, self).clean()

        # extract the username and text field from the data
        username = self.cleaned_data.get('username')
        text = self.cleaned_data.get('text')

        # conditions to be met for the username length
        if len(username) < 5:
            self._errors['username'] = self.error_class([
                'Minimalnie 5 literek ziom'])
        if len(text) < 10:
            self._errors['text'] = self.error_class([
                'Post musi mieć co najmniej 10 literek'])

            # return any errors if found
        return self.cleaned_data
