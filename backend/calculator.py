from backend.models import appliance_info

def energy_calculator(info: appliance_info, watts: float) -> dict:
    if info.hours <= 0 or info.quantity <= 0:
        raise ValueError("Hours and quantity must be positive numbers")
    
    daily_kwh = (watts * info.hours * info.quantity) / 1000  # kWh
    monthly_kwh = daily_kwh * 30  # Approx 30 days, can make dynamic later
    
    return {
    "daily_kwh": daily_kwh,
    "monthly_kwh": monthly_kwh,
    "watts_used": watts
    }