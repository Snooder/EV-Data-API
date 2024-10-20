from collections import defaultdict
from fastapi import HTTPException
from .ev_scraper import ev_data_cache
from .logger import logger

def get_filtered_data(ev_data_cache, year):
    filtered_data = [record for record in ev_data_cache if record.get("model_year") == year]
    
    if not filtered_data:
        available_years = sorted({record.get("model_year") for record in ev_data_cache})
        logger.warning(f"No data found for model year {year}. Available years: {available_years}")
        raise HTTPException(status_code=404, detail=f"No data found for model year {year}. Available years: {available_years}.")
    
    return filtered_data

def group_data_by_make(filtered_data):
    make_data = defaultdict(lambda: {"total_cars": 0, "total_range": 0})
    
    for record in filtered_data:
        make = record.get("make") 
        electric_range = int(record.get("electric_range", 0))
        make_data[make]["total_cars"] += 1
        make_data[make]["total_range"] += electric_range
    
    return make_data

def prepare_result(make_data, filtered_data, verbose):
    result = []
    
    for make, data in make_data.items():
        avg_range = data["total_range"] / data["total_cars"]
        entry = {
            "make": make,
            "total_cars": data["total_cars"],
            "average_electric_range": round(avg_range, 2)
        }
        
        if verbose:
            entry["raw_data"] = [record for record in filtered_data if record.get("make") == make]
        
        result.append(entry)
    
    return sorted(result, key=lambda x: x["total_cars"], reverse=True)

def evaluate_ev_data(verbose: bool = False, year: str = None):
    logger.info(f"Evaluating EV data for response (Year: {year}, Verbose: {verbose}).")
    
    if not ev_data_cache:
        logger.warning("No data available. The cache is empty.")
        raise HTTPException(status_code=404, detail="Data not available. Please try again later.")
    
    filtered_data = get_filtered_data(ev_data_cache, year)
    make_data = group_data_by_make(filtered_data)
    result = prepare_result(make_data, filtered_data, verbose)
    
    return {"year": year, "total_records": len(filtered_data), "data": result}
