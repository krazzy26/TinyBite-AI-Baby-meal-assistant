from pydantic import BaseModel, Field, ConfigDict
from typing import List

class BabyProfile(BaseModel):
    model_config = ConfigDict(extra="forbid")
    age_months:int = Field(..., ge=6, le=36)
    diet:str = "vegetarian"
    preferred_cuisine:str="Indian"
    allergies:List[str]=[]
    avoid_foods: List[str]=[]
    meal_count:int = Field(default=4, ge=1, le=6)
    texture: str = "soft, mashed, small pieces"

class Meal(BaseModel):
    model_config = ConfigDict(extra="forbid")
    type: str
    name: str
    ingredients: List[str]
    prep: str
    portion_guidance: str
    safety_notes: List[str]

class MealPlan(BaseModel):
    model_config = ConfigDict(extra="forbid")
    date:str
    meals:List[Meal]
    shopping_list: List[str]
    parent_note: str

