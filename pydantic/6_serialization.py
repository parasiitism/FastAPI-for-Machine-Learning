from pydantic import BaseModel

class Address(BaseModel):
    city: str 
    state: str 
    pin: str 

class Patient(BaseModel):
    name: str 
    gender: str 
    age: int

address_dict={'city':'gurgoan','state':'haryana','pin':'122234'}
address1=Address(**address_dict)

patient_dict={'name':'nitish','gender':'male','age':35,'address':address1}
patient1=Patient(**patient_dict)



temp=patient1.model_dump()
print(f"Here is temp: {temp} and type: {type(temp)}\n")


json=patient1.model_dump_json()
print(f"Here is json: {json} and type: {type(json)}")







