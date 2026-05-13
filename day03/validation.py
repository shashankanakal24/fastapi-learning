from pydantic import BaseModel,Field,EmailStr, field_validator,model_validator,computed_field
from typing import Dict,List


class Address(BaseModel):
    city:str
    state:str
    pin:str

class Patient(BaseModel):
    name:str
    age:int
    address:Address
    email:EmailStr
    weight:float=Field(gt=0)
    height:float=Field(gt=0)
    married:bool
    allergies:List[str]
    contact:Dict[str,str]
    
    #custom business validation
    @field_validator('email')
    @classmethod
    def email_validator(cls,value):
        valid_domain=["hdfc.com","icici.com"]
        domain_name=value.split('@')[-1]
        
        if domain_name not in valid_domain:
            raise ValueError('Not a domain belonging email')
        return value
    
    @model_validator(mode='after')
    def validate_emergency_contact(cls,model):
        if model.age >60 and 'emergency' not in model.contact:
            raise ValueError('Patient elder than 60 must have emergency number')
        return model
    
    @computed_field
    def bmi(self)->float:
        bmi = round(self.weight/(self.height**2),2)
        return  bmi
    
            
    
        
    
    
    
def insert_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print(patient)
    print(patient.bmi)
    print("insert")

def update_data(patient:Patient):
    print(patient.name)
    print(patient.age)
    print("updated")
    
address_dict ={"city":"bengaluru","state":"karnataka","pin":"890987"}

address1=Address(**address_dict)
    
patient_dict ={"name":"shashank","age":70,"address": address1,"email":"sah@hdfc.com","weight":90.5,"height":"90","married":False,"allergies":["pollen grains","smoke"],"contact":{"home":"5896321420","office":"78965236","emergency":"7852369845"}}
    
patient1= Patient(**patient_dict)

insert_data(patient1)

temp=patient1.model_dump()