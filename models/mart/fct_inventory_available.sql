with inventory_levels as (
  select *
  from {{ ref("stg_inventory_levels") }}
),

locations as (
  select *
  from {{ ref("stg_locations") }}
),

products as (
  select *
  from {{ ref("stg_products") }}
)

select sku, available, product_id, position, inventory_levels.inventory_item_id
from inventory_levels
left join locations on inventory_levels.location_id = locations.location_id
left join products on inventory_levels.inventory_item_id = products.inventory_item_id
order by product_id, position
