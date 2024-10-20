from typing import Optional
from fastapi import APIRouter, HTTPException, Query
from datetime import datetime
from ev_utils.ev_evaluator import evaluate_ev_data
from ev_utils.logger import logger

router = APIRouter()

@router.get("/evdata/{year}")
async def get_ev_data(
    year: int,
    verbose: Optional[bool] = None
):
    request_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    logger.info(f"Received request for EV data at {request_time} with year={year} and verbose={verbose}.")
    
    if year is None:
        raise HTTPException(status_code=400, detail="Year parameter is required.")
    
    try:
        data = evaluate_ev_data(verbose=verbose, year=str(year))
        logger.info(f"Successfully evaluated data and returning {len(data['data'])} records.")
        return data
    except HTTPException as e:
        logger.error(f"Error occurred during evaluation: {e.detail}")
        return {"error": e.detail}
