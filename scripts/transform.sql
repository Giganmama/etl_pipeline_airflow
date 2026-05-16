-- Пример трансформации с оконными функциями и CTE
WITH daily_metrics AS (
    SELECT 
        date_trunc('day', created_at) as report_date,
        region_id,
        product_category,
        COUNT(DISTINCT order_id) as orders_cnt,
        SUM(revenue) as total_revenue,
        AVG(revenue) as avg_order_value,
        LAG(SUM(revenue)) OVER (
            PARTITION BY region_id 
            ORDER BY date_trunc('day', created_at)
        ) as prev_day_revenue
    FROM raw_orders
    WHERE status = 'completed'
    GROUP BY 1, 2, 3
),
dq_checks AS (
    SELECT 
        *,
        CASE WHEN total_revenue IS NULL THEN 1 ELSE 0 END as has_null_revenue,
        CASE WHEN orders_cnt = 0 THEN 1 ELSE 0 END as zero_orders_flag
    FROM daily_metrics
)
SELECT * FROM dq_checks;
