SELECT
    CASE WHEN region_name = 'Unincorporated ACT' THEN 'Canberra' ELSE region_name END AS region_name,
    region_code,
    quarter_date,
    TO_CHAR(quarter_date, 'Mon YYYY') AS period,
    YEAR(quarter_date) AS year,
    level,
    CASE WHEN level = 'sa2' THEN TRUE ELSE FALSE END AS is_gold_coast_sa2,
    unemployment_persons,
    labour_force_persons,
    unemployment_rate,
    unemployment_rank,
    unemployment_rate_prev_year,
    yoy_change,
    avg_unemployment_rate,
    diff_from_avg
FROM {{ ref('int_combined_salm') }}