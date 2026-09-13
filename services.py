import json
import os
from typing import List, Optional

DATA_FILE = os.path.join(os.path.dirname(__file__), "..", "data", "profissionais.json")

def carregar_dados() -> List[dict]:
    if not os.path.exists(DATA_FILE):
        raise FileNotFoundError(f"[ERRO] Arquivo JSON não encontrado: {DATA_FILE}")
    
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def listar_todos_profissionais() -> List[dict]:
    return carregar_dados()

def obter_profissionais_filtrados(
    nome: Optional[str] = None, 
    especialidade: Optional[str] = None
) -> List[dict]:
    profissionais = carregar_dados()
    
    if especialidade:
        esp_clean = especialidade.strip().lower()
        profissionais = [p for p in profissionais if p["especialidade"].strip().lower() == esp_clean]
        
    if nome:
        nome_clean = nome.strip().lower()
        profissionais = [p for p in profissionais if nome_clean in p["nome"].strip().lower()]
        
    return profissionais

def listar_especialidades() -> List[str]:
    profissionais = carregar_dados()
    return sorted(list(set(p["especialidade"] for p in profissionais)))

def buscar_por_id(profissional_id: int) -> Optional[dict]:
    profissionais = carregar_dados()
    for p in profissionais:
        if p["id"] == profissional_id:
            return p
    return None