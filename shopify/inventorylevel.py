import pandas as pd
import requests


# def get_shopify_api(shopify_access_token, shopify_url)
def get_Locations(shopify_access_token):
    # get list of Locations details, via API GET request
    url = 'https://0588b9.myshopify.com/admin/api/2024-04/locations.json'
    headers = {'X-Shopify-Access-Token': shopify_access_token, 'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    
    locations_json = r.json()
    locations_list = locations_json['locations']

    return locations_list

def get_InventoryLevels(locations_list, shopify_access_token):
    # get list of InventoryLevels, via API GET request
    url = 'https://0588b9.myshopify.com/admin/api/2024-04/inventory_levels.json?location_ids=95427658037'
    headers = {'X-Shopify-Access-Token': shopify_access_token, 'content-type': 'application/json'}
    r = requests.get(url, headers=headers)

    inventory_levels = r.json()
    inventory_levels_list = inventory_levels['inventory_levels']
    print(f'arthur inventorylevels: {inventory_levels_list}')

    return inventory_levels_list

def get_Products(shopify_access_token):
    # get list of InventoryLevels, via API GET request
    url = 'https://0588b9.myshopify.com/admin/api/2024-04/products.json'
    headers = {'X-Shopify-Access-Token': shopify_access_token, 'content-type': 'application/json'}
    r = requests.get(url, headers=headers)

    products = r.json()
    products_list = products['products']
    print(f'arthur products: {products_list}')
    return products_list

def to_csv(list_of_dicts: list, output_name: str,
           sort_by: list, sort_asc: bool):
    """
    converts a list of dicts, to a .csv file!
    list_of_dicts: e.g. [
        {'inventory_item_id': 49661765812533, 'location_id': 95427658037, 'available': 1}, 
        {'inventory_item_id': 49661765550389, 'location_id': 95427658037, 'available': 1}, 
        {'inventory_item_id': 49592716230965, 'location_id': 95427658037, 'available': 1}
        ]
    sort_by: e.g. ['inventory_item_id']
    """
    df = pd.DataFrame(list_of_dicts)
    df = df.sort_values(by=sort_by, ascending=sort_asc)

    df.to_csv(f'{output_name}.csv', index=False)
    print(f'{output_name}.csv successfully created!')


shopify_access_token = <token>

locations_list = get_Locations(shopify_access_token)
to_csv(locations_list, 'locations', ['id'], sort_asc=False)

inventory_levels_list = get_InventoryLevels(locations_list, shopify_access_token)
products_list = get_Products(shopify_access_token)