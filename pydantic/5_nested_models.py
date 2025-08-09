from pydantic import BaseModel

class Address(BaseModel):
    city:str
    state:str 
    pin:str 


class Patient(BaseModel):
    name:str 
    gender:str 
    age:int 
    address:Address
    

address_dict={'city':'gurgoan','state':'harayan','pin':'221104'}
address1=Address(**address_dict)

# Object of the pydantic model 
patient_dict={'name':'Paras','gender':'Male','age':30,'address':address1}
patient1=Patient(**patient_dict)
# Let's print the contact
print(patient1.name)
print(patient1.gender)
print(patient1.age)
print(patient1.address)
print(patient1.address.city)
print(patient1.address.state)
print(patient1.address.pin)


# Here are the some notable benefits of having the pydantic model 
      # Better organization of related data(e.g., vitals, address, insurance)
      # Resuability: Use Vitals in multiple models( e.g., Patient, MedicalRecord)
      # Readability: Easier for developers and API consumers to understand 
      # Validation: Nested models are validated automatically- no extra work needed












