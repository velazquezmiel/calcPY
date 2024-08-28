from fastapi import APIRouter
from schemas.residencias import ResidenciaCreate

router = APIRouter(prefix="/residencias", tags=["RESIDÊNCIAS"])
@router.post("/")
def criar_residencia(nova_residencia: ResidenciaCreate):
    return nova_residencia