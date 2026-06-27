SELECT
    region_name,
    region_code,
    quarter_date,
    level,
    MAX(CASE WHEN metric = 'unemployment_persons' THEN value END) AS unemployment_persons,
    MAX(CASE WHEN metric = 'labour_force_persons' THEN value END) AS labour_force_persons,
    MAX(CASE WHEN metric = 'unemployment_rate' THEN value END) AS unemployment_rate,
    RANK() OVER (PARTITION BY quarter_date, level ORDER BY unemployment_rate DESC NULLS LAST) AS unemployment_rank
FROM {{ ref('stg_combined_salm') }}
GROUP BY region_name, region_code, quarter_date, level