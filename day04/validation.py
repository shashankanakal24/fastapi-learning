from pydantic import BaseModel,field_validator,model_validator,computed_field,Field,EmailStr
from typing import List, Dict,Annotated,Literal,Optional

class Address(BaseModel):
    city:Annotated[str,Field(description="Enter the city")]
    state:Annotated[str,Field(description="Enter the state")]
    pincode:Annotated[int,Field(description="Enter the Pincode ")]

class Patient(BaseModel):
    id:Annotated[str,Field(...,description="Enter the ID of the Patient",examples=["P001"])]
    name:Annotated[str,Field(...,description="Enter the name of the Patient")]
    age:int=Field(gt=0)
    gender:Annotated[Literal['male','female','others'],Field(description="Gender selection")]
    height:Annotated[float,Field(...,gt=0,description="Enter the Height")]
    weight:Annotated[float,Field(gt=0,description="Enter the Weight")]
    email:Annotated[EmailStr,Field(description="Enter the Email")]
    contact:Annotated[Dict[str,str],Field(description="Enter your contacts")]
    allergies:Annotated[List[str],Field(description="List the Allergies")]
    address:Address

    @field_validator('email')
    @classmethod
    def validate_email(cls,value):
        valid_domain=["nichi.com","ndr.com"]
        domain_name=value.split('@')[-1]
        if domain_name not in valid_domain:
            raise ValueError("not a valid email domain")    
        return value
    
    @model_validator(mode='after')
    def validate_emergencynumber(model):
        if model.age > 70 and 'emergency' not in model.contact:
            raise ValueError("Patient Aged above 70 must have emergency number")
        return model
    
    @computed_field
    @property
    def bmi(self) ->float:
        bmi=round(self.weight/(self.height**2),2)
        return bmi
    
    @computed_field
    @property
    def verdict(self) ->str:
        if self.bmi <18.5:
            return "Under weight"
        elif self.bmi <25:
            return "normal"
        else:
            return "Obese" 
        
class PatientUpdate(BaseModel):
    name:Annotated[Optional[str],Field(default=None)]
    age:Optional[int]=Field(default=None,gt=0)
    gender:Annotated[Optional[Literal['male','female','others']],Field(default=None,description="Gender selection")]
    height:Annotated[Optional[float],Field(default=None,gt=0,description="Enter the Height")]
    weight:Annotated[Optional[float],Field(default=None,gt=0,description="Enter the Weight")]
    contact:Annotated[Optional[Dict[str,str]],Field(default=None,description="Enter your contacts")]
    allergies:Optional[List[str]]=None
    address:Optional[Address]=None
    
  
    
   
        
        
             
        

    
    