with inventory_levels as (
  select *
  from {{ ref("stg_inventory_levels") }}
),

locations as (
  select location_id, location_name
  from {{ ref("stg_locations") }}
),

products as (
  select sku, product_id, position, inventory_item_id
  from {{ ref("stg_products") }}
)

select 
    products.sku, available, products.product_id, products.position, 
    inventory_levels.inventory_item_id,
    inventory_levels.location_id, locations.location_name
from inventory_levels
left join locations on inventory_levels.location_id = locations.location_id
left join products on inventory_levels.inventory_item_id = products.inventory_item_id
order by product_id, position
