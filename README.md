# 🚀 ETL Pipeline | Airflow + PostgreSQL + Data Quality

Production-ready ETL-пайплайн для ежедневной загрузки и трансформации данных из внешних источников в аналитическое хранилище. Реализован с использованием **Apache Airflow 2.x**, **Python** и **SQL**, с встроенными проверками качества данных и механизмами идемпотентности.

## 🏗 Архитектура
```mermaid
graph LR
  A[Source API / CSV] --> B[Extract Layer]
  B --> C[Transform Layer]
  C --> D[Data Quality Checks]
  D --> E[Load to PostgreSQL]
  E --> F[BI / Downstream]
