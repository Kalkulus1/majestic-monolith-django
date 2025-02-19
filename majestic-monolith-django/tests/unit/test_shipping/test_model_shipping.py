from datetime import timedelta

from django.test import TestCase
from django.core.exceptions import ValidationError
from django.utils import timezone

from shipping.models import ShippingItem
from shipping.choices import ShippingItemStatus

class ShippingItemUnitTests(TestCase):
    def test_shipping_item_status_with_timestamp_completed(self):
        shipping_item = ShippingItem(
            tracking_number="12341234",
            sku="123123",
            status=ShippingItemStatus.CREATED,
            timestamp_completed=timezone.now()

        )
        with self.assertRaises(ValidationError):
            shipping_item.full_clean()
