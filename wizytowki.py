import faker

class BaseContact:
    def __init__(self, imie, nazwisko, telefon, email):
        self.imie = imie
        self.nazwisko = nazwisko
        self.telefon = telefon
        self.email = email

    def contact(self):
        return f"Wybieram numer {self.telefon} i dzwonię do {self.imie} {self.nazwisko}"

    @property
    def label_length(self):
        return len(f"{self.imie} {self.nazwisko}")

class BusinessContact(BaseContact):
    def __init__(self, imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy):
        super().__init__(imie, nazwisko, telefon, email)
        self.stanowisko = stanowisko
        self.firma = firma
        self.telefon_sluzbowy = telefon_sluzbowy

    def contact(self):
        return f"Wybieram numer {self.telefon_sluzbowy} i dzwonię do {self.imie} {self.nazwisko}, {self.stanowisko}"

def create_contacts(typ_wizytowki, ilosc):
    fake = faker.Faker('pl_PL')
    wizytowki = []
    for _ in range(ilosc):
        imie = fake.first_name()
        nazwisko = fake.last_name()
        telefon = fake.phone_number()
        email = fake.email()
        if typ_wizytowki == 'business':
            stanowisko = fake.job()
            firma = fake.company()
            telefon_sluzbowy = fake.phone_number()
            wizytowki.append(BusinessContact(imie, nazwisko, telefon, email, stanowisko, firma, telefon_sluzbowy))
        elif typ_wizytowki == 'base':
            wizytowki.append(BaseContact(imie, nazwisko, telefon, email))
    return wizytowki

base_contacts = create_contacts('base', 5)
business_contacts = create_contacts('business', 5)

for contact in base_contacts + business_contacts:
    print(contact.contact())
    print(f"Długość etykiety: {contact.label_length}")