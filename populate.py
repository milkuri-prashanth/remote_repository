import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','jobproject.settings')
import django
django.setup()



from jobapp.models import *
from faker import Faker
from random import *

fake = Faker()
def phonenumbergen():
    d1 = randint(7,9)
    num = ' '+str(d1)
    for i in range(0,9):
        num = num+str(randint(0,9))
    return int(num)

def populate(n):
    for i in range(n):
        fdate=fake.date()
        fcompany=fake.company()
        ftitle=fake.random_element(elements=('Team manager','project manager','Software Engineer'))
        feligibility=fake.random_element(elements=('B tech','MCA','M tech','Phd'))
        faddress=fake.address()
        femail = fake.email()
        fphonenumber=phonenumbergen()
        hydjobs_record=hydjobs.objects.get_or_create(date=fdate,company=fcompany,title=ftitle,eligibility=feligibility,addr=faddress,email=femail,pno=fphonenumber)
populate(25)
