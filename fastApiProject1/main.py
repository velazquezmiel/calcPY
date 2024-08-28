from fastapi import FastAPI
from routers.residencia import router as residencia_router
from routers.comodos import router as comodo_router
from routers.dispositivos import router as dispositivos_router
app = FastAPI()

app.include_router(residencia_router)
app.include_router(comodo_router)
app.include_router(dispositivos_router)

