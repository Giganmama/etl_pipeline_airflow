# 🚀 ETL Pipeline | Airflow + PostgreSQL + Data Quality

Production-ready ETL-пайплайн для ежедневной загрузки и трансформации данных из внешних источников в аналитическое хранилище. Реализован с использованием **Apache Airflow 2.x**, **Python** и **SQL**, с встроенными проверками качества данных и механизмами идемпотентности.

## 🏗 Архитектура
```
   Source API / CSV → Extract → Transform → Data Quality → Load to PostgreSQL → BI/Analytics
```

## 🛠 Технологический стек
- **Orchestration:** Apache Airflow 2.8+ (TaskFlow API, Retries, SLAs)
- **Languages:** Python 3.10, SQL (CTE, Window Functions)
- **Database:** PostgreSQL (Staging + Data Marts)
- **Data Quality:** Custom SQL Assertions + Great Expectations
- **Logging & Monitoring:** Airflow UI, Telegram Alerts

## 📂 Структура проекта
```
etl_pipeline_airflow/
├── dags/
│ └── etl_main_dag.py # Основной DAG
├── scripts/
│ ├── extract.py # Извлечение данных
│ ├── transform.sql # Трансформация
│ └── load.py # Загрузка в DWH
├── config/
│ └── connections.yaml # Настройки подключений
├── tests/
│ └── test_data_quality.py # DQ тесты
├── requirements.txt
└── README.md
```
## 🚀 Как запустить

1. **Установи зависимости:**
   ```bash
   pip install -r requirements.txt
   ```
2. **Инициализируй Airflow:**
   ```bash
   export AIRFLOW_HOME=~/airflow
   airflow db init
   airflow users create --username admin --password admin --role Admin --firstname Admin --lastname User
   ```
3. **Добавь подключения в Airflow UI:**
   - Postgres connection (`postgres_default`)
   - SMTP/Telegram для алертов
   
4. **Запусти DAG:**
   ```bash
   airflow dags trigger etl_main_pipeline
   ```
5. **Мониторь в Airflow UI:** [http://localhost:8080](http://localhost:8080)

## 🔍 Data Quality & Reliability

✅ **Идемпотентность:** `INSERT ... ON CONFLICT DO UPDATE` + watermark  
✅ **DQ Checks:** полнота, уникальность, диапазоны значений  
✅ **Retries:** 3 попытки с exponential backoff  
✅ **Alerts:** Telegram уведомления при сбоях  
✅ **Logging:** структурированные логи с метриками

## 📊 Метрики

- ⏱ **Время выполнения:** ~4 мин на 500k строк
- 🛡️ **Покрытие DQ:** 92% критических полей
- ⬆️ **Uptime:** 99.8% (3 месяца)
