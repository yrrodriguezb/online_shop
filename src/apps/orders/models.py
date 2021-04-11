from decimal import Decimal
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import gettext_lazy as _
from apps.shop.models import Product
from apps.coupons.models import Coupon


class Order(models.Model):
    first_name = models.CharField(_('First name'), max_length=50)
    last_name = models.CharField(_('Last name'), max_length=50)
    email = models.EmailField(_('E-mail'))
    address = models.CharField(_('Address'), max_length=250)
    postal_code = models.CharField(_('Postal code'), max_length=20)
    city = models.CharField(_('City'), max_length=100)
    created = models.DateTimeField(_('Created'), auto_now_add=True)
    updated = models.DateTimeField(_('Updated'), auto_now=True)
    paid = models.BooleanField(_('Paid'), default=False)
    braintree_id = models.CharField(_('Braintree Id'), max_length=150, blank=True)
    coupon = models.ForeignKey(Coupon, verbose_name=_('Cuopon'), related_name='orders', null=True, blank=True, on_delete=models.SET_NULL)
    discount = models.IntegerField(_('Discount'), default=0, validators=[MinValueValidator(0), MaxValueValidator(100)])

    class Meta:
        ordering = ('-created',)
        verbose_name = _('Order')
        verbose_name_plural = _('Orders')
    
    def __str__(self):
        return f'Order {self.id}'

    def get_total_cost(self):
        total_cost = sum(item.get_cost() for item in self.items.all())
        return total_cost - total_cost * (self.discount / Decimal(100))


class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='order_items', on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        verbose_name = _('Order Items')
        verbose_name_plural = _('Order Items')

    def __str__(self):
        return str(self.id)
    
    def get_cost(self):
        return self.price * self.quantity