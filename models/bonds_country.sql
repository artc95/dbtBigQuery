{{
  config(
    materialized = "table"
  )
}}

with bonds as (
  select ISIN, coupon__, last_price, maturity_date 
  
  from dbt-bigquery-423209.dbtBigQuery.degiro_bonds_20240513_1540
),

bonds_country as (
  select substring(ISIN, 1, 2) as country_iso_alpha2, count(*) as country_count

  from bonds
  group by country_iso_alpha2
  order by country_count desc
)

select * from bonds_country