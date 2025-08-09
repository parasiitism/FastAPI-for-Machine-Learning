from pydantic import BaseModel,EmailStr,AnyUrl,Field,computed_field
from typing import List,Dict,Optional,Annotated

class Patient(BaseModel):
    name:str 
    email:EmailStr
    age:int 
    weight:float # kg
    height:float # mtr
    married:bool # mtr
    allergies:List[str]
    contact_details:Dict[str,str]

    @computed_field
    @property
    def bmi(self)->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi

def update_patient_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient.allergies)
    print(patient.married)
    print('BMI',patient.bmi)
    print('updated')

patient_info={'name':'nitish','email':'paras94nitjsr@hdfc.com','linkedin_url':'https://www.linkedin.com/in/parasiitism',
              'age':30,'weight':75.2,'height':1.72,'married':True,
              'allergies':['pollen','dust'],'contact_details':{'email':'paras@gmail.com'},
              'phone':'+919546566148'}

patient1=Patient(**patient_info)
update_patient_data(patient1)