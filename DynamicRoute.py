from fastapi import FastAPI

# Create FastAPI app instance
app = FastAPI()


# User Route # Dynamic Route
@app.get("/user/{user_id}")
def get_user(user_id:int):
    return{"User_ID": user_id}