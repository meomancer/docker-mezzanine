from copy import deepcopy
from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from cartridge.shop.admin import OrderAdmin
from cartridge.shop.models import Order

blog_fieldsets = deepcopy(OrderAdmin.fieldsets)
blog_fieldsets = list(blog_fieldsets)
blog_fieldsets.insert(3, (
    (_("Information"),
     {"fields": ("dietary_requirements", "plato", "how_to_find_out")})))
blog_fieldsets = tuple(blog_fieldsets)


class OrderAdmin(OrderAdmin):
    fieldsets = blog_fieldsets


admin.site.unregister(Order)
admin.site.register(Order, OrderAdmin)
