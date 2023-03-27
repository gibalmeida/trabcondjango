from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Button, Field, Layout, Submit
from crispy_forms.bootstrap import FormActions, PrependedText


from .models import Pessoa


class PessoaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Field('nome'),
            Field('data_de_nascimento'),
            PrependedText('email', '@'),
            FormActions(
                Submit('save', 'Salvar'),
                Button('cancel', 'Cancelar')
            )
        )

    class Meta:
        model = Pessoa
        fields = ['nome', 'data_de_nascimento', 'email']

        widgets = {
            # 'project_text': Textarea(attrs={'cols': 60, 'rows': 10}),
            'data_de_nascimento': forms.TextInput(attrs={'type': 'date'}),

        }
