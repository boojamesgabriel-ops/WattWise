from backend.models import appliance_info
from backend.calculator import energy_calculator
from backend.gemini import call_gemini
from typing import List

async def estimate_consumption(appliances: List[appliance_info]) -> dict:

    total_estimates = {
        "appliance_breakdown": [],
        "highest_consumer": [],
        "total_daily_kwh": 0,
        "total_monthly_kwh": 0
    }

    for appliance in appliances:

        watts = getattr(appliance, "watts", None)

        if watts is not None: 
            result = energy_calculator(appliance, watts)
        else:
            watts = await call_gemini(appliance)
            result = energy_calculator(appliance, watts)
        
        total_estimates["appliance_breakdown"].append({
            "name": appliance.name,
            "type": appliance.type,
            "hours": appliance.hours,
            "quantity": appliance.quantity,
            "daily_kwh": result["daily_kwh"],
            "monthly_kwh": result["monthly_kwh"]
        })

        total_estimates["total_daily_kwh"] += result["daily_kwh"]
        total_estimates["total_monthly_kwh"] += result["monthly_kwh"]
    
    highest_consumer = None

    for appliance_result in total_estimates["appliance_breakdown"]:
        if highest_consumer is None or appliance_result["monthly_kwh"] > highest_consumer["monthly_kwh"]:
            highest_consumer = appliance_result
    
    total_estimates["highest_consumer"] = highest_consumer


    return total_estimates
        
             