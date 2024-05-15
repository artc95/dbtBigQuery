import requests


def get_Locations():
    # get Locations details via API GET request
    url = 'https://0588b9.myshopify.com/admin/api/2024-04/locations.json'
    headers = {'X-Shopify-Access-Token': <ShopifyAccessToken>, 'content-type': 'application/json'}
    r = requests.get(url, headers=headers)
    
    locations_json = r.json()
    locations_list = locations_json['locations']

    for location in locations_list:
        location = { key: location[key] for key in ['active', 'city', 'country', 'country_code', 'created_at', 
                                                    'id', 'name', 'updated_at']}
        print(location)


get_Locations()