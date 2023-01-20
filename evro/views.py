from collections import namedtuple

from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views import View

from evro.forms import PageForm
from PDFMaker import main
from evro.models import PageModel

EVRO = namedtuple('EVRO', [
    'PLACE', 'DATE', 'TIME', 'QUANTITY_TC', 'VICTIMS', 'DEADED', 'DRUNK_YES', 'DRUNK_NO',
    'DAMAGE_YES', 'DAMAGE_NO', 'OTHERS_DAMAGE_YES', 'OTHERS_DAMAGE_NO',
    'POLIS_MEN_YES', 'POLIS_MEN_NO', 'BANGE_NUMBER', 'WITHESSES', 'MODEL_A', 'NUMBER_VIN_A',
    'NUMBER_TC_A', 'TEX_SERIA_A', 'TEX_NUMBER_A', 'OWNER_NAME_A', 'ADRESS_A', 'DRIVER_NAME_A',
    'BORN_DATA_A', 'ADRESS_DRIVER_A', 'PHONE_A', 'DRIVE_SERIA_A', 'DRIVE_NUMBER_A', 'CATEGORY_A',
    'CATEGORY_DATE_A', 'CONTRACT_A', 'INSURER_A', 'POLIS_SERIA_A', 'POLIS_NUMBER_A', 'POLIS_DATE_END_A',
    'DAMAGE_YES_A', 'DAMAGE_NO_A', 'VISIBLE_DAMAGE_A', 'MODEL_B', 'NUMBER_VIN_B',
    'NUMBER_TC_B', 'TEX_SERIA_B', 'TEX_NUMBER_B', 'OWNER_NAME_B', 'ADRESS_B', 'DRIVER_NAME_B',
    'BORN_DATA_B', 'ADRESS_DRIVER_B', 'PHONE_B', 'DRIVE_SERIA_B', 'DRIVE_NUMBER_B', 'CATEGORY_B',
    'CATEGORY_DATE_B', 'CONTRACT_B', 'INSURER_B', 'POLIS_SERIA_B', 'POLIS_NUMBER_B', 'POLIS_DATE_END_B',
    'DAMAGE_YES_B', 'DAMAGE_NO_B', 'VISIBLE_DAMAGE_B', 'ONE_A', 'ONE_B', 'TWO_A', 'TWO_B', 'FREE_A', 'FREE_B',
    'FOUR_A', 'FOUR_B', 'FIVE_A', 'FIVE_B', 'SIX_A', 'SIX_B', 'SEVEN_A', 'SEVEN_B', 'EIGHT_A', 'EIGHT_B', 'NINE_A',
    'NINE_B', 'TEN_A', 'TEN_B', 'ELEVEN_A', 'ELEVEN_B', 'TWELVE_A', 'TWELVE_B', 'THIRTEEN_A', 'THIRTEEN_B',
    'FOURTEEN_A', 'FOURTEEN_B', 'FIVETEEN_A', 'FIVETEEN_B', 'SIXTEEN_A', 'SIXTEEN_B', 'SEVENTEEN_A', 'SEVENTEEN_B',
    'EIGHTEEN_A', 'EIGHTEEN_B', 'NINETEEN_A', 'NINETEEN_B', 'TWENTY_A', 'TWENTY_B', 'TWENTY_ONE_A', 'TWENTY_ONE_B',
    'TWENTY_TWO_A', 'TWENTY_TWO_B', 'TWENTY_FREE_A', 'TWENTY_FOUR_B', 'QUANTITY_A', 'QUANTITY_B', 'TRANSPORT_A',
    'TRANSPORT_B', 'CIRCUMSTANCES', 'MANAGET_OWNER', 'MANAGET_ANOTHER', 'PHOTO_ONE', 'PHOTO_TWO', 'WORK_AUTO_YES',
    'WORK_AUTO_NO',
    'LOCATION', 'NOTE', 'PATH_RESULT_FILE', 'CASH_TEMPLATE_PATH'

])


