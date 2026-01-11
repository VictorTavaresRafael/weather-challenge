# 🌦️ Weather Data ETL & API Challenge

![Python](https://img.shields.io/badge/Python-3.9-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-0.68-009688?style=for-the-badge&logo=fastapi)
![Docker](https://img.shields.io/badge/Docker-20.10-2496ED?style=for-the-badge&logo=docker)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-316192?style=for-the-badge&logo=postgresql)

Este projeto é uma solução completa de **Engenharia de Dados, Backend e
Cloud-Native Applications**, desenvolvida como parte de um desafio
técnico.\
O objetivo é demonstrar competências em **extração de dados (ETL)**,
**armazenamento relacional**, **desenvolvimento de APIs RESTful** e
**orquestração de infraestrutura com Docker**.

------------------------------------------------------------------------

## 📋 Arquitetura da Solução

A aplicação foi desenhada seguindo o padrão de **serviços
conteinerizados**, priorizando separação de responsabilidades e
reprodutibilidade de ambiente.

O fluxo de dados funciona da seguinte maneira:

1.  **Extração (ETL):**\
    Ao iniciar a aplicação, um processo independente executa a extração
    de dados climáticos consumindo a API da OpenWeatherMap.

2.  **Transformação e Armazenamento:**\
    Os dados são tratados, normalizados e persistidos em um banco de
    dados **PostgreSQL**, garantindo integridade e consistência.

3.  **Exposição via API:**\
    Uma API desenvolvida em **FastAPI** disponibiliza os dados
    armazenados por meio de endpoints HTTP documentados.

4.  **Infraestrutura:**\
    Toda a solução é orquestrada via **Docker Compose**, garantindo que
    a aplicação e o banco de dados subam na mesma rede, na ordem correta
    e de forma totalmente reproduzível.

> 🔎 **Observação:**\
> Embora o ETL e a API estejam no mesmo container por simplicidade, o
> ETL é executado como um **processo independente**, respeitando o
> princípio de **separação de responsabilidades**.

------------------------------------------------------------------------

## 🗄️ Modelo de Dados

A tabela principal armazena informações climáticas normalizadas,
incluindo:

-   `city`
-   `temperature`
-   `humidity`
-   `weather_description`
-   `timestamp`

------------------------------------------------------------------------

## 🚀 Como Executar o Projeto

### Pré-requisitos

-   Docker e Docker Compose instalados
-   Uma chave de API gratuita da OpenWeatherMap

### Passo a Passo

1.  Clone o repositório:

    ``` bash
    git clone https://github.com/VictorTavaresRafael/weather-challenge
    cd weather-challenge
    ```

2.  Configure as variáveis de ambiente criando um arquivo `.env` na raiz
    do projeto.

3.  Suba a aplicação:

    ``` bash
    docker-compose up --build
    ```

------------------------------------------------------------------------

## 📚 Documentação da API

Após subir os containers, acesse:

-   Swagger UI: http://localhost:8000/docs
-   Redoc: http://localhost:8000/redoc

------------------------------------------------------------------------

## 🛠️ Decisões Técnicas

FastAPI, SQLAlchemy, Docker Compose e variáveis de ambiente foram
utilizados para garantir performance, segurança e reprodutibilidade.

------------------------------------------------------------------------

## 🔮 Melhorias Futuras

-   Testes unitários
-   Agendador de ETL
-   Cache com Redis
-   Separação do ETL em serviço dedicado

------------------------------------------------------------------------

**Desenvolvido por Víctor Matheus Tavares Rafael**
