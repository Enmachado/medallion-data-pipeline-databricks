# 📊 Data Pipeline com Databricks (Arquitetura Medallion)

Este projeto implementa um pipeline de dados end-to-end utilizando o Databricks, seguindo a arquitetura Medallion (Bronze, Silver e Gold). O objetivo é demonstrar boas práticas de engenharia de dados, desde a ingestão até a disponibilização de dados para análise.

---

## 🚀 Visão Geral

O pipeline realiza:

- Ingestão de dados a partir de uma API
- Processamento e transformação dos dados
- Organização em camadas (Bronze, Silver e Gold)
- Disponibilização de dados prontos para análise

Todo o fluxo é executado e orquestrado dentro do Databricks.

---

## 🏗️ Arquitetura

O projeto segue o padrão Medallion Architecture:

### 🥉 Bronze Layer (Raw Data)
- Ingestão de dados brutos via API
- Armazenamento sem transformação
- Preservação dos dados originais

### 🥈 Silver Layer (Cleaned Data)
- Limpeza e tratamento dos dados
- Padronização de formatos
- Remoção de inconsistências

### 🥇 Gold Layer (Curated Data)
- Dados refinados e agregados
- Estruturados para análise
- Prontos para consumo por dashboards

---

## ⚙️ Tecnologias Utilizadas

- Databricks  
- Python  
- Apache Spark  
- APIs REST  
- Git e GitHub  

---

## 🔄 Orquestração

O pipeline foi dividido em tarefas interdependentes, garantindo:

- Execução sequencial das etapas
- Monitoramento de execução
- Visualização do fluxo
- Possibilidade de agendamento automático

---

## 📁 Estrutura do Projeto
