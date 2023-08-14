from django import forms
from .models import Fruit


class CreateFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Fruit Name'}),
            'image': forms.TextInput(attrs={'placeholder': 'Fruit Image URL'}),
            'description': forms.Textarea(attrs={'placeholder': 'Fruit Description'}),
            'nutrition': forms.Textarea(attrs={'placeholder': 'Nutrition Info'})
        }

        labels = {
            'name': '',
            'image': '',
            'description': '',
            'nutrition': ''
        }


class EditFruitForm(forms.ModelForm):
    class Meta:
        model = Fruit
        fields = '__all__'

        labels = {
            'image': 'Image URL',
        }


class DeleteFruitForm(forms.ModelForm):

    class Meta:
        model = Fruit
        exclude = ["nutrition"]
        labels = {
            'image': 'Image URL',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
