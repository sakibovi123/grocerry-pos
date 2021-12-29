from django.contrib import admin
from .models import *
# Register your models here.


admin.site.register(
    [
        GrocerryBrand,
        Currency,
        GrocerryCategory,
        Shop,
        CountryModel,
        CityModel,
        Vendor,
        Roles,
        Employee,
        Item,
        CartItems,
        Checkout
    ]
)