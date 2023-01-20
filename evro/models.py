from django.contrib.auth.models import User
from django.db import models


def content_file_name(instance, filename):
    return '/'.join(['photos', str(instance.date), filename])


class PageModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    placeDTP = models.CharField(max_length=115)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    quantity_tc = models.IntegerField(default=0)
    victims = models.IntegerField(default=0)
    deaded = models.IntegerField(default=0)
    drunk_yes = models.BooleanField(default=False)
    drunk_no = models.BooleanField(default=True)
    damage_yes = models.BooleanField(default=False)
    damage_no = models.BooleanField(default=True)
    other_damage_yes = models.BooleanField(default=False)
    other_damage_no = models.BooleanField(default=True)
    withesses = models.CharField(max_length=150, null=True, blank=True)
    polis_men_yes = models.BooleanField(default=False)
    polis_men_no = models.BooleanField(default=True)
    bange_number = models.CharField(max_length=15, null=True, blank=True)
    # "A"
    model_a = models.CharField(max_length=50, default='')
    number_vin_a = models.CharField(max_length=17, default='')
    number_tc_a = models.CharField(max_length=9, default='')
    tex_seria_a = models.CharField(max_length=4, default='')
    tex_number_a = models.CharField(max_length=6, default='')
    owner_name_a = models.CharField(max_length=70, default='')
    adress_a = models.CharField(max_length=80, default='')
    driver_name_a = models.CharField(max_length=100, default='')
    born_data_a = models.DateField(null=True)
    adress_driver_a = models.CharField(max_length=80, default='')
    phone_a = models.CharField(max_length=15, null=True, blank=True)
    driver_seria_a = models.CharField(max_length=4, default='')
    driver_number_a = models.CharField(max_length=6, default='')
    category_a = models.CharField(max_length=5, default='')
    category_date_a = models.DateField(null=True)
    contract_a = models.CharField(max_length=50, default='', null=True, blank=True)
    insurer_a = models.CharField(max_length=50, default='')
    polis_seria_a = models.CharField(max_length=3, default='')
    polis_number_a = models.CharField(max_length=10, default='')
    polis_date_end_a = models.DateField(null=True)
    damage_yes_a = models.BooleanField(default=False)
    damage_no_a = models.BooleanField(default=True)
    visible_damage_a = models.CharField(max_length=150, null=True, blank=True)
    # "B"
    model_b = models.CharField(max_length=50, default='')
    number_vin_b = models.CharField(max_length=17, default='')
    number_tc_b = models.CharField(max_length=9, default='')
    tex_seria_b = models.CharField(max_length=4, default='')
    tex_number_b = models.CharField(max_length=6, default='')
    owner_name_b = models.CharField(max_length=70, default='')
    adress_b = models.CharField(max_length=80, default='')
    driver_name_b = models.CharField(max_length=100, default='')
    born_data_b = models.DateField(null=True)
    adress_driver_b = models.CharField(max_length=80, default='')
    phone_b = models.CharField(max_length=15, null=True, blank=True)
    driver_seria_b = models.CharField(max_length=4, default='')
    driver_number_b = models.CharField(max_length=6, default='')
    category_b = models.CharField(max_length=5, default='')
    category_date_b = models.DateField(null=True)
    contract_b = models.CharField(max_length=50, default='', null=True, blank=True)
    insurer_b = models.CharField(max_length=50, default='')
    polis_seria_b = models.CharField(max_length=3, default='')
    polis_number_b = models.CharField(max_length=10, default='')
    polis_date_end_b = models.DateField(null=True)
    damage_yes_b = models.BooleanField(default=False)
    damage_no_b = models.BooleanField(default=True)
    visible_damage_b = models.CharField(max_length=150, null=True, blank=True)
    # "A" case "B"
    one_a = models.BooleanField(default=False)
    one_b = models.BooleanField(default=False)
    two_a = models.BooleanField(default=False)
    two_b = models.BooleanField(default=False)
    free_a = models.BooleanField(default=False)
    free_b = models.BooleanField(default=False)
    four_a = models.BooleanField(default=False)
    four_b = models.BooleanField(default=False)
    five_a = models.BooleanField(default=False)
    five_b = models.BooleanField(default=False)
    six_a = models.BooleanField(default=False)
    six_b = models.BooleanField(default=False)
    seven_a = models.BooleanField(default=False)
    seven_b = models.BooleanField(default=False)
    eigth_a = models.BooleanField(default=False)
    eigth_b = models.BooleanField(default=False)
    nine_a = models.BooleanField(default=False)
    nine_b = models.BooleanField(default=False)
    ten_a = models.BooleanField(default=False)
    ten_b = models.BooleanField(default=False)
    eleven_a = models.BooleanField(default=False)
    eleven_b = models.BooleanField(default=False)
    twelve_a = models.BooleanField(default=False)
    twelve_b = models.BooleanField(default=False)
    thirteen_a = models.BooleanField(default=False)
    thirteen_b = models.BooleanField(default=False)
    fourteen_a = models.BooleanField(default=False)
    fourteen_b = models.BooleanField(default=False)
    fiveteen_a = models.BooleanField(default=False)
    fiveteen_b = models.BooleanField(default=False)
    sixteen_a = models.BooleanField(default=False)
    sixteen_b = models.BooleanField(default=False)
    seventeen_a = models.BooleanField(default=False)
    seventeen_b = models.BooleanField(default=False)
    eigthteen_a = models.BooleanField(default=False)
    eigthteen_b = models.BooleanField(default=False)
    nineteen_a = models.BooleanField(default=False)
    nineteen_b = models.BooleanField(default=False)
    twenty_a = models.BooleanField(default=False)
    twenty_b = models.BooleanField(default=False)
    twenty_one_a = models.BooleanField(default=False)
    twenty_one_b = models.BooleanField(default=False)
    twenty_two_a = models.BooleanField(default=False)
    twenty_two_b = models.BooleanField(default=False)
    twenty_free_a = models.BooleanField(default=False)
    twenty_four_b = models.BooleanField(default=False)
    quantity_a = models.CharField(max_length=1, default='0')
    quantity_b = models.CharField(max_length=1, default='0')
    transport_a = models.BooleanField(default=False)
    transport_b = models.BooleanField(default=False)
    circumstances = models.TextField(null=True, blank=True, max_length=1100)
    managet_owner = models.BooleanField(default=False, verbose_name='собственник')
    managet_another = models.BooleanField(default=False, verbose_name='иное лицо, подущенное к управлению ТС')
    photo_one = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    photo_two = models.ImageField(upload_to=content_file_name, null=True, blank=True)
    work_auto_yes = models.BooleanField(default=True)
    work_auto_no = models.BooleanField(default=False)
    location = models.TextField(null=True, blank=True, max_length=235)
    note = models.TextField(null=True, blank=True, max_length=800)

    def __str__(self):
        return f'({self.pk}, {self.date})'
