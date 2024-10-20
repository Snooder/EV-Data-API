import requests
from fastapi import HTTPException
from .logger import logger

ev_data_cache = []

def scrape_ev_data():
    url = "https://data.wa.gov/resource/f6w7-q2d2.json"
    logger.info("Starting to scrape EV data from the source.")
    
    try:
        response = requests.get(url)

        if response.status_code == 200:
            ev_data_cache.clear()
            ev_data_cache.extend(response.json())
            logger.info(f"Successfully scraped {len(ev_data_cache)} records of EV data.")
        else:
            logger.error(f"Failed to fetch data from the source. Status code: {response.status_code}")
            raise HTTPException(status_code=500, detail="Failed to fetch data from the source.")
    
    except Exception as e:
        logger.error(f"Error occurred while scraping EV data: {str(e)}")
        raise HTTPException(status_code=500, detail="Error occurred while scraping EV data.")
