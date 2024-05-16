with staged as (

    select product_id, sku, position, created_at, inventory_item_id
    from {{ source("dbtBigQuery", "products") }}

)

select * from staged