from django.http import HttpResponse
from django.shortcuts import render
from fuzzy_logic import Fuzzifiction

def diet_form(request):
    if request.method == "POST":
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        activity_level = request.POST.get("activity_level")
        diet_preference = request.POST.get("diet_preference")
        disease=request.POST.get("user_disease")
        height=float(height)
        weight=float(weight)

        height_m = height/100
        bmi = weight / (height_m ** 2)

        activity_map = {
            "active": 0, # 3, 4
            "moderate": 2,
            "sedentary": 1,
        }

        diet_map = {
            "non-veg": 0,
            "vegan": 2,
            "vegetarian": 3,
        }
              
        activity_level = activity_map.get(activity_level, 0)
        diet_preference= diet_map.get(diet_preference, 0)

        recommendation = Fuzzifiction().execute(age, bmi, activity_level, diet_preference,disease)

        return render(request, "users/result.html", {
                "bmi": round(bmi, 2),
                "recommendation": recommendation,
        })

    return render(request, template_name="users/health.html", context={})