class EvroView(View):

    def bool_check(self, elem):
        if elem:
            elem = "✓"
        else:
            elem = ''
        return elem

    def get(self, request):
        page = PageModel.objects.get(id=30)
        form = PageForm(instance=page)
        data = {
            'form': form,

        }
        return render(request, 'evro/evro.html', data)

    def post(self, request):
        form = PageForm(request.POST, request.FILES)

        if form.is_valid():
            place = form.cleaned_data['placeDTP']  # PLACE
            date = form.cleaned_data['date']
            date_f = date.strftime('%d.%m.%Y')  # DATE
            time = form.cleaned_data['time']
            time = time.strftime('%H:%M')  # TIME
            quantity_tc = str(form.cleaned_data['quantity_tc'])  # QUANTITY_TC
            victims = str(form.cleaned_data['victims'])  # VICTIMS
            deaded = str(form.cleaned_data['deaded'])  # DEADED
            drunk_yes = form.cleaned_data['drunk_yes']  # DRUNK_YES
            drunk_yes = self.bool_check(drunk_yes)
            drunk_no = form.cleaned_data['drunk_no']  # DRUNK_NO
            drunk_no = self.bool_check(drunk_no)
            damage_yes = form.cleaned_data['damage_yes']  # DAMAGE_YES
            damage_yes = self.bool_check(damage_yes)
            damage_no = form.cleaned_data['damage_no']  # DAMAGE_NO
            damage_no = self.bool_check(damage_no)
            other_damage_yes = form.cleaned_data['other_damage_yes']  # OTHERS_DAMAGE_YES
            other_damage_yes = self.bool_check(other_damage_yes)
            other_damage_no = form.cleaned_data['other_damage_no']  # OTHERS_DAMAGE_NO
            other_damage_no = self.bool_check(other_damage_no)
            polis_men_yes = form.cleaned_data['polis_men_yes']  # POLIS_MEN_YES
            polis_men_yes = self.bool_check(polis_men_yes)
            polis_men_no = form.cleaned_data['polis_men_no']  # POLIS_MEN_NO
            polis_men_no = self.bool_check(polis_men_no)
            bange_number = form.cleaned_data['bange_number']  # BANGE_NUMBER
            if not bange_number:
                bange_number = ''
            withesses = form.cleaned_data['withesses']  # WITHESSES
            if not withesses:
                withesses = ''
            """
            транспортное средство А
            """
            model_a = form.cleaned_data['model_a']  # MODEL_A
            number_vin_a = form.cleaned_data['number_vin_a']  # NUMBER_VIN_A
            number_tc_a = form.cleaned_data['number_tc_a']  # NUMBER_TC_A
            tex_seria_a = form.cleaned_data['tex_seria_a']  # TEX_SERIA_A
            tex_number_a = form.cleaned_data['tex_number_a']  # TEX_NUMBER_A
            owner_name_a = form.cleaned_data['owner_name_a']  # OWNER_NAME_A
            adress_a = form.cleaned_data['adress_a']  # ADRESS_A
            driver_name_a = form.cleaned_data['driver_name_a']  # DRIVER_NAME_A
            born_data_a = form.cleaned_data['born_data_a']  # BORN_DATA_A
            if born_data_a:
                born_data_a_f = born_data_a.strftime('%d.%m.%Y')
            else:
                born_data_a_f = ''
            adress_driver_a = form.cleaned_data['adress_driver_a']  # ADRESS_DRIVER_A
            phone_a = form.cleaned_data['phone_a']  # PHONE_A
            driver_seria_a = form.cleaned_data['driver_seria_a']  # DRIVE_SERIA_A
            driver_number_a = form.cleaned_data['driver_number_a']  # DRIVE_NUMBER_A
            category_a = form.cleaned_data['category_a']  # CATEGORY_A
            category_date_a = form.cleaned_data['category_date_a']  # CATEGORY_DATE_A
            category_date_a_f = category_date_a.strftime('%d.%m.%Y')
            contract_a = form.cleaned_data['contract_a']  # CONTRACT_A
            insurer_a = form.cleaned_data['insurer_a']  # INSURER_A
            polis_seria_a = form.cleaned_data['polis_seria_a']  # POLIS_SERIA_A
            polis_number_a = form.cleaned_data['polis_number_a']  # POLIS_NUMBER_A
            polis_date_end_a = form.cleaned_data['polis_date_end_a']  # POLIS_DATE_END_A
            polis_date_end_a_f = polis_date_end_a.strftime('%d.%m.%Y')
            damage_yes_a = form.cleaned_data['damage_yes_a']  # DAMAGE_YES_A
            damage_yes_a = self.bool_check(damage_yes_a)
            damage_no_a = form.cleaned_data['damage_no_a']  # DAMAGE_NO_A
            damage_no_a = self.bool_check(damage_no_a)
            visible_damage_a = form.cleaned_data['visible_damage_a']  # VISIBLE_DAMAGE_A
            if not visible_damage_a:
                visible_damage_a = ' '
            """
            транстпортное стредство B
            """
            model_b = form.cleaned_data['model_b']  # MODEL_B
            number_vin_b = form.cleaned_data['number_vin_b']  # NUMBER_VIN_B
            number_tc_b = form.cleaned_data['number_tc_b']  # NUMBER_TC_B
            tex_seria_b = form.cleaned_data['tex_seria_b']  # TEX_SERIA_B
            tex_number_b = form.cleaned_data['tex_number_b']  # TEX_NUMBER_B
            owner_name_b = form.cleaned_data['owner_name_b']  # OWNER_NAME_B
            adress_b = form.cleaned_data['adress_b']  # ADRESS_B
            driver_name_b = form.cleaned_data['driver_name_b']  # DRIVER_NAME_B
            born_data_b = form.cleaned_data['born_data_b']  # BORN_DATA_B
            if born_data_b:
                born_data_b_f = born_data_b.strftime('%d.%m.%Y')
            else:
                born_data_b_f = ''
            adress_driver_b = form.cleaned_data['adress_driver_b']  # ADRESS_DRIVER_B
            phone_b = form.cleaned_data['phone_b']  # PHONE_B
            driver_seria_b = form.cleaned_data['driver_seria_b']  # DRIVE_SERIA_B
            driver_number_b = form.cleaned_data['driver_number_b']  # DRIVE_NUMBER_B
            category_b = form.cleaned_data['category_b']  # CATEGORY_B
            category_date_b = form.cleaned_data['category_date_b']  # CATEGORY_DATE_B
            category_date_b_f = category_date_b.strftime('%d.%m.%Y')
            contract_b = form.cleaned_data['contract_b']  # CONTRACT_B
            insurer_b = form.cleaned_data['insurer_b']  # INSURER_B
            polis_seria_b = form.cleaned_data['polis_seria_b']  # POLIS_SERIA_B
            polis_number_b = form.cleaned_data['polis_number_b']  # POLIS_NUMBER_B
            polis_date_end_b = form.cleaned_data['polis_date_end_b']  # POLIS_DATE_END_B
            polis_date_end_b_f = polis_date_end_b.strftime('%d.%m.%Y')
            damage_yes_b = form.cleaned_data['damage_yes_b']  # DAMAGE_YES_B
            damage_yes_b = self.bool_check(damage_yes_b)
            damage_no_b = form.cleaned_data['damage_no_b']  # DAMAGE_NO_B
            damage_no_b = self.bool_check(damage_no_b)
            visible_damage_b = form.cleaned_data['visible_damage_b']  # VISIBLE_DAMAGE_B
            if not visible_damage_b:
                visible_damage_b = ' '
            one_a = form.cleaned_data['one_a']
            one_a = self.bool_check(one_a)
            one_b = form.cleaned_data['one_b']
            one_b = self.bool_check(one_b)
            two_a = form.cleaned_data['two_a']
            two_a = self.bool_check(two_a)
            two_b = form.cleaned_data['two_b']
            two_b = self.bool_check(two_b)
            free_a = form.cleaned_data['free_a']
            free_a = self.bool_check(free_a)
            free_b = form.cleaned_data['free_b']
            free_b = self.bool_check(free_b)
            four_a = form.cleaned_data['four_a']
            four_a = self.bool_check(four_a)
            four_b = form.cleaned_data['four_b']
            four_b = self.bool_check(four_b)
            five_a = form.cleaned_data['five_a']
            five_a = self.bool_check(five_a)
            five_b = form.cleaned_data['five_b']
            five_b = self.bool_check(five_b)
            six_a = form.cleaned_data['six_a']
            six_a = self.bool_check(six_a)
            six_b = form.cleaned_data['six_b']
            six_b = self.bool_check(six_b)
            seven_a = form.cleaned_data['seven_a']
            seven_a = self.bool_check(seven_a)
            seven_b = form.cleaned_data['seven_b']
            seven_b = self.bool_check(seven_b)
            eigth_a = form.cleaned_data['eigth_a']
            eigth_a = self.bool_check(eigth_a)
            eigth_b = form.cleaned_data['eigth_b']
            eigth_b = self.bool_check(eigth_b)
            nine_a = form.cleaned_data['nine_a']
            nine_a = self.bool_check(nine_a)
            nine_b = form.cleaned_data['nine_b']
            nine_b = self.bool_check(nine_b)
            ten_a = form.cleaned_data['ten_a']
            ten_a = self.bool_check(ten_a)
            ten_b = form.cleaned_data['ten_b']
            ten_b = self.bool_check(ten_b)
            eleven_a = form.cleaned_data['eleven_a']
            eleven_a = self.bool_check(eleven_a)
            eleven_b = form.cleaned_data['eleven_b']
            eleven_b = self.bool_check(eleven_b)
            twelve_a = form.cleaned_data['twelve_a']
            twelve_a = self.bool_check(twelve_a)
            twelve_b = form.cleaned_data['twelve_b']
            twelve_b = self.bool_check(twelve_b)
            thirteen_a = form.cleaned_data['thirteen_a']
            thirteen_a = self.bool_check(thirteen_a)
            thirteen_b = form.cleaned_data['thirteen_b']
            thirteen_b = self.bool_check(thirteen_b)
            fourteen_a = form.cleaned_data['fourteen_a']
            fourteen_a = self.bool_check(fourteen_a)
            fourteen_b = form.cleaned_data['fourteen_b']
            fourteen_b = self.bool_check(fourteen_b)
            fiveteen_a = form.cleaned_data['fiveteen_a']
            fiveteen_a = self.bool_check(fiveteen_a)
            fiveteen_b = form.cleaned_data['fiveteen_b']
            fiveteen_b = self.bool_check(fiveteen_b)
            sixteen_a = form.cleaned_data['sixteen_a']
            sixteen_a = self.bool_check(sixteen_a)
            sixteen_b = form.cleaned_data['sixteen_b']
            sixteen_b = self.bool_check(sixteen_b)
            seventeen_a = form.cleaned_data['seventeen_a']
            seventeen_a = self.bool_check(seventeen_a)
            seventeen_b = form.cleaned_data['seventeen_b']
            seventeen_b = self.bool_check(seventeen_b)
            eigthteen_a = form.cleaned_data['eigthteen_a']
            eigthteen_a = self.bool_check(eigthteen_a)
            eigthteen_b = form.cleaned_data['eigthteen_b']
            eigthteen_b = self.bool_check(eigthteen_b)
            nineteen_a = form.cleaned_data['nineteen_a']
            nineteen_a = self.bool_check(nineteen_a)
            nineteen_b = form.cleaned_data['nineteen_b']
            nineteen_b = self.bool_check(nineteen_b)
            twenty_a = form.cleaned_data['twenty_a']
            twenty_a = self.bool_check(twenty_a)
            twenty_b = form.cleaned_data['twenty_b']
            twenty_b = self.bool_check(twenty_b)
            twenty_one_a = form.cleaned_data['twenty_one_a']
            twenty_one_a = self.bool_check(twenty_one_a)
            twenty_one_b = form.cleaned_data['twenty_one_b']
            twenty_one_b = self.bool_check(twenty_one_b)
            twenty_two_a = form.cleaned_data['twenty_two_a']
            twenty_two_a = self.bool_check(twenty_two_a)
            twenty_two_b = form.cleaned_data['twenty_two_b']
            twenty_two_b = self.bool_check(twenty_two_b)
            twenty_free_a = form.cleaned_data['twenty_free_a']
            twenty_free_a = self.bool_check(twenty_free_a)
            twenty_four_b = form.cleaned_data['twenty_four_b']
            twenty_four_b = self.bool_check(twenty_four_b)
            quantity_a = form.cleaned_data['quantity_a']
            quantity_b = form.cleaned_data['quantity_b']
            managet_owner = form.cleaned_data['managet_owner']
            managet_owner = self.bool_check(managet_owner)
            managet_another = form.cleaned_data['managet_another']
            managet_another = self.bool_check(managet_another)

            """
            второй лист
            """

            transport_a = form.cleaned_data['transport_a']
            transport_a = self.bool_check(transport_a)
            transport_b = form.cleaned_data['transport_b']
            transport_b = self.bool_check(transport_b)
            circumstances = form.cleaned_data['circumstances']
            work_auto_yes = form.cleaned_data['work_auto_yes']
            work_auto_yes = self.bool_check(work_auto_yes)
            work_auto_no = form.cleaned_data['work_auto_no']
            work_auto_no = self.bool_check(work_auto_no)
            location = form.cleaned_data['location']
            note = form.cleaned_data['note']
            obj = form.save()
            result = EVRO(
                PLACE=place,
                DATE=date_f,
                TIME=time,
                QUANTITY_TC=quantity_tc,
                VICTIMS=victims,
                DEADED=deaded,
                DRUNK_YES=drunk_yes,
                DRUNK_NO=drunk_no,
                DAMAGE_YES=damage_yes,
                DAMAGE_NO=damage_no,
                OTHERS_DAMAGE_YES=other_damage_yes,
                OTHERS_DAMAGE_NO=other_damage_no,
                POLIS_MEN_YES=polis_men_yes,
                POLIS_MEN_NO=polis_men_no,
                BANGE_NUMBER=bange_number,
                WITHESSES=withesses,

                MODEL_A=model_a,
                NUMBER_VIN_A=number_vin_a,
                NUMBER_TC_A=number_tc_a,
                TEX_SERIA_A=tex_seria_a,
                TEX_NUMBER_A=tex_number_a,
                OWNER_NAME_A=owner_name_a,
                ADRESS_A=adress_a,
                DRIVER_NAME_A=driver_name_a,
                BORN_DATA_A=born_data_a_f,
                ADRESS_DRIVER_A=adress_driver_a,
                PHONE_A=phone_a,
                DRIVE_SERIA_A=driver_seria_a,
                DRIVE_NUMBER_A=driver_number_a,
                CATEGORY_A=category_a,
                CATEGORY_DATE_A=category_date_a_f,
                CONTRACT_A=contract_a,
                INSURER_A=insurer_a,
                POLIS_SERIA_A=polis_seria_a,
                POLIS_NUMBER_A=polis_number_a,
                POLIS_DATE_END_A=polis_date_end_a_f,
                DAMAGE_YES_A=damage_yes_a,
                DAMAGE_NO_A=damage_no_a,
                VISIBLE_DAMAGE_A=visible_damage_a,

                MODEL_B=model_b,
                NUMBER_VIN_B=number_vin_b,
                NUMBER_TC_B=number_tc_b,
                TEX_SERIA_B=tex_seria_b,
                TEX_NUMBER_B=tex_number_b,
                OWNER_NAME_B=owner_name_b,
                ADRESS_B=adress_b,
                DRIVER_NAME_B=driver_name_b,
                BORN_DATA_B=born_data_b_f,
                ADRESS_DRIVER_B=adress_driver_b,
                PHONE_B=phone_b,
                DRIVE_SERIA_B=driver_seria_b,
                DRIVE_NUMBER_B=driver_number_b,
                CATEGORY_B=category_b,
                CATEGORY_DATE_B=category_date_b_f,
                CONTRACT_B=contract_b,
                INSURER_B=insurer_b,
                POLIS_SERIA_B=polis_seria_b,
                POLIS_NUMBER_B=polis_number_b,
                POLIS_DATE_END_B=polis_date_end_b_f,
                DAMAGE_YES_B=damage_yes_b,
                DAMAGE_NO_B=damage_no_b,
                VISIBLE_DAMAGE_B=visible_damage_b,

                ONE_A=one_a,
                ONE_B=one_b,
                TWO_A=two_a,
                TWO_B=two_b,
                FREE_A=free_a,
                FREE_B=free_b,
                FOUR_A=four_a,
                FOUR_B=four_b,
                FIVE_A=five_a,
                FIVE_B=five_b,
                SIX_A=six_a,
                SIX_B=six_b,
                SEVEN_A=seven_a,
                SEVEN_B=seven_b,
                EIGHT_A=eigth_a,
                EIGHT_B=eigth_b,
                NINE_A=nine_a,
                NINE_B=nine_b,
                TEN_A=ten_a,
                TEN_B=ten_b,
                ELEVEN_A=eleven_a,
                ELEVEN_B=eleven_b,
                TWELVE_A=twelve_a,
                TWELVE_B=twelve_b,
                THIRTEEN_A=thirteen_a,
                THIRTEEN_B=thirteen_b,
                FOURTEEN_A=fourteen_a,
                FOURTEEN_B=fourteen_b,
                FIVETEEN_A=fiveteen_a,
                FIVETEEN_B=fiveteen_b,
                SIXTEEN_A=sixteen_a,
                SIXTEEN_B=sixteen_b,
                SEVENTEEN_A=seventeen_a,
                SEVENTEEN_B=seventeen_b,
                EIGHTEEN_A=eigthteen_a,
                EIGHTEEN_B=eigthteen_b,
                NINETEEN_A=nineteen_a,
                NINETEEN_B=nineteen_b,
                TWENTY_A=twenty_a,
                TWENTY_B=twenty_b,
                TWENTY_ONE_A=twenty_one_a,
                TWENTY_ONE_B=twenty_one_b,
                TWENTY_TWO_A=twenty_two_a,
                TWENTY_TWO_B=twenty_two_b,
                TWENTY_FREE_A=twenty_free_a,
                TWENTY_FOUR_B=twenty_four_b,
                QUANTITY_A=quantity_a,
                QUANTITY_B=quantity_b,

                TRANSPORT_A=transport_a,
                TRANSPORT_B=transport_b,
                CIRCUMSTANCES=circumstances,
                MANAGET_OWNER=managet_owner,
                MANAGET_ANOTHER=managet_another,
                PHOTO_ONE=str(obj.photo_one),
                PHOTO_TWO=str(obj.photo_two),
                WORK_AUTO_YES=work_auto_yes,
                WORK_AUTO_NO=work_auto_no,
                LOCATION=location,
                NOTE=note,
                PATH_RESULT_FILE=str(f"{obj.id}_evro.pdf"),
                CASH_TEMPLATE_PATH=str(f"{obj.id}_new.pdf")
            )
            filePath = main(result)
            fsock = open(filePath, "rb")
            response = HttpResponse(fsock, content_type='application/pdf')
            response['Content-Disposition'] = f'attachment; filename={obj.id}_evro.pdf'
            return response

        return render(request, 'evro/evro.html', context={'form': form})
