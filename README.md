# TinyBite AI

An AI-powered baby meal planning API that generates safe, age-appropriate meal plans for babies and toddlers (6–36 months).

## Features

- Generates a one-day, 4-meal plan (breakfast, lunch, snack, dinner) tailored to the baby's profile
- Respects allergies, foods to avoid, texture preferences, and cuisine preferences
- Returns a structured shopping list and a parent note with each plan
- Includes safety notes per meal (choking hazards, texture guidance)
- Exposes a WhatsApp-formatted message endpoint (WhatsApp delivery integration coming soon)

## Tech Stack

- **FastAPI** — REST API framework
- **OpenAI GPT-4o-mini** — structured meal plan generation via JSON schema output
- **Pydantic** — request/response validation and schema definition
- **uv** — dependency and virtual environment management

## Project Structure

```
app/
  main.py           # FastAPI app and route definitions
  schemas.py        # Pydantic models: BabyProfile, Meal, MealPlan
  openai_service.py # OpenAI call with structured output
  formatter.py      # WhatsApp message formatter
pyproject.toml
```

## Getting Started

### Prerequisites

- Python 3.13+
- [uv](https://docs.astral.sh/uv/) installed
- An OpenAI API key

### Installation

```bash
uv sync
```

### Environment Variables

Create a `.env` file in the project root:

```
OPENAI_API_KEY=your_openai_api_key_here
```

### Run the Server

```bash
uv run uvicorn app.main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Reference

### `GET /health`

Returns the service status.

**Response**
```json
{ "status": "ok", "service": "TinyBite AI" }
```

---

### `POST /meal-plan`

Generates a structured one-day meal plan.

**Request Body**

| Field               | Type         | Required | Default                         | Notes                    |
|---------------------|--------------|----------|---------------------------------|--------------------------|
| `age_months`        | int          | Yes      | —                               | Must be between 6 and 36 |
| `diet`              | string       | No       | `"vegetarian"`                  |                          |
| `preferred_cuisine` | string       | No       | `"Indian"`                      |                          |
| `allergies`         | list[string] | No       | `[]`                            |                          |
| `avoid_foods`       | list[string] | No       | `[]`                            |                          |
| `meal_count`        | int          | No       | `4`                             | Between 1 and 6          |
| `texture`           | string       | No       | `"soft, mashed, small pieces"`  |                          |

**Example Request**
```json
{
  "age_months": 10,
  "allergies": ["nuts"],
  "avoid_foods": ["honey"],
  "texture": "mashed"
}
```

**Example Response**
```json
{
  "date": "2026-05-15",
  "meals": [
    {
      "type": "Breakfast",
      "name": "Ragi Porridge with Banana",
      "ingredients": ["ragi flour", "banana", "water"],
      "prep": "Cook ragi flour in water until thick. Mash banana and stir in.",
      "portion_guidance": "4–5 tablespoons",
      "safety_notes": ["Ensure porridge is smooth with no lumps", "Let cool before serving"]
    }
  ],
  "shopping_list": ["ragi flour", "banana"],
  "parent_note": "All meals are soft and suitable for 10-month-olds."
}
```

---

### `POST /meal-plan/message`

Same as `/meal-plan` but also returns the plan formatted as a WhatsApp-ready text message.

**Response**
```json
{
  "message": "*BREAKFAST*: Ragi Porridge with Banana\n...",
  "plan": { ... }
}
```

## Roadmap

- [x] Structured meal plan generation via OpenAI
- [x] WhatsApp message formatter
- [ ] WhatsApp delivery integration (send plans directly to a WhatsApp number)
