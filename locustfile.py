from locust import HttpUser, task, between
import random
import os
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'createDataPaV2.settings')
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
from pav2.models import Order
from pav2.models import Get
from pav2.models import Pick
from dotenv import load_dotenv


load_dotenv()

header = os.getenv("REQUEST_HEADER_TOKEN_INDEX")
token = os.getenv("REQUEST_HEADER_TOKEN_VALUE")

class SendMultiRequest(HttpUser):

    wait_time = between(1, 1)

    @task
    def createData(self):
        order = Order()
        order.save()

        orderBody = {
            "id": order.id,
            "order_id": order.id,
            "userId": 1411962698,
            "firstName": "Rappi",
            "lastName": "SAS",
            "user_phone": "+57 031 3163535",
            "createdAt": "2021-11-09 16:27:20",
            "storeId": "900104538",
            "useGrowth": 'true',
            "growth_global_discounts": [],
            "growthGlobalDiscounts": [],
            "growthDeliveryDiscounts": {
                "totalPercentageDiscount": 0,
                "totalValueDiscount": 0
            },
            "totalValueWithTotalDiscountGrowth": 3990,
            "totalValueFromGrowth": 3990,
            "totalValue": 3990,
            "products": [
                
            ],
            "cooking_time_information": {
                "cooking_time": 15,
                "min_cooking_time": 10,
                "max_cooking_time": 20
            },
            "user_address": "Rappi Principal - Cl 93 #19-58.",
            "payment_method": "cc",
            "delivery_method": "delivery",
            "is_marketplace": 'false',
            "address_description": "1",
            "address_details": {
                "main_street_type": "Calle",
                "main_street_number": "68B Bis",
                "main_street_quadrant": "Sur",
                "secondary_street_number": "70C",
                "meter": "12",
                "secondary_street_quadrant": "Sur",
                "complete_address": "Calle 68B Bis # 70c - 12",
                "city": "Bogotá",
                "neighborhood": "Salitre",
                "postal_code": "110421"
            },
            "address_tag": "Otro",
            "address_zip_code": "1419",
            "charges": {
                "shipping": 0,
                "service_fee": 0
            },
            "discounts": {},
            "lat": 4.684172514993,
            "lng": -74.048535525799,
            "partner_id": 57799,
            "payment_details": {
                "total_discounts": 0,
                "total_charges": 0,
                "total_rappi_pay": 0,
                "total_rappi_credits": 0,
                "total_products_with_markdown": 3990,
                "tip": 0,
                "total_whims": 0,
                "total_orders": 3990,
                "total_products": 3990
            },
            "billing_information": {
                "address": "Some street 12345",
                "billing_type": "Factura",
                "document_number": "32432342",
                "document_type": "DNI",
                "email": "client@gmail.com",
                "name": "client",
                "phone": "43333222"
            }
        }
        self.client.post("/menu-mapping-test/", json=orderBody, headers={'pos-flow': 'true', 'save-log': 'true'})