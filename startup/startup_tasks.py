from ev_utils.ev_scraper import scrape_ev_data
from ev_utils.logger import logger

async def on_startup():
    port = 8000
    logger.info(f"Starting up FastAPI application on port {port}.")
    
    try:
        scrape_ev_data()
        logger.info("Initial scraping of EV data complete.")
    except Exception as e:
        logger.error(f"Error during startup scraping: {str(e)}")
        raise
