WITH filtered AS (
    SELECT *
    FROM {{ source('raw', 'combined_salm_data') }}
    WHERE quarter IS NOT NULL
    AND quarter != 'Unnamed: 64'
)

SELECT
    CASE
        WHEN metric = 'Smoothed unemployment (persons)' THEN 'unemployment_persons'
        WHEN metric = 'Smoothed labour force (persons)' THEN 'labour_force_persons'
        WHEN metric = 'Smoothed unemployment rate (%)' THEN 'unemployment_rate'
    END AS metric,
    region_name,
    region_code,
    TRY_TO_DATE('01-' || quarter, 'DD-MON-YY') AS quarter_date,
    TRY_CAST(REPLACE(value, ',', '') AS FLOAT) AS value,
    level
FROM filtered