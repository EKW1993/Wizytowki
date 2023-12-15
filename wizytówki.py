from faker import Faker

class BaseContact: 
    def __init__(self, first_name, surname, telephone, email): 
        self.first_name = first_name 
        self.surname = surname 
        self.telephone = telephone 
        self.email = email

    def __str__(self): 
        return f"{self.first_name} {self.surname}: {self.email}"

    def contact(self): 
        print(f"Wybieram numer {self.telephone} i dzwonię do {self.first_name} {self.surname}")

    @property 
    def label_length(self): 
        return len(self.first_name) + len(self.surname)

class BusinessContact(BaseContact): 
    def __init__(self, first_name, surname, business_telephone, email, job, company): 
        super().__init__(first_name, surname, business_telephone, email) 
        self.business_telephone=business_telephone
        self.job = job 
        self.company = company

    def contact(self): 
        super().contact()
        print(f"{self.job} z {self.company}")

def create_contacts(type, quantity): 
    fake = Faker() 
    contacts = [] 
    for _ in range(quantity): 
        first_name = fake.first_name() 
        surname = fake.last_name() 
        telephone = fake.phone_number() 
        email = fake.email() 
        if type == "base": 
            contact = BaseContact(first_name, surname, telephone, email) 
        elif type == "business": 
            business_telephone=fake.phone_number()
            job = fake.job() 
            company = fake.company() 
            contact = BusinessContact(first_name, surname, business_telephone, email, job, company) 
        else: 
            print("Nieprawidłowy rodzaj wizytówki") 
            return None 
        contacts.append(contact) 
    return contacts

contacts = create_contacts("base", 3) 
for contact in contacts: 
    print(contact) 
    contact.contact() 
    print(contact.label_length)

contacts = create_contacts("business", 3) 
for contact in contacts: 
    print(contact) 
    contact.contact() 
    print(contact.label_length)