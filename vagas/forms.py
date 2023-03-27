from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Field, Layout, Submit
from crispy_forms.bootstrap import FormActions

from .models import Candidatura

class CandidatarForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        # self.helper.layout = Layout(
        #     FormActions(
        #         Submit('save', 'Salvar'),
        #         Button('cancel', 'Cancelar')
        #     )
        # )

    class Meta:
        model = Candidatura
        fields = '__all__'
