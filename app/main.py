from fastapi import FastAPI, HTTPException
from app.schemas import BabyProfile, Meal, MealPlan
from app.openai_service import generate_meal_plan_with_openai
import traceback

app = FastAPI(title="TinyBite AI",
              description="AI -powered baby meal planning assistant",
              version="0.1.0",)

@app.get("/health")
def health_check():
    return {
        "status":"ok",
        "service":"TinyBite AI"
    }

@app.post("/meal-plan", response_model=MealPlan)
def create_meal_plan(profile:BabyProfile):
    try:
        return generate_meal_plan_with_openai(profile)
    except Exception as e:
        print("Error while generating meal plan")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=f"Failed to generate meal plan: str(e)")

@app.post("/meal-plan1", response_model=MealPlan)
def create_meal_plan1(profile:BabyProfile):
    return MealPlan (
        date="2026-05-11", 
        meals=[
          Meal(
                type="breakfast",
                name="Vegetable suji upma",
                ingredients=["suji", "carrot", "peas", "ghee"],
                prep="Cook until very soft and mash lightly.",
                portion_guidance="Start with a small toddler bowl and follow appetite.",
                safety_notes=["Ensure vegetables are very soft and finely chopped."]
            ),
        ],
        shopping_list=["suji", "moong dal", "curd", "paneer", "carrot"],
        parent_note="Simple meal plan. Consult pediatrician for any allergy concerns"
         
    )
