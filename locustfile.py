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

        body = {
            "id": order.id,
        }
        self.client.post("/menu-mapping-test/", json=body, headers={'pos-flow': 'true', 'save-log': 'true'})