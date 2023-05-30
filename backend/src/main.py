from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Middleware: https://fastapi.tiangolo.com/tutorial/cors/
origins = [
    "http://localhost",
    "http://localhost:5173",  # Default webapp port
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.post("/")
async def root():
    return {"message": "Hello World"}
