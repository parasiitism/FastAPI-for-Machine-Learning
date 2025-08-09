from pydantic import BaseModel,EmailStr,AnyUrl,Field,field_validator
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str 
    email:EmailStr
    age:int 
    weight:float
    married:bool 
    allergies:List[str]
    contact_details:Dict[str,str]

    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domains=['hdfc.com','icici.com']
        #abc.@gmail.com
        domain_name=value.split('@')[-1]

        if domain_name not in valid_domains:
            raise ValueError('Not a valid domain')
        return value 
    
    @field_validator('name',mode='after')
    @classmethod
    def transform_name(cls,value):
        return value.upper()
    
    @field_validator('age')
    @classmethod
    def validate_age(cls,value):
        if 0<value<100:
            return value 
        else:
            raise ValueError('Age should be between 0 and 100')

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