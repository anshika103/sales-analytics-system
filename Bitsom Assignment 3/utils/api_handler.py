import requests

def get_product_info(product_id):
    """
    Fetches product details from an API. 
    Note: Real-world IDs would map to specific API endpoints.
    """
    # Using a sample public API for demonstration
    url = f"https://fakestoreapi.com/products/{product_id.replace('P', '')}"
    try:
        response = requests.get(url, timeout=5)
        if response.status_code == 200:
            return response.json()
        return None
    except Exception as e:
        print(f"API Error: {e}")
        return None