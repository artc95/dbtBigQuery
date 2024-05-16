with staged as (

    select 
        id as location_id,
        name as location_name,
        created_at,
        country_code as location_code,
        active
    
    from {{ source("dbtBigQuery", "locations") }}

)

select * from staged