# 🌦️ Weather Data ETL & API Challenge

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192?style=for-the-badge&logo=postgresql)

Este projeto é uma solução completa de Engenharia de Software e Dados, desenvolvida como parte de um desafio técnico. O objetivo é demonstrar competências em **extração de dados (ETL)**, **armazenamento relacional**, **desenvolvimento de APIs RESTful** e **orquestração de infraestrutura com Docker**.

---

## 📋 Arquitetura da Solução

A aplicação foi desenhada seguindo o padrão de microsserviços conteinerizados. O fluxo de dados funciona da seguinte maneira:

1.  **Extração (ETL):** Ao iniciar, um script Python consome a API da OpenWeatherMap.
2.  **Armazenamento:** Os dados extraídos são tratados e persistidos em um banco de dados **PostgreSQL**.
3.  **Exposição:** Uma API desenvolvida em **FastAPI** expõe esses dados através de endpoints HTTP documentados.
4.  **Infraestrutura:** Tudo é orquestrado via **Docker Compose**, garantindo que a aplicação e o banco subam na mesma rede e na ordem correta.

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
* [Docker](https://www.docker.com/) e [Docker Compose](https://docs.docker.com/compose/) instalados.
* Uma chave de API (API Key) gratuita da [OpenWeatherMap](https://openweathermap.org/).

### Passo a Passo

1.  **Clone o repositório:**
    ```bash
    git clone [https://github.com/SEU_USUARIO/weather-challenge.git](https://github.com/SEU_USUARIO/weather-challenge.git)
    cd weather-challenge
    ```

2.  **Configure as Variáveis de Ambiente:**
    Por questões de segurança, chaves de API e senhas não são versionadas. Crie um arquivo chamado `.env` na raiz do projeto e preencha conforme o exemplo abaixo:

    ```env
    # Arquivo: .env
    OPENWEATHER_API_KEY=sua_chave_api_aqui
    DATABASE_URL=postgresql://user:password@db:5432/weatherdb
    POSTGRES_USER=user
    POSTGRES_PASSWORD=password
    POSTGRES_DB=weatherdb
    ```

3.  **Suba a aplicação:**
    Execute o comando abaixo para construir as imagens e iniciar os containers:
    ```bash
    docker-compose up --build
    ```

    > **Nota:** O sistema aguardará o banco de dados estar pronto, executará a extração dos dados (ETL) automaticamente e, em seguida, iniciará a API.

---

## 📚 Documentação da API

Uma das vantagens do uso do FastAPI é a geração automática de documentação interativa (Swagger UI).

Após subir os containers, acesse:

* **Swagger UI (Documentação Interativa):** [http://localhost:8000/docs](http://localhost:8000/docs)
* **Redoc (Documentação Alternativa):** [http://localhost:8000/redoc](http://localhost:8000/redoc)

### Endpoints Principais

| Método | Endpoint | Descrição |
| :--- | :--- | :--- |
| `GET` | `/` | Health check da API. |
| `GET` | `/weather` | Retorna a lista de dados climáticos armazenados no banco. |

---

## 📂 Estrutura do Projeto

A organização de pastas segue as boas práticas de separação de responsabilidades:

```text
weather-challenge/
├── app/
│   ├── __init__.py
│   ├── main.py          # Definição dos Endpoints (Controller)
│   ├── models.py        # Modelagem das tabelas (ORM / SQLAlchemy)
│   ├── database.py      # Configuração da conexão com o Banco
│   └── etl.py           # Script de Extração e Carga (ETL)
├── Dockerfile           # Definição da imagem da aplicação
├── docker-compose.yml   # Orquestração dos serviços (App + DB)
├── requirements.txt     # Dependências do projeto Python
├── .env                 # Variáveis de ambiente (Ignorado pelo Git)
└── README.md            # Documentação do projeto
