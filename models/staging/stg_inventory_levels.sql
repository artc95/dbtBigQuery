with staged as (

    select * from {{ source("dbtBigQuery", "inventory_levels") }}

)

select * from staged