from airflow import DAG
from airflow.decorators import task
from datetime import timedelta, datetime
import logging

default_args = {
    "owner": "danila_babenko",
    "depends_on_past": False,
    "email_on_failure": False,
    "email_on_retry": False,
    "retries": 3,
    "retry_delay": timedelta(minutes=5),
}

with DAG(
    dag_id="etl_main_pipeline",
    default_args=default_args,
    description="ETL pipeline с DQ проверками и идемпотентной загрузкой",
    schedule_interval="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    tags=["etl", "production", "data_quality"],
) as dag:

    @task
    def extract_data():
        """Загрузка сырых данных из источника (API/CSV/DB)"""
        logging.info("📥 Extract: начинаем загрузку данных...")
        # Здесь логика получения данных
        # Пример: response = requests.get(API_URL).json()
        # kwargs["ti"].xcom_push(key="raw_data", value=response)
        return {"status": "extracted", "rows": 15000}

    @task
    def transform_data(raw_data):
        """Очистка, нормализация, бизнес-правила"""
        logging.info("🔄 Transform: применяем бизнес-логику...")
        # Пример: df = pd.DataFrame(raw_data).dropna()
        # df["revenue"] = df["price"] * df["quantity"]
        return {"status": "transformed", "clean_rows": 14800}

    @task
    def data_quality_checks(transformed_data):
        """Проверки качества перед загрузкой"""
        logging.info("✅ DQ Checks: валидация данных...")
        rules = [
            transformed_data["clean_rows"] > 0,
            # add more checks: uniqueness, ranges, schema validation
        ]
        assert all(rules), "❌ Data Quality checks failed!"
        logging.info("✅ Все DQ проверки пройдены")
        return transformed_data

    @task
    def load_to_dwh(validated_data):
        """Идемпотентная загрузка в PostgreSQL/ClickHouse"""
        logging.info("💾 Load: загрузка в витрину...")
        # Пример SQL:
        # INSERT INTO mart_sales (id, date, revenue)
        # SELECT ... ON CONFLICT (id, date) DO UPDATE SET ...
        return {"status": "loaded", "target_table": "mart_sales"}

    # Оркестрация
    raw = extract_data()
    cleaned = transform_data(raw)
    checked = data_quality_checks(cleaned)
    loaded = load_to_dwh(checked)

    raw >> cleaned >> checked >> loaded
