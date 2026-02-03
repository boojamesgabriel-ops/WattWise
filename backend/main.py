from fastapi.concurrency import asynccontextmanager
from fastapi import FastAPI
from backend.gemini import initialize_gemini
from routes.kwH import router as kwh_router

@asynccontextmanager
async def lifespan(the_app):
    print("startup things")
    initialize_gemini()
    print("Gemini has been initialized")
    yield
    print("shutdown things")

app = FastAPI(lifespan=lifespan)

app.included_router(kwh_router)