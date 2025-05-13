from django import forms
from .models import Cliente, Medicamento, Compra

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'endereco', 'telefone']

class MedicamentoForm(forms.ModelForm):
  class Meta:
      model = Medicamento
      fields = ['nomeMedicamento', 'fabricante', 'preco']

class CompraForm(forms.ModelForm):
  class Meta:
      model = Compra
      fields = ['cliente', 'medicamento', 'quantidade']
