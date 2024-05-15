import requests


def get_locations(shopify_access_token):
    # get list of Locations details, via API GET request
    url = 'https://0588b9.myshopify.com/admin/api/2024-04/locations.json'
    headers = {'X-Shopify-Access-Token': shopify_access_token, 'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    
    locations_json = r.json()
    locations_list = locations_json['locations']

    # extract key Locations details, store as dict of dicts (key is Location id, value is dict of Locations details)
    locations_dict = {}
    for location in locations_list:
        location_id = location['id']
        locations_dict[location_id] = { key: location[key] for key in ['active', 'city', 'country', 'country_code', 'created_at', 
                                                    'id', 'name', 'updated_at']}
    # print(locations_dict)
    return locations_dict

def get_inventoryLevel(locations_dict, shopify_access_token):
    # get list of InventoryLevels, via API GET request
    url = 'https://0588b9.myshopify.com/admin/api/2024-04/inventory_levels.json?location_ids=95427658037'
    headers = {'X-Shopify-Access-Token': shopify_access_token, 'content-type': 'application/json'}
    r = requests.get(url, headers=headers)

    inventory_levels = r.json()
    inventory_levels = inventory_levels['inventory_levels']
    print(inventory_levels)



shopify_access_token = <shopify_access_token>
locations_dict = get_locations(shopify_access_token)
inventory_levels = get_inventoryLevel(locations_dict, shopify_access_token)