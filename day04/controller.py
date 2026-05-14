from fastapi import FastAPI,HTTPException
from validation import Patient,PatientUpdate
from fastapi.responses import JSONResponse 
import json

app =FastAPI()

def load_data():
    with open('patient.json','r') as f:
        data= json.load(f)
    return data
def save_data(data):
    with open('patient.json','w') as f:
        json.dump(data,f)

@app.post('/create')
def create_patient(patient:Patient):
    data = load_data()
    if patient.id in data:
        raise HTTPException(status_code=400,detail="User already Exists")
    data[patient.id] = patient.model_dump(exclude=['id'])
    save_data(data)
    
    return JSONResponse(status_code=201,content={'message':'Patient created successfully'})


@app.put('/edit/{patient_id}')
def update_patient(patient_id:str,patientUpdate:PatientUpdate):
    data =load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="User not found")
    
    existing_patient_info =data[patient_id]
    
    update_patient_info =patientUpdate.model_dump(exclude_unset=True)
    
    for key, value in update_patient_info.items():
        if key =='Address':
            if 'Address' not in existing_patient_info:
                existing_patient_info['Address']={}
            for address_key , address_value in value.items():
                existing_patient_info['Address'][address_key] =address_value      
        else:
            existing_patient_info[key]=value
            
            
            
    #now updated and all are dict i need back to convert pydantic to push to the .json 
    data[patient_id] = existing_patient_info

    save_data(data)

    return JSONResponse(
        status_code=200,
        content={
            "message": "Patient updated successfully",
            "updated_data": existing_patient_info
        })
    
    
@app.delete('/delete/{patient_id}')
def delete_patient(patient_id:str):
    data =load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="User not found")
    
    del data[patient_id]
    
    save_data(data)
    
    return JSONResponse(status_code=200,content={'message':'Patient delete succesfully'})

@app.get('/patient')
def get_all_patients():
    data =load_data()
    return JSONResponse(status_code=200,content=data)

@app.get('/patient/{patient_id}')
def get_patient_by_id(patient_id:str):
    data = load_data()
    
    if patient_id not in data:
        raise HTTPException(status_code=404,detail="Not found")
    patient =data[patient_id]
    
    return JSONResponse(status_code=200,content=patient)
        

    
        
    
    
    
    
    
    