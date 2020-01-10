from django import forms
from .models import resume_info

class resume_info_form(forms.ModelForm):

    CHOICES = (
        ('#ffb6b9', 'pink'),
        ('#51eaea', 'skyblue'),
        ('#be9fe1','purple'),
        ('#c3f584','green'),
        ('#ffd271','yellow'),
    )

    template = forms.ChoiceField(choices=CHOICES)



    class Meta():
        model = resume_info
        fields = "__all__"
        exclude = ('slug',)
        labels = {
            'name': ('Full name'),
        }
        help_texts = {
            'skills': ('Put all skills with comma(,)'),
            'name' : ('use only unique name everytime'),
            'email' : ('your resume will directly sent to your email address'),
        }
