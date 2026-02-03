from pydantic import BaseModel
from typing import List
from typing import Optional

class appliance_info(BaseModel):
    hours: int
    quantity: int
    name: str
    type: str

class applianceBreakdown(BaseModel):
    name: str
    type: str
    daily_kwh: float
    monthly_kwh: float
    watts_used: float

class highestConsumer(BaseModel):
    name: str
    type: str
    monthly_kwh: float

class EstimationResponse(BaseModel):
    total_daily_kwh: float
    total_monthly_kwh: float
    total_monthly_cost: Optional[float] = 0
    appliance_breakdown: List[applianceBreakdown]
    highest_consumer: highestConsumer

class Estimation(BaseModel):
    appliances: List[appliance_info]
    