from django import forms
from django.contrib.admin import widgets
from evro.models import PageModel
from django.contrib.admin import widgets


class DateInput(forms.DateInput):
    input_type = 'date'


class TimeInput(forms.TimeInput):
    input_type = 'time'


class PageForm(forms.ModelForm):
    class Meta:
        model = PageModel
        fields = '__all__'
        widgets = {
            'placeDTP': forms.TextInput(attrs={'class': 'input_text', 'id': 'placeDTP_id'}),
            'date': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'time': TimeInput(attrs={'class': 'date'}),
            'quantity_tc': forms.TextInput(attrs={'class': 'js_valid_num'}),
            'victims': forms.TextInput(attrs={'class': 'js_valid_num'}),
            'deaded': forms.TextInput(attrs={'class': 'js_valid_num'}),
            'drunk_yes': forms.CheckboxInput(attrs={'class': 'js_drunk'}),
            'drunk_no': forms.CheckboxInput(attrs={'class': 'js_drunk', 'cheked': True}),
            'damage_yes': forms.CheckboxInput(attrs={'class': 'js_damage'}),
            'damage_no': forms.CheckboxInput(attrs={'class': 'js_damage'}),
            'other_damage_yes': forms.CheckboxInput(attrs={'class': 'js_other_damage'}),
            'other_damage_no': forms.CheckboxInput(attrs={'class': 'js_other_damage'}),
            'withesses': forms.TextInput(
                attrs={'class': 'input_text', 'placeholder': '(фамилия, имя, отчество, адрес места жительства)'}),
            'polis_men_yes': forms.CheckboxInput(attrs={'class': 'js_polis_men'}),
            'polis_men_no': forms.CheckboxInput(attrs={'class': 'js_polis_men'}),
            'bange_number': forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'номер нагрудного знака'}),
            # "A"
            'model_a': forms.TextInput(attrs={'class': 'input_text'}),
            'number_vin_a': forms.TextInput(attrs={'class': 'input_text'}),
            'number_tc_a': forms.TextInput(attrs={'class': 'input_text'}),
            'tex_seria_a': forms.TextInput(attrs={'class': 'input_text seria', 'placeholder': 'серия'}),
            'tex_number_a': forms.TextInput(attrs={'class': 'input_text number', 'placeholder': 'номер'}),
            'owner_name_a': forms.TextInput(attrs={'class': 'input_text'}),
            'adress_a': forms.TextInput(attrs={'class': 'input_text'}),
            'driver_name_a': forms.TextInput(attrs={'class': 'input_text'}),
            'born_data_a': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'adress_driver_a': forms.TextInput(attrs={'class': 'input_text'}),
            'phone_a': forms.TextInput(attrs={'class': 'input_text'}),
            'driver_seria_a': forms.TextInput(attrs={'class': 'input_text seria', 'placeholder': 'серия'}),
            'driver_number_a': forms.TextInput(attrs={'class': 'input_text number', 'placeholder': 'номер'}),
            'category_a': forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'ABCDE'}),
            'category_date_a': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'contract_a': forms.TextInput(
                attrs={'class': 'input_text', 'placeholder': '(доверенность, договор аренды, путевойлист и т.п.)'}),
            'insurer_a': forms.TextInput(attrs={'class': 'input_text',
                                                'placeholder': '(наименование страховщика, застраховавшего ответственность)'}),
            'polis_seria_a': forms.TextInput(attrs={'class': 'input_text seria', 'placeholder': 'серия'}),
            'polis_number_a': forms.TextInput(attrs={'class': 'input_text number', 'placeholder': 'номер'}),
            'polis_date_end_a': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'damage_yes_a': forms.CheckboxInput(attrs={'class': 'js_damage_tc'}),
            'damage_no_a': forms.CheckboxInput(attrs={'class': 'js_damage_tc'}),
            'visible_damage_a': forms.TextInput(attrs={'class': 'input_text margin_left'}),
            # "B"
            'model_b': forms.TextInput(attrs={'class': 'input_text'}),
            'number_vin_b': forms.TextInput(attrs={'class': 'input_text'}),
            'number_tc_b': forms.TextInput(attrs={'class': 'input_text'}),
            'tex_seria_b': forms.TextInput(attrs={'class': 'input_text seria', 'placeholder': 'серия'}),
            'tex_number_b': forms.TextInput(attrs={'class': 'input_text number', 'placeholder': 'номер'}),
            'owner_name_b': forms.TextInput(attrs={'class': 'input_text'}),
            'adress_b': forms.TextInput(attrs={'class': 'input_text'}),
            'driver_name_b': forms.TextInput(attrs={'class': 'input_text'}),
            'born_data_b': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'adress_driver_b': forms.TextInput(attrs={'class': 'input_text'}),
            'phone_b': forms.TextInput(attrs={'class': 'input_text'}),
            'driver_seria_b': forms.TextInput(attrs={'class': 'input_text seria', 'placeholder': 'серия'}),
            'driver_number_b': forms.TextInput(attrs={'class': 'input_text number', 'placeholder': 'номер'}),
            'category_b': forms.TextInput(attrs={'class': 'input_text', 'placeholder': 'ABCDE'}),
            'category_date_b': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'contract_b': forms.TextInput(
                attrs={'class': 'input_text', 'placeholder': '(доверенность, договор аренды, путевойлист и т.п.)'}),
            'insurer_b': forms.TextInput(attrs={'class': 'input_text',
                                                'placeholder': '(наименование страховщика, застраховавшего ответственность)'}),
            'polis_seria_b': forms.TextInput(attrs={'class': 'input_text seria', 'placeholder': 'серия'}),
            'polis_number_b': forms.TextInput(attrs={'class': 'input_text number', 'placeholder': 'номер'}),
            'polis_date_end_b': DateInput(attrs={'class': 'date'}, format='%Y-%m-%d'),
            'damage_yes_b': forms.CheckboxInput(attrs={'class': 'js_damage_b_tc'}),
            'damage_no_b': forms.CheckboxInput(attrs={'class': 'js_damage_b_tc'}),
            'visible_damage_b': forms.TextInput(attrs={'class': 'input_text margin_left'}),
            'one_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'one_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'two_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'two_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'free_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'free_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'four_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'four_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'five_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'five_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'six_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'six_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'seven_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'seven_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'eigth_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'eigth_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'nine_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'nine_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'ten_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'ten_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'eleven_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'eleven_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'twelve_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'twelve_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'thirteen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'thirteen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'fourteen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'fourteen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'fiveteen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'fiveteen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'sixteen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'sixteen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'seventeen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'seventeen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'eigthteen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'eigthteen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'nineteen_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'nineteen_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'twenty_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'twenty_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'twenty_one_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'twenty_one_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'twenty_two_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'twenty_two_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'twenty_free_a': forms.CheckboxInput(attrs={'class': 'js_case_a case'}),
            'twenty_four_b': forms.CheckboxInput(attrs={'class': 'js_case_b case'}),
            'quantity_a': forms.TextInput(attrs={'class': 'quantity_case js_quantity_case_a', 'type': 'hidden'}),
            'quantity_b': forms.TextInput(attrs={'class': 'quantity_case js_quantity_case_b', 'type': 'hidden'}),
            'transport_a': forms.CheckboxInput(attrs={'class': 'js_transport'}),
            'transport_b': forms.CheckboxInput(attrs={'class': 'js_transport'}),
            'circumstances': forms.Textarea(attrs={"cols": "80", "rows": "7"}),
            'managet_owner': forms.CheckboxInput(attrs={'class': 'js_managet managet'}),
            'managet_another': forms.CheckboxInput(attrs={'class': 'js_managet managet'}),
            'photo_one': forms.FileInput(),
            'photo_two': forms.FileInput(),
            'work_auto_yes': forms.CheckboxInput(attrs={'class': 'js_work_auto work_auto'}),
            'work_auto_no': forms.CheckboxInput(attrs={'class': 'js_work_auto work_auto'}),
            'location': forms.Textarea(attrs={"cols": "80", "rows": "4"}),
            'note': forms.Textarea(attrs={"cols": "80", "rows": "4"})

        }
