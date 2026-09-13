from pydantic import BaseModel
from typing import List

class ProfissionalBase(BaseModel):
    id: int
    nome: str
    crm: str
    especialidade: str
    servicos: List[str]
    atende_convenio: bool
    horarios_disponiveis: List[str]

class EspecialidadeResponse(BaseModel):
    especialidades: List[str]