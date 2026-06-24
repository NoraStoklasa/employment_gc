# Gold Coast Labour Market Pipeline

A data pipeline that analyses 15 years of quarterly unemployment data
(Dec 2010 – Dec 2025) across Gold Coast suburbs. Data comes from the
Department of Employment and Workplace Relations' Small Area Labour
Markets (SALM) series.

## Data

Two CSVs, stored in `data/raw/`:

- **SA2-level file (primary)** — ~28 Gold Coast suburb regions
  (e.g. Southport, Surfers Paradise, Robina, Coomera, Helensvale,
  Burleigh Heads).
- **LGA-level file (benchmark)** — Gold Coast as one region, used to
  compare suburb trends against the city-wide trend.

Each file has three measures per quarter: smoothed unemployment
(persons), smoothed labour force (persons), and smoothed unemployment
rate (%).

**Things to know about the data:**
- It's 4-quarter smoothed, so it shows trends, not sharp
  quarter-to-quarter changes.
- Areas with a labour force under 1,000 people are more volatile —
  treat those numbers with caution.
- The SA2 file uses 2021 region boundaries, the LGA file uses 2025
  boundaries. This matters when comparing the two.

## Tech stack

- **Python** — extracts and reshapes the raw data
- **AWS S3** — stores the data
- **AWS Lambda** — automates parts of the pipeline
- **CloudFormation** — defines the AWS infrastructure as code
- **Snowflake** — data warehouse
- **dbt-core** — transforms and tests the data
- **Power BI** — final dashboard
- **GitLab CI/CD** — runs dbt tests automatically on every push

## Pipeline architecture

See [docs/pipeline-diagram.svg](docs/pipeline-diagram.svg).

```
SALM CSVs (data/raw/)
    -> Python (filter to Gold Coast, reshape wide -> long)
    -> S3
    -> Snowflake (RAW layer)
    -> dbt (staging -> intermediate -> marts)
    -> Power BI dashboard
```

## Project status

This project is being built step by step. Right now:

- [x] Raw data sourced and added to `data/raw/`
- [x] Folder structure set up
- [ ] Python ingestion script
- [ ] AWS (S3, Lambda, CloudFormation)
- [ ] Snowflake ingestion
- [ ] dbt models and tests
- [ ] Power BI dashboard
- [ ] GitLab CI/CD

## How to run

Not runnable yet — the pipeline is still being built. This section
will be filled in once the Python ingestion step works end to end.
