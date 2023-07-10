from fastapi import FastAPI
import joblib
import numpy as np

app = FastAPI()

def load_model():
    try:
        model = joblib.load('/home/muhfaridansutariya/asistensi_mlprocess/MLProcess/Asistensi/jakarta-pollution-classification/models/model2.pkl')
        return model
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
        return response
    
@app.post("/predict")
async def predict(DKI1: float, DKI2: float, DKI3: float, DKI4: float, DKI5: float, pm10: float, pm25: float, so2: float, co: float, o3: float, no2: float):

    model = load_model()

    label = ['BAIK', 'TIDAK SEHAT']

    try:
        input_data = np.array([[DKI1, DKI2, DKI3, DKI4, DKI5, pm10, pm25, so2, co, o3, no2]])
        prediction = model.predict(input_data)
        response = {
            "status": 200,
            "input": [DKI1, DKI2, DKI3, DKI4, DKI5, pm10, pm25, so2, co, o3, no2],
            "message": label[prediction[0]]
        }
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
    return response
