from faker import Faker

fake = Faker()

checkout_user = {
    "first_name" : fake.first_name(),
    "last_name" : fake.last_name(),
    "postal_code" : fake.postcode()
}