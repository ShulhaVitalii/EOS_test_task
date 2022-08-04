from data.data import Person
from faker import Faker

faker_en = Faker('en_Us')


def generated_person():
    yield Person(
        firstname=faker_en.first_name(),
        lastname=faker_en.last_name(),
        email=faker_en.email()
    )


