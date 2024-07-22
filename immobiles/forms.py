from .models import Customer, Immobile, RegisterLocation
from django import forms

class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field_name == 'is_active':
                field.widget = forms.CheckboxInput(attrs={'class': 'sr-only'})
            else:
                field.widget.attrs.update({
                    'class': 'h-full w-full border-gray-300 px-2 transition-all border-blue rounded-sm text-xs',
                })

            field.label = self.get_custom_label(field_name)

    def get_custom_label(self, field_name):
        labels = {
            'name': 'Nome Completo',
            'email': 'E-mail',
            'phone': 'Telefone',
        }
        return labels.get(field_name, field_name.replace('_', ' ').title())

class MultipleFileInput(forms.ClearableFileInput):
  allow_multiple_selected = True

class MultipleFileField(forms.FileField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("widget", MultipleFileInput())
        super().__init__(*args, **kwargs)

    def clean(self, data, initial=None):
        single_file_clean = super().clean
        if isinstance(data, (list, tuple)):
            result = [single_file_clean(d, initial) for d in data]
        else:
            result = single_file_clean(data, initial)
        return result

class ImmobileForm(forms.ModelForm):
    immobile = MultipleFileField()
    class Meta:
        model = Immobile
        fields = '__all__'
        exclude = ('is_locate',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if field.widget.__class__ in [forms.CheckboxInput, forms.RadioSelect]:
                field.widget.attrs.update({'class': 'sr-only'})
            elif field_name == 'immobile':
                field.widget.attrs.update({
                    'class': 'hidden-input',  
                })
            else:
                additional_class = 'resize-none pt-3' if field_name == 'address' else ''
                field.widget.attrs.update({
                    'class': f'h-full w-full border-gray-300 px-2 transition-all border-blue rounded-sm text-xs {additional_class}',
                })
            
            field.label = self.get_custom_label(field_name)

    def get_custom_label(self, field_name):
        labels = {
            'address': 'Endereço',
            'code': 'Código',
            'type_item': 'Tipo do Item',
            'price': 'Preço',
        }
        return labels.get(field_name, field_name.replace('_', ' ').title())


class RegisterLocationForm(forms.ModelForm):
    dt_start = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))
    dt_end = forms.DateTimeField(widget=forms.DateInput(format='%d-%m-%Y',attrs={'type': 'date',}))

    class Meta:
        model = RegisterLocation
        fields = '__all__'
        exclude = ('immobile',)
        
    def __init__(self, *args, **kwargs): 
        super().__init__(*args, **kwargs)  
        for field_name, field in self.fields.items():   
            field.widget.attrs['class'] = 'h-full w-full border-gray-300 px-2 transition-all border-blue rounded-sm text-xs'
    
            field.label = self.get_custom_label(field_name)

    def get_custom_label(self, field_name):
        labels = {
            'client': 'Cliente',
            'dt_start': 'Data Inicial',
            'dt_end': 'Data Final',
        }
        return labels.get(field_name, field_name.replace('_', ' ').title())