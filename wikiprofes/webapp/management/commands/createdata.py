from django.core.management.base import BaseCommand
from faker import Faker
import faker.providers
from webapp.models import Materia

CLAVE_MATERIA = [
    'I5882','I5883','I5892','I5893','I5894',
    'I5886','I5887','I5915','I5895','I5896',
    'I5888','I5889','I5907','I5884','I5885','I5897',
    'I5890','I5891','I5908','I5910','I5898',
    'I5901','I5905','I5909','I5900','I5899',
    'I5904','I5903',
    'I5906','I5902','I5911',
    'I5913','I5914','I5912',
]


class Provider(faker.providers.BaseProvider):
    def clave_materia(self):
        return self.random_element(CLAVE_MATERIA)

class Command(BaseCommand):
    help = "Command Information"

    def handle(self, *args, **kwargs):
        
        fake = Faker(["es_MX"])
        fake.add_provider(Provider)

        for _ in range(15):
            d = fake.unique.clave_materia()
            Materia.objects.create(clave=d)



