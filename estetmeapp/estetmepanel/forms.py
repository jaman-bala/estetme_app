from .models import Panel
from django.forms import ModelForm, TextInput, Textarea, FileInput, DateInput


class CreateForm(ModelForm):
    class Meta:
        model = Panel
        fields = ['title', 'descriptions', 'file', 'created']

        widgets = {
            "title": TextInput(attrs={

                'placeholder': 'Тема задачи'
            }),

            "descriptions": Textarea(attrs={

                'placeholder': 'Введите свой вопрос'
            }),

            "file": FileInput(attrs={

                'placeholder': 'Файл'
            }),
            "created": DateInput(attrs={

                'placeholder': 'Срок задачи'
            }),

        }