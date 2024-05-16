import pandas as pd
import requests


def request_shopifyAPI(shopify_domain_id: str, shopify_access_token: str,
                       item: str, endpoint: str):
    """
    request Shopify API, extract list of dicts from response!
    - item e.g. "locations"
    - endpoint e.g. "locations.json"
    - r_json e.g. {
        "locations": [{"name": "50 Rideau Street"}, {"name": "Apple Api Shipwire"}, {"name": "Apple Cupertino"}]
        }
    - r_list e.g. [{"name": "50 Rideau Street"}, {"name": "Apple Api Shipwire"}, {"name": "Apple Cupertino"}]
    """

    url = f"https://{shopify_domain_id}.myshopify.com/admin/api/2024-04/{endpoint}"
    headers = {"X-Shopify-Access-Token": shopify_access_token, "content-type": 'application/json'}
    r = requests.get(url, headers=headers)
    r_json = r.json() # dict with endpoint as key, list of dicts as value
    r_list = r_json[item]  # extract list of dicts from json

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

def get_ids_to_variants(shopify_domain_id, shopify_access_token, list_of_product_dicts):
    
    """
    get list of all product_ids, to get product_variants data
    - list_of_product_dicts e.g. [
        {"id": 1, "variants": [{"inventory_item_id": 341629}, {"inventory_item_id": 012345}]},
        {"id": 2, "variants": [{"inventory_item_id": 538194}]}
        ]
    """
    list_product_ids = [product["id"] for product in list_of_product_dicts]
            
    list_of_variants_dicts = []
    for product_id in list_product_ids:
        # for each product_id, get list of dicts of all its variants
        variants = request_shopifyAPI(shopify_domain_id, shopify_access_token, 
                                      item="variants",
                                      endpoint=f"products/{product_id}/variants.json")
        for variant in variants:
            list_of_variants_dicts.append(variant)
    
    return list_of_variants_dicts



def get_endpoints_csvs(shopify_domain_id: str, shopify_access_token: str,
                       endpoints_dict: dict):
    """
    request Shopify API and convert to .csv, using dict of endpoints and specifications
    - endpoints_dict e.g. {
        "locations": {"endpoint": "locations.json", "sort_by": "id", "sort_asc": True}, 
        "products": {"endpoint": "products.json", "sort_by": ["product_id", "position"], "sort_asc": True}
        }
    """

    for item in endpoints_dict.keys():
        # unpack values of dict for each endpoint
        endpoint, sort_by, sort_asc = endpoints_dict[item].values()
        
        list_of_dicts = request_shopifyAPI(shopify_domain_id, shopify_access_token,
                                           item, endpoint)
        if item == "products":
            # extra step, bcause BigQuery cannot handle dicts as cell values??
            list_of_dicts = get_ids_to_variants(shopify_domain_id, shopify_access_token, list_of_dicts)

        to_csv(list_of_dicts, item, sort_by, sort_asc)


shopify_domain_id = '0588b9'
shopify_access_token = <token>
endpoints_dict = {
    "locations": {"endpoint": "locations.json", "sort_by": "id", "sort_asc": True}, 
    # TODO: SEQUENTIAL DEPENDENCY e.g. inventory_levels should take in location_ids from locations
    "inventory_levels": {"endpoint": "inventory_levels.json?location_ids=95391711541", "sort_by": "inventory_item_id", "sort_asc": True},
    "products": {"endpoint": "products.json", "sort_by": ["product_id", "position"], "sort_asc": True}
    }

# create .csvs for multiple endpoints
get_endpoints_csvs(shopify_domain_id, shopify_access_token, endpoints_dict)