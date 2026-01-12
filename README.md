# 🌦️ Weather Data ETL & API Challenge

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-009688?style=for-the-badge&logo=fastapi)
![Pytest](https://img.shields.io/badge/Tests-Pytest-green?style=for-the-badge&logo=pytest)
![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192?style=for-the-badge&logo=postgresql)

Este projeto é uma solução completa de **Engenharia de Dados, Backend e Cloud-Native Applications**, desenvolvida como parte de um desafio técnico.

O objetivo é demonstrar competências em **extração de dados (ETL)**, **armazenamento relacional**, **desenvolvimento de APIs RESTful**, **testes automatizados** e **orquestração de infraestrutura com Docker**.

---

## 📋 Arquitetura da Solução

A aplicação foi desenhada seguindo o padrão de **serviços conteinerizados**, priorizando a separação de responsabilidades e a reprodutibilidade do ambiente.

O fluxo de dados funciona da seguinte maneira:

1. **Extração (ETL):**
   Ao iniciar a aplicação, um processo independente executa a extração de dados climáticos consumindo a API da OpenWeatherMap. Implementa lógica de **Retry** e **Logging estruturado** para resiliência.

2. **Transformação e Armazenamento:**
   Os dados são tratados, normalizados e persistidos em um banco de dados **PostgreSQL**, garantindo integridade e consistência transacional.

3. **Exposição via API:**
   Uma API desenvolvida em **FastAPI** disponibiliza os dados armazenados por meio de endpoints HTTP documentados, utilizando **Schemas (Pydantic)** para validação de contratos.

4. **Infraestrutura:**
   Toda a solução é orquestrada via **Docker Compose**, garantindo que a aplicação e o banco de dados subam na mesma rede, na ordem correta e de forma totalmente reproduzível.

---

## 🗄️ Modelo de Dados

A tabela principal (`weather_logs`) armazena as informações climáticas normalizadas:

| Coluna | Tipo | Descrição |
|------|------|-----------|
| `id` | Integer | Chave primária |
| `city` | String | Nome da cidade consultada |
| `temperature` | Float | Temperatura em graus Celsius |
| `humidity` | Integer | Umidade relativa do ar (%) |
| `description` | String | Descrição do clima (ex: "céu limpo") |
| `collected_at` | DateTime | Timestamp da coleta |

---

## 🚀 Como Executar o Projeto

### Pré-requisitos
- Docker e Docker Compose instalados.
- Uma chave de API gratuita da OpenWeatherMap.

### Passo a Passo

```bash
git clone https://github.com/VictorTavaresRafael/weather-challenge.git
cd weather-challenge
```

Crie um arquivo `.env` na raiz do projeto:

```env
OPENWEATHER_API_KEY=sua_chave_aqui
DATABASE_URL=postgresql://user:password@db:5432/weatherdb
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_DB=weatherdb
```

Suba a aplicação:

```bash
docker-compose up --build
```

---

## 🧪 Qualidade de Código e Testes

Execute os testes com:

```bash
docker-compose exec web pytest -v
```

---

## 📚 Documentação da API

- Swagger UI: http://localhost:8000/docs
- Redoc: http://localhost:8000/redoc

---

## 🛠️ Decisões Técnicas

- **FastAPI**: Performance e documentação automática  
- **SQLAlchemy**: ORM seguro e flexível  
- **Docker Compose**: Ambiente reproduzível  
- **Logging estruturado**  
- **Variáveis de ambiente (.env)**

---

## 🔮 Melhorias Futuras

- [ ] Agendador de tarefas (Cron/Celery)
- [ ] Cache com Redis
- [ ] ETL como microserviço

---

Desenvolvido por **Víctor Matheus Tavares Rafael**
