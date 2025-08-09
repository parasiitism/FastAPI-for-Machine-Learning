from pydantic import BaseModel,EmailStr,AnyUrl,Field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:Annotated[str,Field(max_length=50,title='Name of the patient',
                             description='Give the name of patient less than 50 chars',
                             examples=['Paras','Ajay'])]
    email: EmailStr
    linkedin_url:AnyUrl
    age:int = Field(gt=0,lt=120)
    weight:Annotated[float,Field(gt=0,strict=True)]
    married:Annotated[bool,Field(default=None,
                                 description='Is the patient married or not')]
    allergies:Optional[List[str]] = Field(max_length=5)
    contact_details:Dict[str,str]

def insert_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.email)
    print(patient.linkedin_url)
    print(patient.weight)
    print(patient.married)
    print(patient.allergies)
    print(patient.contact_details)
    print('Records has been inserted successfully\n')

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("records successfully has been updated")

patient_info={'name':'nitish','email':'paras94nitjsr@gmail.com','linkedin_url':'https://www.linkedin.com/in/parasiitism',
              'age':30,'weight':75.2,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'email':'paras@gmail.com'},
              'phone':'+919546566148'}

patient_info=Patient(**patient_info)
insert_patient_data(patient=patient_info)
update_patient_data(patient=patient_info)


