from .models import Panel
from django.forms import ModelForm, TextInput, Textarea, FileInput, DateInput, SelectMultiple


class CreateForm(ModelForm):
    class Meta:
        model = Panel
        fields = ['title', 'descriptions', 'file', 'created', 'participants']

        widgets = {
            "title": TextInput(attrs={

                'placeholder': 'Введите тему'
            }),

            "descriptions": Textarea(attrs={

                'placeholder': 'Введите своё описание'
            }),

            "file": FileInput(attrs={

                'placeholder': 'Файл'
            }),
            'created': DateInput(format='%Y-%m-%d', attrs={
                'type': 'date'
            }),

            'participants': SelectMultiple(attrs={
                'placeholder': 'Список участников'
            }),

        }