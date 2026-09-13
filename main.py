from fastapi import FastAPI, Query, HTTPException, Path
from fastapi.middleware.cors import CORSMiddleware
from typing import List, Optional

from src.schemas import ProfissionalBase, EspecialidadeResponse
from src import services

app = FastAPI(
    title="API de Profissionais de Saúde - Clínica de Saúde",
    description="API RESTful desenvolvida para consulta da disponibilidade dos profissionais da clínica.",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Geral"])
def raiz():
    """Endpoint de status da API."""
    return {
        "mensagem": "API de Profissionais de Saúde",
        "status": "online",
        "documentacao": "/docs",
        "versao": "1.0.0"
    }

@app.get("/api/v1/especialidades", response_model=EspecialidadeResponse, tags=["Especialidades"])
def obter_especialidades():
    """Retorna a lista de todas as especialidades ativas na clínica."""
    try:
        especialidades = services.listar_especialidades()
        return {"especialidades": especialidades}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro interno: {str(e)}")

@app.get("/api/v1/profissionais", response_model=List[ProfissionalBase], tags=["Profissionais"])
def listar_profissionais(
    nome: Optional[str] = Query(
        None, 
        description="Filtra por nome do profissional (busca parcial e case-insensitive)"
    ),
    especialidade: Optional[str] = Query(
        None, 
        description="Filtra por área/especialidade médica"
    )
):
    """
    Retorna a lista de profissionais com suporte a filtros combinados de nome e especialidade.
    """
    try:
        return services.obter_profissionais_filtrados(nome=nome, especialidade=especialidade)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Erro ao filtrar profissionais: {str(e)}")

@app.get("/api/v1/profissionais/{id}", response_model=ProfissionalBase, tags=["Profissionais"])
def obter_profissional_por_id(
    id: int = Path(..., description="ID único do profissional", ge=1)
):
    """Retorna os detalhes e os horários de atendimento de um profissional específico."""
    profissional = services.buscar_por_id(id)
    if not profissional:
        raise HTTPException(status_code=404, detail=f"Profissional com ID {id} não encontrado.")
    return profissional