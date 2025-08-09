from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator,model_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str 
    email:EmailStr
    age:int 
    weight:float
    married:bool 
    allergies:List[str]
    contact_details:Dict[str,str]

    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age>16 and 'emergency' not in model.contact_details:
            raise ValueError('Patient older than 60 must have an emergency contact')
        return model



def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('updated')


patient_info={'name':'nitish','email':'paras94nitjsr@hdfc.com','linkedin_url':'https://www.linkedin.com/in/parasiitism',
              'age':30,'weight':75.2,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'email':'paras@gmail.com'},
              'phone':'+919546566148'}

patient1=Patient(**patient_info)
update_patient_data(patient1)