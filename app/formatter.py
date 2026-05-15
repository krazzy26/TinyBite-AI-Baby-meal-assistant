from app.schemas import MealPlan


def format_meal_plan_for_whatsapp(plan:MealPlan) -> str:
    lines=[f"TinyBite AI meal plan = {plan.date}", ""]

    for meal in plan.meals:
        lines.append(f"*{meal.type.upper()}*: {meal.name}")
        lines.append(f"Ingredients: {', '.join(meal.ingredients)}")
        lines.append(f"Prep: {meal.prep}")
        lines.append(f"Portion: {meal.portion_guidance}")
        lines.append(f"Safety: {meal.safety_notes}")
        lines.append("")
    
    lines.append(f"Shopping list: {', '.join(plan.shopping_list)}")
    lines.append("")
    lines.append(f"Note: {plan.parent_note}")

    return "\n".join(lines)

