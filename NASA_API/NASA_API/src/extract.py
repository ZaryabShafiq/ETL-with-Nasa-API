import requests
from config import BASE_URL, API_KEY

def fetch_neo_data(start_date, end_date, logger):
    """Fetch data from NASA API."""
    params = {
        "start_date": start_date,
        "end_date": end_date,
        "api_key": API_KEY
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        logger.info(f"Successfully fetched data for {start_date} to {end_date}")
        return response.json()
    except requests.exceptions.RequestException as e:
        logger.error(f"Error fetching data: {e}")
        return None
