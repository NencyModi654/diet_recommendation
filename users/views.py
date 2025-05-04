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
        diseases = request.POST.getlist("user_disease")  # Accept multiple diseases
        
        height = float(height)
        weight = float(weight)
        height_m = height / 100
        bmi = weight / (height_m ** 2)

        activity_map = {
            "active": 0,
            "sedentary": 1,
            "moderate": 2,
            
        }

        diet_map = {
            "non-veg": 0,
            "vegan": 1,
            "vegetarian": 2,
        }

        activity_level = activity_map.get(activity_level, 0)
        diet_preference = diet_map.get(diet_preference, 0)

        # You can handle diseases as list, or join them into a string if your Fuzzifiction model expects a single value
        # Example: just take the first one, or pass all as comma-separated string
        # disease_input = diseases[0] if diseases else "Nothing"
        # 
        if "Nothing" in diseases and len(diseases) == 1:
            disease_input = "Weight Gain"  # fallback case
        else:
            diseases = [d for d in diseases if d != "Nothing"]
            disease_input = ", ".join(diseases) if diseases else "Weight Gain"

        recommendation = Fuzzifiction().execute(age, bmi, activity_level, diet_preference, disease_input)

        return render(request, "users/result.html", {
            "bmi": round(bmi, 2),
            "recommendation": recommendation,
        })
    
        

    return render(request, template_name="users/health.html", context={})

# def contact_view(request):
#             return render(request, 'contact-page.html')


def services_page(request):
    return render(request, 'users/service-page.html')
    
    
def contact_page(request):
    return render(request, 'users/contact-page.html')