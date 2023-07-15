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

def load_encoder():
    try:
        ohe_stasiun = joblib.load("/home/muhfaridansutariya/asistensi_mlprocess/MLProcess/Asistensi/jakarta-pollution-classification/models/ohe_stasiun.pkl")
        return ohe_stasiun
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
        return response
    
@app.post("/predict")
async def predict(stasiun: str, pm10: float, pm25: float, so2: float, co: float, o3: float, no2: float):

    model = load_model()
    encoder = load_encoder()

    label = ['BAIK', 'TIDAK SEHAT']

    encoded_stasiun = encoder.transform(np.array(stasiun).reshape(-1, 1))
    numerical_features = np.array([[pm10, pm25, so2, co, o3, no2]])

    input_data = np.concatenate((encoded_stasiun, numerical_features), axis=1)

    try:
        prediction = model.predict(input_data)
        response = {
            "status": 200,
            "input": input_data.tolist(),
            "message": label[prediction[0]]
        }
    except Exception as e:
        response = {
            "status": 204,
            "message": str(e)
        }
    return response

