from fastapi import APIRouter
from schemas.dispositivos import DispositivoCreate

router = APIRouter(prefix="/dispositivos", tags=["DISPOSITIVOS"])
@router.post("/")
def criar_dispositivo(novo_dispositivo: DispositivoCreate):
    return novo_dispositivo