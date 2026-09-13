# Desenvolvimento de Soluções para Clínica de Saúde
## API de Profissionais de Saúde

API RESTful desenvolvida em Python para permitir a consulta de profissionais, especialidades e horários de atendimento disponíveis de uma Clínica de Saúde utilizando FastAPI.

---

## Estrutura do Repositório

```text
clinica-api/
├── src/
│   ├── services.py      # Lógica de leitura do JSON e filtros
│   ├── main.py          # Rotas e configuração da API FastAPI
│   └── schemas.py       # Modelos de dados e validação com Pydantic
├── data/
│   └── profissionais.json # Base de dados local em JSON
├── docs/ 
│   └── (...) # Documentações adicionais do projeto
├── .gitignore           # Arquivos ignorados pelo Git
├── README.md            # Documentação completa do projeto
└── requirements.txt     # Dependências do projeto
```

---

## Tecnologias Utilizadas

- **Linguagem:** Python 3
- **Framework Web:** [FastAPI](https://fastapi.tiangolo.com/)
- **Servidor ASGI:** [Uvicorn](https://www.uvicorn.org/)
- **Validação de Dados:** [Pydantic v2](https://docs.pydantic.dev/)
- **Armazenamento de Dados:** Arquivo local `JSON` (`data/profissionais.json`)
- **Modelagem:** Draw.io (Estrutura Analítica do Projeto - EAP)

---

## Funcionalidades Principais

- **Leitura de Base Local:** Processamento dinâmico de dados armazenados em `JSON`.
- **Catálogo de Especialidades:** Listagem das áreas de atuação atendidas pela clínica.
- **Consulta de Profissionais:** Busca geral de profissionais da clínica.
- **Filtros Avançados:** Busca combinada ou individual por **nome** e **especialidade**.
- **Agenda e Detalhes:** Consulta de informações detalhadas e horários livres por ID do profissional.

---

## Como Executar o Projeto Localmente

Usando `uv`
```bash
# 1. Clonar o repositório
git clone [https://github.com/seu-usuario/api-clinica-profissionais-saude.git](https://github.com/seu-usuario/api-clinica-profissionais-saude.git)
cd api-clinica-profissionais-saude

# 2. Criar e sincronizar o ambiente virtual
uv sync

# 3. Executar o servidor
uv run uvicorn src.main:app --reload
```

Usando `pip`
```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux / macOS
python3 -m venv .venv
source .venv/bin/activate

# Instalar dependências e executar
pip install -r requirements.txt
uvicorn src.main:app --reload
```

A API estará disponível no endereço: `http://127.0.0.1:8000`

---

## Principais Endpoints

A documentação interativa gerada pelo Swagger pode ser acessada em `http://127.0.0.1:8000/docs`.

|Método|Rota|Descrição|Parâmetros|
|---|---|---|---|
|**GET**|`/`|Status da Aplicação|N/A|
|**GET**|`/api/v1/especialidades`|Lista todas as especialidades|N/A|
|**GET**|`/api/v1/profissionais`|Lista todos os profissionais|`nome`,`especialidade`|
|**GET**|`/api/v1/profissionais/{id}`|Retorna um profissional pelo ID|N/A|

---

## Planejamento do Projeto

O planejamento de execução seguiu a Estrutura Analítica do Projeto definida no **Marco 1**:

* **Marco 1**: Elaboração da EAP e planejamento da API
* **Marco 2**: Implementação da Leitura do arquivo local e dos filtros de nome e especialidade para os profissionais
* **Marco 3**: Refinamento do código, documentação, publicação no GitHub e gravação do vídeo.

A EAP elaborada se encontra em [`docs`](./docs/).

---