

from fastapi import FastAPI
import uvicorn
import httpx



app = FastAPI()

@app.on_event("startup")
async def startup_event():
    app.backend_url = "http://backend:8080"  # Use "backend" as the hostname



@app.post("/predict/")
async def make_prediction():
    # try:
    #     # Serialize inputdata to a dictionary
    #     input_data_dict = {
    #         "sepal_length": inputdata.sepal_length,
    #         "sepal_width": inputdata.sepal_width,
    #         "petal_length": inputdata.petal_length,
    #         "petal_width": inputdata.petal_width
    #     }

        # Make a POST request to the backend service
        async with httpx.AsyncClient() as client:
            response = await client.post(
                f"{app.backend_url}/test")
                #json={"input_data": input_data_dict}  # Send JSON data as the request body
            
        if response.status_code == 200:
            data = response.json()
            return {"prediction": data}
        elif response.status_code == 422:
            error_data = response.json()
            return {"error": "Validation error", "details": error_data}
        else:
            return {"error": "Failed to make a prediction"}

    # except Exception as e:
    #     return {"error": str(e)}

if __name__ == '__main__':
    # server api
    uvicorn.run("main:app", host="0.0.0.0", port=9090,
                reload=True
                )