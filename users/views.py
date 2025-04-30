from django.http import HttpResponse
from django.shortcuts import render
from fuzzy_logic import Fuzzifiction

def diet_form(request):
    if request.method == "POST":
        age = request.POST.get("age")
        height = request.POST.get("height")
        weight = request.POST.get("weight")
        activity_level = request.POST.get("activity_level")
        diet_preference = request.POST.get("diet_prefrence")
        disease=request.POST.get("user_disease")
        print(weight, height)
        height=float(height)
        weight=float(weight)

        bmi = weight / (height ** 2)

        activity_map = {
            "Extremely Active": 0,
            "Lightly Active": 1,
            "Moderately": 2,
            "Sedentary": 3,
            "Very Active": 4
             }

        diet_map = {
            "Omnivore": 0,
            "Pescatarian": 1,
            "Vegan": 2,
            "Vegetarian": 2,
        }

              
        activity_level = activity_map.get(activity_level, 0)
        diet_preference= diet_map.get(diet_preference, 0)

        

        recommendation = Fuzzifiction().execute(age, bmi, activity_level, diet_preference,disease)

        return render(request, "users/result.html", {
                "bmi": round(bmi, 2),
                "recommendation": recommendation,
        })

        # return render(request,template_name="users/result.html", {
        #     "bmi": round(bmi, 2),
        #     "recommendation": recommendation,
        #     "breakfast": breakfast, 
        #     "lunch": lunch,
        #     "dinner": dinner,
        #     "snack": snack,
    # })

    return render(request, template_name="users/health.html", context={})

        
    
# return render(request,template_name="users/result.html", {
#         "bmi": round(bmi, 2),
#         "recommendation": recommendation,
#         "breakfast": breakfast,
#         "lunch": lunch,
#         "dinner": dinner,
#         "snack": snack, kk
#     })
