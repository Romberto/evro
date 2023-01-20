import os

from django.http import FileResponse
from fpdf import FPDF
from PyPDF2 import PdfFileWriter, PdfFileReader, PdfMerger
from io import BytesIO


def main(result):
    CASH_TEMPLATE_PATH = f'result/{result.CASH_TEMPLATE_PATH}'
    pdf = FPDF(orientation='P', unit='mm', format='A4')
    pdf.add_page()
    pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf.set_font("DejaVu", size=8)
    pdf.cell(20, 15, ln=1)
    """
    1. строка
    """
    PLACE = result.PLACE
    pdf.cell(22, 5)
    pdf.cell(170, 5, txt=f"{PLACE}", ln=1)
    """
     2. строка
    """
    pdf.cell(22, 6)
    DATE = result.DATE
    TIME = result.TIME
    QUANTITY_TC = result.QUANTITY_TC
    pdf.set_font("DejaVu", size=8)
    for i in DATE:
        pdf.cell(2.8, 10, txt=f"{i}")
    pdf.cell(2.1, 8)
    for i in TIME:
        pdf.cell(2.8, 10, txt=f"{i}")
    pdf.cell(56, 6)
    pdf.set_font("DejaVu", size=10)
    pdf.cell(2, 10, txt=f"{QUANTITY_TC}", ln=1)
    """
    3. строка
    """
    VICTIMS = result.VICTIMS
    DEADED = result.DEADED
    pdf.cell(100, 2)
    pdf.cell(2, 2, txt=f"{VICTIMS}")
    pdf.cell(20, 2)
    pdf.cell(2, 2, txt=f"{DEADED}", ln=1)
    """
    4. строка
    """
    DRUNK_YES = result.DRUNK_YES
    DRUNK_NO = result.DRUNK_NO
    pdf.cell(109, 8)
    pdf.cell(2, 8, txt=f"{DRUNK_YES}")
    pdf.cell(9, 8)
    pdf.cell(2, 8, txt=f"{DRUNK_NO}", ln=1)

    """
    5. строка
    """
    DAMAGE_YES = result.DAMAGE_YES
    DAMAGE_NO = result.DAMAGE_NO
    OTHERS_DAMAGE_YES = result.OTHERS_DAMAGE_YES
    OTHERS_DAMAGE_NO = result.OTHERS_DAMAGE_NO
    pdf.cell(115, 5)
    pdf.cell(2, 5, txt=f"{DAMAGE_YES}")
    pdf.cell(8, 5)
    pdf.cell(2, 5, txt=f"{DAMAGE_NO}")
    pdf.cell(43, 5)
    pdf.cell(2, 5, txt=f"{OTHERS_DAMAGE_YES}")
    pdf.cell(7, 5)
    pdf.cell(2, 5, txt=f"{OTHERS_DAMAGE_NO}", ln=1)

    """
    6.строка
    """
    WITHESSES = result.WITHESSES

    pdf.cell(25, 4)
    top = pdf.y
    offset = pdf.x + 170
    pdf.multi_cell(170, 5,
                   f"{WITHESSES}", )
    pdf.y = top
    pdf.x = offset
    pdf.cell(0.1, 10, ln=1)

    """
    7.строка
    """
    POLIS_MEN_YES = result.POLIS_MEN_YES
    POLIS_MEN_NO = result.POLIS_MEN_NO
    BANGE_NUMBER = result.BANGE_NUMBER
    pdf.cell(115, 7)
    pdf.cell(5, 7, txt=f"{POLIS_MEN_NO}")
    pdf.cell(7, 7)
    pdf.cell(5, 7, txt=f"{POLIS_MEN_YES}")
    pdf.cell(8, 7)
    pdf.cell(35, 7, txt=f"{BANGE_NUMBER}", ln=1)
    """
    8.строка
    """
    pdf.cell(180, 7, ln=1)
    """
    9.строка
    """
    MODEL_A = result.MODEL_A
    MODEL_B = result.MODEL_B
    ONE_A = result.ONE_A
    ONE_B = result.ONE_B
    pdf.cell(29, 7)
    pdf.set_font("DejaVu", size=6)
    top = pdf.y
    offset = pdf.x + 35
    pdf.multi_cell(35, 3, f'{MODEL_A}')
    pdf.y = top
    pdf.x = offset

    pdf.set_font("DejaVu", size=15)
    pdf.cell(3, 6, "", )
    pdf.cell(4, 4, f"{ONE_A}")
    pdf.cell(52, 4, "")
    pdf.cell(4, 4, f"{ONE_B}")
    pdf.cell(29, 7)
    pdf.set_font("DejaVu", size=6)

    top = pdf.y
    offset = pdf.x + 35
    pdf.multi_cell(35, 3, f'{MODEL_B}')
    pdf.y = top
    pdf.x = offset
    pdf.cell(0.5, 3, '', ln=1)
    pdf.set_font("DejaVu", size=15)
    """
    10.строка
    """
    TWO_A = result.TWO_A
    TWO_B = result.TWO_B
    pdf.cell(67, 8)
    pdf.cell(4, 8.5, f"{TWO_A}")
    pdf.cell(52, 8.5, "")
    pdf.cell(4, 8.5, f"{TWO_B}")
    pdf.cell(67, 8, ln=1)
    """
    11.строка
    """
    NUMBER_VIN_A = result.NUMBER_VIN_A
    NUMBER_VIN_B = result.NUMBER_VIN_B
    FREE_A = result.FREE_A
    FREE_B = result.FREE_B
    pdf.cell(4.6, 4.5)
    pdf.set_font("DejaVu", size=8)
    for i in NUMBER_VIN_A:
        pdf.cell(2.8, 4.7, txt=f"{i}")
    if len(NUMBER_VIN_A) < 17:
        range_num = 17 - len(NUMBER_VIN_A)
        for i in range(range_num):
            pdf.cell(2.8, 4.7, txt=" ")
    pdf.cell(15, 4)
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 4, f"{FREE_A}")
    pdf.cell(52, 4, "")
    pdf.cell(4, 4, f"{FREE_B}")
    pdf.cell(4, 4)
    pdf.set_font("DejaVu", size=8)
    for i in NUMBER_VIN_B:
        pdf.cell(2.8, 4.7, txt=f"{i}")
    if len(NUMBER_VIN_B) < 17:
        range_num = 17 - len(NUMBER_VIN_B)
        for i in range(range_num):
            pdf.cell(2.8, 4.7, txt=" ")
    pdf.cell(0.1, 4, ln=1)
    """
    12.строка
    """
    NUMBER_TC_A = result.NUMBER_TC_A
    NUMBER_TC_B = result.NUMBER_TC_B
    FOUR_A = result.FOUR_A
    FOUR_B = result.FOUR_B
    pdf.cell(39.5, 4.5)
    for i in NUMBER_TC_A:
        pdf.cell(2.65, 5, txt=f"{i}")
    if len(NUMBER_TC_A) < 9:
        range_num = 9 - len(NUMBER_TC_A)
        for i in range(range_num):
            pdf.cell(2.65, 5, txt=" ")
    pdf.cell(4, 4)
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 4, f"{FOUR_A}")
    pdf.cell(52, 4, "")
    pdf.cell(4, 4, f"{FOUR_B}")
    pdf.cell(38.5, 4)
    pdf.set_font("DejaVu", size=8)
    for i in NUMBER_TC_B:
        pdf.cell(2.65, 5, txt=f"{i}")
    if len(NUMBER_TC_B) < 9:
        range_num = 9 - len(NUMBER_TC_B)
        for i in range(range_num):
            pdf.cell(2.65, 5, txt=" ")
    pdf.cell(2, 4, ln=1)
    """
    13.строка
    """
    pdf.cell(33.9, 4.5)
    TEX_SERIA_A = result.TEX_SERIA_A
    TEX_NUMBER_A = result.TEX_NUMBER_A
    TEX_SERIA_B = result.TEX_SERIA_B
    TEX_NUMBER_B = result.TEX_NUMBER_B
    FIVE_A = result.FIVE_A
    FIVE_B = result.FIVE_B
    pdf.set_font("DejaVu", size=7)
    for i in TEX_SERIA_A:
        pdf.cell(2.78, 5, txt=f"{i}")
    pdf.cell(1.8, 4.5)
    for i in TEX_NUMBER_A:
        pdf.cell(2.78, 5, txt=f"{i}")
    pdf.cell(4, 4)
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 8, f"{FIVE_A}")
    pdf.cell(52, 8, "")
    pdf.cell(4, 8, f"{FIVE_B}")
    pdf.cell(33, 6)
    pdf.set_font("DejaVu", size=7)
    for i in TEX_SERIA_B:
        pdf.cell(2.78, 5, txt=f"{i}")
    pdf.cell(1.8, 4.5)
    for i in TEX_NUMBER_B:
        pdf.cell(2.78, 5, txt=f"{i}")
    pdf.cell(2, 4, ln=1)
    """
    14.строка
    """
    SIX_A = result.SIX_A
    SIX_B = result.SIX_B
    pdf.cell(67, 7, '')
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 11, f"{SIX_A}")
    pdf.cell(52, 8, "")
    pdf.cell(4, 11, f"{SIX_B}")
    pdf.cell(67, 7, '', ln=1)
    """
    15.строка
    """
    SEVEN_A = result.SEVEN_A
    SEVEN_B = result.SEVEN_B
    OWNER_NAME_A = result.OWNER_NAME_A
    OWNER_NAME_B = result.OWNER_NAME_B
    pdf.set_font("DejaVu", size=8)
    pdf.cell(8, 6, '')
    pdf.cell(58, 6, f"{OWNER_NAME_A}")
    pdf.cell(1.5, 5, '')
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 5, f"{SEVEN_A}")
    pdf.cell(52, 5, "")
    pdf.cell(4, 5, f"{SEVEN_B}")
    pdf.cell(2, 5, "")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(65, 6, f'{OWNER_NAME_B}', ln=1)
    pdf.set_font("DejaVu", size=10)
    """
    16.строка
    """
    EIGHT_A = result.EIGHT_A
    EIGHT_B = result.EIGHT_B
    ADRESS_A = result.ADRESS_A
    ADRESS_B = result.ADRESS_B
    pdf.cell(13, 8, "")
    top = pdf.y
    offset = pdf.x + 52
    pdf.set_font("DejaVu", size=6)
    pdf.set_fill_color(255, 255, 255)
    pdf.multi_cell(52, 4, f'{ADRESS_A}', fill=True)
    pdf.y = top
    pdf.x = offset
    pdf.cell(1.7, 8, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 2, f"{EIGHT_A}")
    pdf.cell(52, 5, "")
    pdf.cell(4, 2, f"{EIGHT_B}")
    pdf.cell(12, 8, "")
    pdf.set_font("DejaVu", size=6)
    top = pdf.y
    offset = pdf.x + 54
    pdf.multi_cell(54, 4, f'{ADRESS_B}', fill=True)
    pdf.y = top
    pdf.x = offset
    pdf.cell(0.1, 8, "", ln=1)
    """
    17.строка
    """
    NINE_A = result.NINE_A
    NINE_B = result.NINE_B
    pdf.cell(67.5, 4.5, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, -5, f"{NINE_A}")
    pdf.cell(52, 5, "")
    pdf.cell(4, -5, f"{NINE_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(67.5, 4.5, "", ln=1)
    """
    18.строка
    """
    TEN_A = result.TEN_A
    TEN_B = result.TEN_B
    pdf.cell(67.5, 1, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 0, f"{TEN_A}")
    pdf.cell(52, 0, "")
    pdf.cell(4, 0, f"{TEN_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(67.5, 1, "", ln=1)

    """
     19.строка
    """
    DRIVER_NAME_A = result.DRIVER_NAME_A
    DRIVER_NAME_B = result.DRIVER_NAME_B
    pdf.cell(8, 5, '')
    pdf.cell(57, 5, f"{DRIVER_NAME_A}")
    pdf.cell(65, 5, "")
    pdf.cell(65, 5, f"{DRIVER_NAME_B}", ln=1)

    """
    20.строка
    """
    BORN_DATA_A = result.BORN_DATA_A
    BORN_DATA_B = result.BORN_DATA_B
    ELEVEN_A = result.ELEVEN_A
    ELEVEN_B = result.ELEVEN_B
    pdf.cell(35, 6, '')
    for i in BORN_DATA_A:
        pdf.cell(2.78, 6, txt=f"{i}")
    pdf.cell(4.8, 5)
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 5, f"{ELEVEN_A}")
    pdf.cell(52, 5, "")
    pdf.cell(4, 5, f"{ELEVEN_B}")
    pdf.cell(34, 5, "")
    pdf.set_font("DejaVu", size=8)
    for i in BORN_DATA_B:
        pdf.cell(2.78, 6, txt=f"{i}")
    pdf.cell(2, 5, ln=1)

    """
    21.строка
    """
    ADRESS_DRIVER_A = result.ADRESS_DRIVER_A
    ADRESS_DRIVER_B = result.ADRESS_DRIVER_B
    TWELVE_A = result.TWELVE_A
    TWELVE_B = result.TWELVE_B

    pdf.cell(12, 9, "")
    top = pdf.y
    offset = pdf.x + 53
    pdf.set_font("DejaVu", size=6)
    pdf.multi_cell(53, 4.5, f'{ADRESS_DRIVER_A}', fill=True)
    pdf.y = top
    pdf.x = offset
    pdf.cell(1.5, 9, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(2, 14, f"{TWELVE_A}", )
    pdf.cell(54, 5, "")
    pdf.cell(4, 14, f"{TWELVE_B}")
    pdf.cell(12.5, 9, "")
    pdf.set_font("DejaVu", size=6)
    top = pdf.y
    offset = pdf.x + 54
    pdf.multi_cell(54, 4.5, f'{ADRESS_DRIVER_B}', fill=True)
    pdf.y = top
    pdf.x = offset
    pdf.cell(0.1, 9, "", ln=1)

    """
    22.строка
    """
    PHONE_A = result.PHONE_A
    PHONE_B = result.PHONE_B
    THIRTEEN_A = result.THIRTEEN_A
    THIRTEEN_B = result.THIRTEEN_B
    pdf.cell(20.8, 6, "")
    pdf.set_font("DejaVu", size=8)
    if PHONE_A:
        for i in PHONE_A:
            pdf.cell(2.78, 6.5, txt=f"{i}")
        if len(PHONE_A) < 15:
            range_num = 15 - len(PHONE_A)
            for i in range(range_num):
                pdf.cell(2.78, 6.5, txt=" ")
    else:
        for i in range(15):
            pdf.cell(2.78, 6.5, txt=" ")
    pdf.cell(5, 6, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 6, f"{THIRTEEN_A}")
    pdf.cell(52, 6, "")
    pdf.cell(4, 6, f"{THIRTEEN_B}")
    pdf.cell(20, 6, "")
    pdf.set_font("DejaVu", size=8)
    if PHONE_B:
        for i in PHONE_B:
            pdf.cell(2.78, 6.5, txt=f"{i}")
        if len(PHONE_B) < 15:
            range_num = 15 - len(PHONE_B)
            for i in range(range_num):
                pdf.cell(2.78, 6.5, txt=" ")
    else:
        for i in range(15):
            pdf.cell(2.78, 6.5, txt=" ")
    pdf.cell(2, 6, "", ln=1)
    """
        водительское удостоверение
    """
    DRIVE_SERIA_A = result.DRIVE_SERIA_A
    DRIVE_NUMBER_A = result.DRIVE_NUMBER_A
    DRIVE_SERIA_B = result.DRIVE_SERIA_B
    DRIVE_NUMBER_B = result.DRIVE_NUMBER_B
    FOURTEEN_A = result.FOURTEEN_A
    FOURTEEN_B = result.FOURTEEN_B
    pdf.cell(33.3, 3, "")
    pdf.set_font("DejaVu", size=8)
    for i in DRIVE_SERIA_A:
        pdf.cell(2.78, 3, txt=f"{i}")
    pdf.cell(1.8, 3, '')
    for i in DRIVE_NUMBER_A:
        pdf.cell(2.78, 3, txt=f"{i}")
    pdf.cell(4.6, 3, '')
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 3, f"{FOURTEEN_A}")
    pdf.cell(52, 3, "")
    pdf.cell(4, 3, f"{FOURTEEN_B}")
    pdf.cell(32.5, 3, "")
    pdf.set_font("DejaVu", size=8)
    for i in DRIVE_SERIA_B:
        pdf.cell(2.78, 3, txt=f"{i}")
    pdf.cell(1.8, 3, '')
    for i in DRIVE_NUMBER_B:
        pdf.cell(2.78, 3, txt=f"{i}")
    pdf.cell(2, 3, "", ln=1)
    """
    24.строка
    """
    FIVETEEN_A = result.FIVETEEN_A
    FIVETEEN_B = result.FIVETEEN_B
    pdf.cell(67.5, 4.3, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 4.3, f"{FIVETEEN_A}")
    pdf.cell(52, 4.3, "")
    pdf.cell(4, 4.3, f"{FIVETEEN_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(67.5, 4.3, "", ln=1)
    """
    25.строка
    """
    CATEGORY_A = result.CATEGORY_A
    CATEGORY_DATE_A = result.CATEGORY_DATE_A
    CATEGORY_B = result.CATEGORY_B
    CATEGORY_DATE_B = result.CATEGORY_DATE_B
    SIXTEEN_A = result.SIXTEEN_A
    SIXTEEN_B = result.SIXTEEN_B
    pdf.cell(21, 3.7, "")
    pdf.cell(11.5, 3.7, txt=f"{CATEGORY_A}", align='C')
    pdf.cell(2.6, 3.7, "")
    for i in CATEGORY_DATE_A:
        pdf.cell(2.78, 3.7, txt=f"{i}")
    pdf.cell(4, 3.7, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 4, f"{SIXTEEN_A}")
    pdf.cell(52, 4, "")
    pdf.cell(4, 4, f"{SIXTEEN_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(21, 3.7, "")
    pdf.cell(11.5, 3.7, txt=f"{CATEGORY_B}", align='C')
    pdf.cell(2.6, 3.7, "")
    for i in CATEGORY_DATE_B:
        pdf.cell(2.78, 3.7, txt=f"{i}")
    pdf.cell(0.5, 3.7, "", ln=1)
    """
    26.строка
    """
    SEVENTEEN_A = result.SEVENTEEN_A
    SEVENTEEN_B = result.SEVENTEEN_B

    pdf.cell(67.5, 3.5, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 5, f"{SEVENTEEN_A}")
    pdf.cell(52, 5, "")
    pdf.cell(4, 5, f"{SEVENTEEN_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(67.5, 3.5, "", ln=1)
    """
    27.строка
    """
    CONTRACT_A = result.CONTRACT_A
    CONTRACT_B = result.CONTRACT_B
    EIGHTEEN_A = result.EIGHTEEN_A
    EIGHTEEN_B = result.EIGHTEEN_B
    pdf.cell(26, 5, "")
    pdf.cell(38, 6, f"{CONTRACT_A}", align='C')
    pdf.cell(3, 5, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 4, f"{EIGHTEEN_A}")
    pdf.cell(52, 4, "")
    pdf.cell(4, 4, f"{EIGHTEEN_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(26, 5, "")
    pdf.cell(38, 6, f"{CONTRACT_B}", align='C')
    pdf.cell(0.5, 5, "", ln=1)
    """
    28.строка
    """
    NINETEEN_A = result.NINETEEN_A
    NINETEEN_B = result.NINETEEN_B
    pdf.cell(67.5, 6, "")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 13, f"{NINETEEN_A}")
    pdf.cell(52, 7, "")
    pdf.cell(4, 13, f"{NINETEEN_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(67.5, 6, "", ln=1)
    """
    28.строка
    """
    TWENTY_A = result.TWENTY_A
    TWENTY_B = result.TWENTY_B
    INSURER_A = result.INSURER_A
    INSURER_B = result.INSURER_B
    pdf.cell(67.5, 5, f"{INSURER_A}", align="C")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 9, f"{TWENTY_A}")
    pdf.cell(52, 9, "")
    pdf.cell(4, 9, f"{TWENTY_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(67.5, 5, f"{INSURER_B}", align="C", ln=1)
    """
    28.строка
    """
    TWENTY_ONE_A = result.TWENTY_ONE_A
    TWENTY_ONE_B = result.TWENTY_ONE_B
    POLIS_SERIA_A = result.POLIS_SERIA_A
    POLIS_NUMBER_A = result.POLIS_NUMBER_A
    POLIS_SERIA_B = result.POLIS_SERIA_B
    POLIS_NUMBER_B = result.POLIS_NUMBER_B
    pdf.cell(24.5, 10, "")
    for i in POLIS_SERIA_A:
        pdf.cell(2.78, 11, txt=f"{i}", align='C')
    if len(POLIS_SERIA_A) < 3:
        range_num = 3 - len(POLIS_SERIA_A)
        for i in range(range_num):
            pdf.cell(2.78, 11, txt=" ", align='C')
    pdf.cell(2.9, 10, txt="", align='C')
    for i in POLIS_NUMBER_A:
        pdf.cell(2.78, 11, txt=f"{i}", align='C')
    if len(POLIS_NUMBER_A) < 10:
        range_num = 10 - len(POLIS_NUMBER_A)
        for i in range(range_num):
            pdf.cell(2.78, 11, txt=" ", align='C')
    pdf.cell(4, 10, txt="")
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 10, f"{TWENTY_ONE_A}")
    pdf.cell(52, 10, "")
    pdf.cell(4, 10, f"{TWENTY_ONE_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(23.5, 10, "")
    for i in POLIS_SERIA_B:
        pdf.cell(2.78, 11, txt=f"{i}", align='C')
    if len(POLIS_SERIA_B) < 3:
        range_num = 3 - len(POLIS_SERIA_B)
        for i in range(range_num):
            pdf.cell(2.78, 11, txt=" ", align='C')
    pdf.cell(2.9, 10, txt="", align='C')
    for i in POLIS_NUMBER_B:
        pdf.cell(2.78, 11, txt=f"{i}", align='C')
    if len(POLIS_NUMBER_B) < 10:
        range_num = 10 - len(POLIS_NUMBER_B)
        for i in range(range_num):
            pdf.cell(2.78, 11, txt=" ", align='C')
    pdf.cell(23.5, 10, "", ln=1)
    """
    29.строка
    """
    TWENTY_TWO_A = result.TWENTY_TWO_A
    TWENTY_TWO_B = result.TWENTY_TWO_B
    POLIS_DATE_END_A = result.POLIS_DATE_END_A
    POLIS_DATE_END_B = result.POLIS_DATE_END_B
    pdf.cell(35.5, 5, "")
    for i in POLIS_DATE_END_A:
        pdf.cell(2.78, 6, txt=f"{i}", align='C')
    pdf.cell(3.5, 5, txt="", align='C')
    pdf.set_font("DejaVu", size=15)
    pdf.cell(4, 4, f"{TWENTY_TWO_A}")
    pdf.cell(52, 5, "")
    pdf.cell(4, 4, f"{TWENTY_TWO_B}")
    pdf.set_font("DejaVu", size=8)
    pdf.cell(35.5, 5, "")
    for i in POLIS_DATE_END_B:
        pdf.cell(2.78, 6, txt=f"{i}", align='C')
    pdf.cell(0.1, 5, "", ln=1)
    """
    30.строка страховка от ущерба
    """
    TWENTY_FREE_A = result.TWENTY_FREE_A
    DAMAGE_YES_A = result.DAMAGE_YES_A
    DAMAGE_NO_A = result.DAMAGE_NO_A

    DAMAGE_YES_B = result.DAMAGE_YES_B
    DAMAGE_NO_B = result.DAMAGE_NO_B
    pdf.set_font("DejaVu", size=15)
    pdf.cell(43.5, 7, "")
    pdf.cell(2.8, 7, f"{DAMAGE_NO_A}", align='C')
    pdf.cell(9, 7, "")
    pdf.cell(2.8, 7, f"{DAMAGE_YES_A}", align='C')
    pdf.cell(9.9, 7, "")
    pdf.cell(2.8, 5, f"{TWENTY_FREE_A}", align='C')
    pdf.cell(99, 7, "")
    pdf.cell(2.8, 7, f"{DAMAGE_NO_B}", align='C')
    pdf.cell(9, 7, "")
    pdf.cell(2.8, 7, f"{DAMAGE_YES_B}", align='C')
    pdf.cell(9, 7, "", ln=1)
    """
    30.строка страховка от ущерба
    """
    TWENTY_FOUR_B = result.TWENTY_FOUR_B
    pdf.cell(124, 4, "")
    pdf.cell(2.8, 5, f"{TWENTY_FOUR_B}", align='C')
    pdf.cell(0.1, 4, "", ln=1)

    """
    30.строка страховка от ущерба
    """
    QUANTITY_A = result.QUANTITY_A
    QUANTITY_B = result.QUANTITY_B
    pdf.cell(68, 13, "")
    pdf.set_font("DejaVu", size=12)
    pdf.cell(6, 13, f"{QUANTITY_A}", align='C')
    pdf.cell(47, 13, "")
    pdf.cell(6, 13, f"{QUANTITY_B}", align='C')
    pdf.cell(30, 13, "", ln=1)
    """
    31.строка страховка от ущерба
    """
    pdf.cell(180, 21, "", ln=1)
    """
    31.строка страховка от ущерба
    """

    VISIBLE_DAMAGE_A = result.VISIBLE_DAMAGE_A
    VISIBLE_DAMAGE_B = result.VISIBLE_DAMAGE_B

    pdf.set_font('DejaVu', size=8)
    pdf.cell(4, 3, "")
    top = pdf.y
    offset = pdf.x + 50
    pdf.multi_cell(50, 4,
                   f'{VISIBLE_DAMAGE_A}')
    pdf.y = top
    pdf.x = offset
    pdf.cell(88, 4, "")
    pdf.multi_cell(50, 4,
                   f'{VISIBLE_DAMAGE_B}')
    # формирование первой страницы
    pdf.output(CASH_TEMPLATE_PATH)
    new_pdf = PdfFileReader(open(CASH_TEMPLATE_PATH, 'rb'))
    if os.path.exists(CASH_TEMPLATE_PATH):
        os.remove(CASH_TEMPLATE_PATH)
    existing_pdf = PdfFileReader(open("evroprotokol.pdf", "rb"))

    output = PdfFileWriter()
    page = existing_pdf.getPage(0)
    page.mergePage(new_pdf.getPage(0))
    """
        лого
    """
    CASH_TEMPLATE_PATH = f'result/{result.CASH_TEMPLATE_PATH}'
    pdf_logo = FPDF(orientation='P', unit='mm', format='A4')
    pdf_logo.add_page()
    pdf_logo.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf_logo.set_font("DejaVu", size=8)
    top = pdf.y
    offset = pdf.x + 35
    pdf_logo.image(f'images/vis_logo.jpeg', w=35, h=15)
    pdf.y = top
    pdf.x = offset


    pdf_logo.cell(190, 8, "", align='C', ln=1)
    pdf_logo.cell(140, 8, "", align='C')
    top = pdf.y
    offset = pdf.x + 50
    pdf_logo.image(f'images/vis_phone.jpeg', w=50, h=16)
    pdf.y = top
    pdf.x = offset
    pdf_logo.cell(0.1, 8, '')
    pdf_logo.cell(190, 8, "", align='C', ln=1)


    pdf_logo.output(CASH_TEMPLATE_PATH)
    new_pdf_logo = PdfFileReader(open(CASH_TEMPLATE_PATH, 'rb'))
    if os.path.exists(CASH_TEMPLATE_PATH):
        os.remove(CASH_TEMPLATE_PATH)
    page.mergePage(new_pdf_logo.getPage(0))

    output.addPage(page) # сохранение первой страницы

    # вторая страница

    pdf_second = FPDF(orientation='P', unit='mm', format='A4')
    pdf_second.add_page()
    pdf_second.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
    pdf_second.set_font("DejaVu", size=10)

    """
        1.строка
    """
    pdf_second.cell(150, 5, '', ln=1)
    """
        2.строка
    """
    TRANSPORT_A = result.TRANSPORT_A
    TRANSPORT_B = result.TRANSPORT_B
    pdf_second.cell(50, 5, '')
    pdf_second.set_font('DejaVu', size=15)
    pdf_second.cell(5.5, 5, f'{TRANSPORT_A}')
    pdf_second.cell(12, 5, '')
    pdf_second.cell(5.5, 5, f'{TRANSPORT_B}', ln=1)
    """
        3.строка
    """
    pdf_second.cell(190, 13.4, '', ln=1)

    """
        4.строка
    """
    CIRCUMSTANCES = result.CIRCUMSTANCES
    pdf_second.cell(5, 48, '')
    pdf_second.set_font("DejaVu", size=8)
    col_width = 185
    top = pdf_second.y
    offset = pdf_second.x + col_width
    pdf_second.set_fill_color(255, 255, 255)
    width_row = len(CIRCUMSTANCES)
    if width_row >= 1100:
        CIRCUMSTANCES = CIRCUMSTANCES[:1100]
    pdf_second.multi_cell(col_width, 5, CIRCUMSTANCES, fill=True)
    pdf_second.y = top
    pdf_second.x = offset
    pdf_second.cell(0.1, 48, '', ln=1)

    """
        5.строка
    """
    pdf_second.cell(190, 9, '', ln=1)
    """
        6.строка
    """
    MANAGET_OWNER = result.MANAGET_OWNER
    MANAGET_ANOTHER = result.MANAGET_ANOTHER
    pdf_second.set_font("DejaVu", size=15)
    pdf_second.cell(47.4, 3.8, '')
    pdf_second.cell(3, 3.8, f'{MANAGET_OWNER}', ln=1, align='C')
    pdf_second.cell(47.4, 3.8, '')
    pdf_second.cell(3, 3.8, f'{MANAGET_ANOTHER}', ln=1, align='C')
    """
        7.строка
    """
    pdf_second.cell(190, 12, '', ln=1, fill=True)
    """
        8.строка
    """
    PHOTO_ONE = result.PHOTO_ONE
    PHOTO_TWO = result.PHOTO_TWO

    if PHOTO_ONE:
        top = pdf_second.y
        offset = pdf_second.x + 90
        pdf_second.image(f'media/{PHOTO_ONE}', w=90, h=60)
        pdf_second.y = top
        pdf_second.x = offset
        if os.path.exists(f'media/{PHOTO_ONE}'):
            os.remove(f'media/{PHOTO_ONE}')
    else:
        pdf_second.cell(90, 60, '', fill=True)
    pdf_second.cell(10, 60, '', fill=True)
    if PHOTO_TWO:
        top = pdf_second.y
        offset = pdf_second.x + 90
        pdf_second.image(f'media/{PHOTO_TWO}', w=90, h=60)
        pdf_second.y = top
        pdf_second.x = offset
        if os.path.exists(f'media/{PHOTO_TWO}'):
            os.remove(f'media/{PHOTO_TWO}')
    else:
        pdf_second.cell(90, 60, '', fill=True)
    pdf_second.cell(1, 60, '', fill=True, ln=1)

    """
        8.строка
    """
    pdf_second.cell(190, 7, '', ln=1)

    """
        9.строка
    """
    WORK_AUTO_YES = result.WORK_AUTO_YES
    WORK_AUTO_NO = result.WORK_AUTO_NO
    pdf_second.cell(62.7, 4, '')
    pdf_second.cell(4, 4, f'{WORK_AUTO_YES}', align='C')
    pdf_second.cell(6, 4, '')
    pdf_second.cell(4, 4, f'{WORK_AUTO_NO}', align='C', ln=1)
    """
        10.строка
    """
    pdf_second.cell(190, 3, '', ln=1)
    """
        11.строка
    """
    LOCATION = result.LOCATION
    pdf_second.cell(5, 8, '')
    pdf_second.set_font("DejaVu", size=8)
    if len(LOCATION) >= 274:
        LOCATION = LOCATION[:274]
    top = pdf_second.y
    offset = pdf_second.x + 185
    pdf_second.multi_cell(185, 4, f"{LOCATION}")
    pdf_second.y = top
    pdf_second.x = offset
    pdf_second.cell(0.1, 8, '', ln=1)
    """
        12.строка
    """
    pdf_second.cell(70, 4, '', ln=1)
    """
        13.строка
    """
    NOTE = result.NOTE
    pdf_second.cell(5, 24, '')
    top = pdf_second.y
    offset = pdf_second.x + 185
    if len(NOTE) >= 845:
        NOTE = NOTE[:845]
    pdf_second.multi_cell(185, 4, f"{NOTE}")
    pdf_second.y = top
    pdf_second.x = offset

    # формирование второй страницы
    pdf_second.output(CASH_TEMPLATE_PATH)
    new_pdf_second = PdfFileReader(open(CASH_TEMPLATE_PATH, "rb"))
    if os.path.exists(CASH_TEMPLATE_PATH):
        os.remove(CASH_TEMPLATE_PATH)
    page_second = existing_pdf.getPage(1)
    page_second.mergePage(new_pdf_second.getPage(0))
    output.addPage(page_second)

    # запись в pdf файл
    FILE_II_PATH = f"result/{result.PATH_RESULT_FILE}"
    outputStream = open(FILE_II_PATH, "wb")
    output.write(outputStream)
    outputStream.close()

    return FILE_II_PATH


if __name__ == "__main__":
    pass
