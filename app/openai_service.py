import json
from datetime import date

from dotenv import load_dotenv
from openai import OpenAI

from app.schemas import BabyProfile, MealPlan

load_dotenv()

client = OpenAI()


def generate_meal_plan_with_openai(profile:BabyProfile) -> MealPlan:

    system_prompt="""
You are TinyBite AI, a baby meal advisor.

Your job:
- Generate safe, practical baby/toddler meal ideas.
- Do not provide any medical diagnosis or medical treatment advice
- Avoid any choking hazards for baby
- Avoid excess salt and added sugar
- Use age-appropriate soft textures
- Prefer simple Indian vegeterian meals unless the user asks otherwise
- Return only valid JSON matching the required schema
"""

    user_prompt = """
    Create a one-day meal plan for this baby profile.
    Baby profile:
    {profile.model_dump_json()}

    Today's date:
    {date.today().isoformat()}

    Requirements:
    - Exactly 4 meals - Breakfast, lunch, snacks, dinner
    - Match the baby's age and texture preference
    - Respect allergens and foods to be avoided
    - Include protein in atleast two meal
    - Include fruit and vegetables in atleast two meals
    - Include safety notes for every meal
    - Keep meals realistic and should not be extremely time-consuming to prepare
    - Do not repeat main ingredients from one of the meals in other meals.
    """

    response = client.responses.create(
        model="gpt-4o-mini",
        input=[{"role":"system", "content":system_prompt},
            {"role":"user", "content":user_prompt},],
        text={
            "format": {
                "type":"json_schema",
                "name": "baby_meal_plan",
                "schema": MealPlan.model_json_schema(),
                "strict":True
            }
        },
    )

    data = json.loads(response.output_text)
    return MealPlan(**data)