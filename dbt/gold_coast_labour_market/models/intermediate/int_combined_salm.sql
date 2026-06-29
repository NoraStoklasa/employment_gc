SELECT
    region_name,
    region_code,
    quarter_date,
    level,
    MAX(CASE WHEN metric = 'unemployment_persons' THEN value END) AS unemployment_persons,
    MAX(CASE WHEN metric = 'labour_force_persons' THEN value END) AS labour_force_persons,
    MAX(CASE WHEN metric = 'unemployment_rate' THEN value END) AS unemployment_rate,

    -- Rank suburbs from highest to lowest unemployment rate within each quarter and level (sa2 vs lga)
    RANK() OVER (PARTITION BY quarter_date, level ORDER BY unemployment_rate DESC NULLS LAST) AS unemployment_rank,

    -- Unemployment rate from the same quarter one year ago (4 quarters back)
    LAG(unemployment_rate, 4) OVER (PARTITION BY region_code ORDER BY quarter_date) AS unemployment_rate_prev_year,

    -- Change in unemployment rate compared to same quarter last year (positive = got worse, negative = improved)
    unemployment_rate - LAG(unemployment_rate, 4) OVER (PARTITION BY region_code ORDER BY quarter_date) AS yoy_change,

    -- Average unemployment rate across all regions in the same quarter and level
    AVG(unemployment_rate) OVER (PARTITION BY quarter_date, level) AS avg_unemployment_rate,

    -- How far above or below the average this region is (positive = worse than average, negative = better)
    unemployment_rate - AVG(unemployment_rate) OVER (PARTITION BY quarter_date, level) AS diff_from_avg

FROM {{ ref('stg_combined_salm') }}
GROUP BY region_name, region_code, quarter_date, level