from backend.models import appliance_info
from fastapi import APIRouter, HTTPException
from backend.calculator import energy_calculator
from backend.gemini import call_gemini

router = APIRouter()

@router.post("/compute_kwh")
async def compute_kwh(info: appliance_info):
    try:
        watts = await call_gemini(info)
        
        result = energy_calculator(info, watts)
        return {
            "appliance": info.name,
            "type": info.type,
            "hours": info.hours,
            "quantity": info.quantity,
            **result
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))