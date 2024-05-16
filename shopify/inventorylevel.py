import pandas as pd
import requests


def request_shopifyAPI(shopify_domain_id: str, shopify_access_token: str,
                       endpoint: str, parameters: str):
    """
    request Shopify API, extract list of dicts from response!
    - endpoint e.g. "locations"
    - r_json e.g. {
        "locations": [{"name": "50 Rideau Street"}, {"name": "Apple Api Shipwire"}, {"name": "Apple Cupertino"}]
        }
    - r_list e.g. [{"name": "50 Rideau Street"}, {"name": "Apple Api Shipwire"}, {"name": "Apple Cupertino"}]
    """

    url = f"https://{shopify_domain_id}.myshopify.com/admin/api/2024-04/{endpoint}.json{parameters}"
    headers = {"X-Shopify-Access-Token": shopify_access_token, "content-type": 'application/json'}
    r = requests.get(url, headers=headers)
    r_json = r.json() # dict with endpoint as key, list of dicts as value
    r_list = r_json[endpoint]  # extract list of dicts from json

    return r_list

def to_csv(list_of_dicts: list, output_name: str,
           sort_by: list, sort_asc: bool):
    """
    converts a list of dicts, to a .csv file!
    - list_of_dicts: e.g. [{"name": "50 Rideau Street"}, {"name": "Apple Api Shipwire"}, {"name": "Apple Cupertino"}]
    - sort_by: e.g. ['inventory_item_id']
    """
    df = pd.DataFrame(list_of_dicts)
    df = df.sort_values(by=sort_by, ascending=sort_asc)

    df.to_csv(f'{output_name}.csv', index=False)
    print(f'{output_name}.csv successfully created!')

def get_endpoints_csvs(shopify_domain_id: str, shopify_access_token: str,
                       endpoints_dict: dict):
    """
    request Shopify API and convert to .csv, using dict of endpoints and specifications
    - endpoints_dict e.g. {"locations": {"parameters": "", "sort_by": "id", "sort_asc": True}, 
                           "inventory_levels": {"parameters": "a", "sort_by": "inventory_item_id", "sort_asc": True}}
    """

    for endpoint in endpoints_dict.keys():
        # unpack values of dict for each endpoint
        parameters, sort_by, sort_asc = endpoints_dict[endpoint].values()
        
        list_of_dicts = request_shopifyAPI(shopify_domain_id, shopify_access_token, 
                                           endpoint, parameters)
        to_csv(list_of_dicts, endpoint, sort_by, sort_asc)

shopify_domain_id = '0588b9'
shopify_access_token = <token>
endpoints_dict = {
    "locations": {"parameters": "", "sort_by": "id", "sort_asc": True}, 
    # TODO: SEQUENTIAL DEPENDENCY e.g. inventory_levels should take in location_ids from locations
    "inventory_levels": {"parameters": "?location_ids=95427658037", "sort_by": "inventory_item_id", "sort_asc": True},
    "products": {"parameters": "", "sort_by": "title", "sort_asc": True}
    }

# create .csvs for multiple endpoints
get_endpoints_csvs(shopify_domain_id, shopify_access_token, endpoints_dict)