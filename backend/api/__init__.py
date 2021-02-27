from fastapi import FastAPI
from backend.api.routers import images
from fastapi.middleware.cors import CORSMiddleware


app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*",
                   "http://localhost:*",
                   ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
app.include_router(images.router)

@app.get("/")
async def root():
    return {"message": "Hello Wor13ld"}
