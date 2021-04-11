from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CouponsConfig(AppConfig):
    name = 'apps.coupons'
    verbose_name = _('Coupon')
    verbose_name_plural = _('Coupons')
