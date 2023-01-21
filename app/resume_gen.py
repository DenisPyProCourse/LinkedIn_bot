from faker import Faker

fake = Faker()

# def job_listing():
#     print("Between", fake.day_of_week(), fake.month_name(), fake.day_of_month(), fake.year(), "and", fake.day_of_week(), fake.month_name(), fake.day_of_month(), fake.year(), "\nI worked at", fake.company(), "located at\n", fake.address(), "\nwhere we focused on", fake.catch_phrase(), "\nIn my job, I", fake.bs(), "by", fake.bs(), "through", fake.bs(), "\nMy boss was", fake.prefix(), fake.name(),"\nOur website is", fake.url(), "and you can speak with HR representative", fake.prefix(), fake.name(), "at", fake.phone_number(), "or via e-mail at", fake.company_email(),  "who can attest to my accomplishments", "\n______________________")

def job_listing():
    work_exp = "Between" + ' ' + fake.day_of_week() + ' ' + fake.month_name() + ' ' + fake.day_of_month() + ' ' + '2019' + ' ' + "and" + ' ' + fake.day_of_week() + ' ' + 'December' + ' ' + fake.day_of_month() + ' ' + '2022' + ' ' + "\nI worked at" + ' ' + fake.company() + ' ' + "located at\n" + ' ' + fake.address() + ' ' + "\nwhere we focused on" + ' ' + fake.catch_phrase() + ' ' + "\nIn my job, I" + ' ' + fake.bs() + ' ' + "by" + ' ' + fake.bs() + ' ' + "through" + ' ' + fake.bs() + ' ' + "\nMy boss was" + ' ' + fake.prefix() + ' ' + fake.name() + ' ' + "\nOur website is" + ' ' + fake.url() + ' ' + "and you can speak with HR representative" + ' ' + fake.prefix() + ' ' + fake.name() + ' ' + "at" + ' ' + fake.phone_number() + ' ' + "or via e-mail at" + ' ' + fake.company_email() + ' ' + "who can attest to my accomplishments" + ' ' + "\n______________________"
    return work_exp
