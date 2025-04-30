import numpy as np
import pandas as pd
import skfuzzy as fuzz
import skfuzzy.control as ctrl

class Fuzzifiction():
    def execute(self, age, bmi, activity_level, diet_preference,disease):    
        fuzzified = self.fuzzify_user_input(age, bmi, activity_level, diet_preference)
        score = self.infer_diet_recommendation(fuzzified)
        result = self.fetch_recommendation(score,diet_preference,disease)
        return result

    # Step 1: Fuzzify user input
    def fuzzify_user_input(self, age_val, bmi_val, activity_val, pref_val):
        age = np.arange(15, 81, 1)
        age_young = fuzz.trimf(age, [15, 20, 35])
        age_middle = fuzz.trimf(age, [30, 45, 60])
        age_elderly = fuzz.trimf(age, [55, 70, 80])

        age_membership = {
            "Young": round(fuzz.interp_membership(age, age_young, age_val), 3),
            "Middle-aged": round(fuzz.interp_membership(age, age_middle, age_val), 3),
            "Elderly": round(fuzz.interp_membership(age, age_elderly, age_val), 3)
        }

        bmi = np.arange(10, 41, 0.5)
        bmi_under = fuzz.trimf(bmi, [10, 15, 18.5])
        bmi_normal = fuzz.trimf(bmi, [18.5, 22, 25])
        bmi_over = fuzz.trimf(bmi, [24, 27, 30])
        bmi_obese = fuzz.trimf(bmi, [29, 35, 40])

        bmi_membership = {
            "Underweight": round(fuzz.interp_membership(bmi, bmi_under, bmi_val), 3),
            "Normal": round(fuzz.interp_membership(bmi, bmi_normal, bmi_val), 3),
            "Overweight": round(fuzz.interp_membership(bmi, bmi_over, bmi_val), 3),
            "Obese": round(fuzz.interp_membership(bmi, bmi_obese, bmi_val), 3)
        }

        activity = np.arange(0, 5, 1)
        activity_sedentary = fuzz.trimf(activity, [0, 0, 2])
        activity_moderate = fuzz.trimf(activity, [1, 2, 3])
        activity_active = fuzz.trimf(activity, [2, 4, 4])
        
        activity_membership = {
            "Sedentary": round(fuzz.interp_membership(activity, activity_sedentary, activity_val), 3),
            "Moderate": round(fuzz.interp_membership(activity, activity_moderate, activity_val), 3),
            "Active": round(fuzz.interp_membership(activity, activity_active, activity_val), 3)
        }

        pref = np.arange(1, 5, 1)
        pref_vegan = fuzz.trimf(pref, [1, 1, 2])
        pref_veg = fuzz.trimf(pref, [1, 2, 3])
        pref_egg = fuzz.trimf(pref, [2, 3, 4])
        pref_nonveg = fuzz.trimf(pref, [3, 4, 4])

        pref_membership = {
            "Vegan": round(fuzz.interp_membership(pref, pref_vegan, pref_val), 3),
            "Vegetarian": round(fuzz.interp_membership(pref, pref_veg, pref_val), 3),
            "Eggitarian": round(fuzz.interp_membership(pref, pref_egg, pref_val), 3),
            "Non-Veg": round(fuzz.interp_membership(pref, pref_nonveg, pref_val), 3)
        }

        return {
            "Age": age_membership,
            "BMI": bmi_membership,
            "Activity Level": activity_membership,
            "Dietary Preference": pref_membership
        }

    # Step 2: Define rules and inference
    def infer_diet_recommendation(self, fuzzified_input):
        age = fuzzified_input["Age"]
        bmi = fuzzified_input["BMI"]
        activity = fuzzified_input["Activity Level"]
        # pref = fuzzified_input["Dietary Preference"]

        # recommendation = np.arange(0, 11, 1)
        # rec_low = fuzz.trimf(recommendation, [0, 0, 5])
        # rec_moderate = fuzz.trimf(recommendation, [3, 5, 7])
        # rec_high = fuzz.trimf(recommendation, [5, 10, 10])

        # --- Vegan ---
        if age == 'young' and bmi == 'obese' and activity == 'moderate':
         return 'moderate'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'moderate':
            return 'high'
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'active':
             return 'high'
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'active':
             return 'high'
        elif age == 'middle_aged' and bmi == 'obese' and activity == 'sedentary':
            return 'low'
        if age == 'elderly' and bmi == 'obese' and activity == 'active':
            return 'low'
        elif age == 'young' and bmi == 'overweight' and activity == 'moderate':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'obese' and activity == 'sedentary':
            return 'low'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'sedentary':
            return 'low'
        elif age == 'middle_aged' and bmi == 'underweight' and activity == 'active':
            return 'high'
        elif age == 'middle_aged' and bmi == 'obese' and activity == 'sedentary':
            return 'low'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'moderate':
            return 'high'
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'active':
            return 'high'
        elif age == 'elderly' and bmi == 'underweight' and activity == 'moderate':
            return 'low'
        elif age == 'elderly' and bmi == 'underweight' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'overweight' and activity == 'moderate':
            return 'moderate'
        elif age == 'young' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'active':
            return 'high'
        elif age == 'elderly' and bmi == 'obese' and activity == 'sedentary':
            return 'low'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'moderate':
            return 'high'        
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'moderate':
            return 'moderate'
        elif age == 'young' and bmi == 'underweight' and activity == 'sedentary':
            return 'low'
        elif age == 'elderly' and bmi == 'normal' and activity == 'moderate':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'obese' and activity == 'active':
            return 'high'
        elif age == 'young' and bmi == 'underweight' and activity == 'active':
            return 'high'
        elif age == 'elderly' and bmi == 'underweight' and activity == 'moderate':
            return 'low'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'moderate':
            return 'low'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'overweight' and activity == 'moderate':
            return 'moderate'
        elif age == 'young' and bmi == 'obese' and activity == 'sedentary':
            return 'low'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'sedentary':
            return 'low'
        elif age == 'elderly' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'middle_aged' and bmi == 'underweight' and activity == 'moderate':
            return 'moderate'
        elif age == 'elderly' and bmi == 'underweight' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'overweight' and activity == 'active':
            return 'moderate'
        elif age == 'elderly' and bmi == 'underweight' and activity == 'active':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'normal' and activity == 'moderate':
            return 'moderate'
        elif age == 'elderly' and bmi == 'obese' and activity == 'moderate':
            return 'low'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'young' and bmi == 'normal' and activity == 'sedentary':
            return 'low'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'active':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'young' and bmi == 'obese' and activity == 'active':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'underweight' and activity == 'active':
            return 'high'
        elif age == 'elderly' and bmi == 'normal' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'overweight' and activity == 'sedentary':
            return 'low'
        elif age == 'elderly' and bmi == 'obese' and activity == 'active':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'underweight' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'normal' and activity == 'moderate':
            return 'high'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'moderate':
            return 'moderate'
        elif age == 'middle_aged' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'young' and bmi == 'underweight' and activity == 'moderate':
            return 'low'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'sedentary':
            return 'low'
        elif age == 'middle_aged' and bmi == 'obese' and activity == 'sedentary':
            return 'low'
        elif age == 'young' and bmi == 'underweight' and activity == 'active':
            return 'high'
        elif age == 'elderly' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'middle_aged' and bmi == 'overweight' and activity == 'active':
            return 'high'
        elif age == 'young' and bmi == 'normal' and activity == 'moderate':
            return 'high'
        elif age == 'elderly' and bmi == 'underweight' and activity == 'active':
            return 'high'
        elif age == 'middle_aged' and bmi == 'obese' and activity == 'moderate':
            return 'moderate'
        elif age == 'young' and bmi == 'normal' and activity == 'active':
            return 'high'
        elif age == 'elderly' and bmi == 'overweight' and activity == 'moderate':
            return 'low'
        else:
            return 'unknown'  # Default if no condition is met
    
    def fetch_recommendation(self, score: str, diet_preference: int, disease: str) -> str:

# Use a raw string or double backslashes to avoid escape characters
        file_path = r'D:\projects\diet_recommendation\dataset\food_and_nutrition_update.csv'
        data = pd.read_csv(file_path)
        

        fetch=data[
            (data['Scaling'].str.lower() == score.lower()) &
            (data['Disease']== disease.lower()) 
            (data['Dietary Preference']== diet_preference),
         ]

        breakfast = ", ".join(fetch['Breakfast Suggestion'].dropna().head(4).tolist())
        lunch = ", ".join(fetch['Lunch Suggestion'].dropna().head(4).tolist())
        dinner = ", ".join(fetch['Dinner Suggestion'].dropna().head(4).tolist())
        snack = ", ".join(fetch['Snack Suggestion'].dropna().head(4).tolist())

        return render_template("result.html",
                            breakfast=breakfast,
                            lunch=lunch,
                            dinner=dinner,
                            snack=snack)







    # print(f"\nDiet Recommendation Score (0-Low to 10-High): {score}")

