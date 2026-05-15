from fastapi import FastAPI, HTTPException
from app.schemas import BabyProfile, Meal, MealPlan
from app.openai_service import generate_meal_plan_with_openai
from app.formatter import format_meal_plan_for_whatsapp
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
    

@app.post("/meal-plan/message")
def create_meal_plan_message(profile:BabyProfile):
    try:
        plan = generate_meal_plan_with_openai(profile)
        message = format_meal_plan_for_whatsapp(plan)

        return {
            "message":message,
            "plan":plan
        }
    except Exception as e:
        print("Error while generating meal plan message")
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))