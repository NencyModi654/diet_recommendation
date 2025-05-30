from django.conf import settings
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

    def fuzzify_user_input(self, age_val, bmi_val, activity_val, pref_val):
        age = np.arange(15, 81, 1)
        age_young = fuzz.trimf(age, [15, 20, 35])
        age_middle = fuzz.trimf(age, [30, 45, 60])
        age_elderly = fuzz.trimf(age, [55, 70, 80])

        age_membership = {
            "young": round(fuzz.interp_membership(age, age_young, age_val), 3),
            "middle_aged": round(fuzz.interp_membership(age, age_middle, age_val), 3),
            "elderly": round(fuzz.interp_membership(age, age_elderly, age_val), 3)
        }

        bmi = np.arange(10, 41, 0.5)
        bmi_under = fuzz.trimf(bmi, [10, 15, 18.5])
        bmi_normal = fuzz.trimf(bmi, [18.5, 22, 25])
        bmi_over = fuzz.trimf(bmi, [24, 27, 30])
        bmi_obese = fuzz.trimf(bmi, [29, 35, 40])

        bmi_membership = {
            "underweight": round(fuzz.interp_membership(bmi, bmi_under, bmi_val), 3),
            "normal": round(fuzz.interp_membership(bmi, bmi_normal, bmi_val), 3),
            "overweight": round(fuzz.interp_membership(bmi, bmi_over, bmi_val), 3),
            "obese": round(fuzz.interp_membership(bmi, bmi_obese, bmi_val), 3)
        }

        activity = np.arange(0, 5, 1)
        activity_sedentary = fuzz.trimf(activity, [0, 0, 2])
        activity_moderate = fuzz.trimf(activity, [1, 2, 3])
        activity_active = fuzz.trimf(activity, [2, 4, 4])
        
        activity_membership = {
            "sedentary": round(fuzz.interp_membership(activity, activity_sedentary, activity_val), 3),
            "moderate": round(fuzz.interp_membership(activity, activity_moderate, activity_val), 3),
            "active": round(fuzz.interp_membership(activity, activity_active, activity_val), 3)
        }

        pref = np.arange(0, 5, 1)

        pref_nonveg = fuzz.trimf(pref, [0, 0, 1.5])  
        pref_vegan = fuzz.trimf(pref, [1, 2, 3])             
        pref_vegetarian = fuzz.trimf(pref, [2, 3, 4])        

        pref_membership = {
            "Non-Veg": round(fuzz.interp_membership(pref, pref_nonveg, pref_val), 3),
            "Vegan": round(fuzz.interp_membership(pref, pref_vegan, pref_val), 3),
            "Vegetarian": round(fuzz.interp_membership(pref, pref_vegetarian, pref_val), 3)
        }
        output = {
            "Age": age_membership,
            "BMI": bmi_membership,
            "Activity Level": activity_membership,
            "Dietary Preference": pref_membership
        }
        return output

    def infer_diet_recommendation(self, fuzzified_input):
        age= max(fuzzified_input["Age"], key=fuzzified_input["Age"].get)
        bmi = max(fuzzified_input["BMI"], key=fuzzified_input["BMI"].get)
        activity = max(fuzzified_input["Activity Level"], key=fuzzified_input["Activity Level"].get)
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
    
    # def fetch_recommendation(self, score: str, diet_preference: int, disease: str) -> str:
    #     data = pd.read_csv(settings.DATASET_PATH)
    #     # print("???? User diseases: ", disease)

    #     fetch = data[
    #         data['Disease'].str.contains(disease.lower(), case=False, na=False) & 
    #         (data['Dietary Preference'] == diet_preference) &
    #         (data['Scaling'] == score)
    #     ]

    #     # fetch = data[
    #     # (data['Disease'].str.lower() == disease.lower()) &
    #     # (data['Dietary Preference'] == diet_preference) &
    #     # (data['Scaling'] == score)
    #     # ]

    #     breakfast = ', '.join(fetch['Breakfast Suggestion'].dropna().head(4).tolist())
    #     lunch = ', '.join(fetch['Lunch Suggestion'].dropna().head(4).tolist())
    #     dinner = ', '.join(fetch['Dinner Suggestion'].dropna().head(4).tolist())
    #     snack = ', '.join(fetch['Snack Suggestion'].dropna().head(4).tolist())
        
    #     return {
    #         "breakfast": breakfast,
    #         "lunch": lunch,
    #         "dinner": dinner,
    #         "snack": snack
    #     }

    # def fetch_recommendation(self, score: str, diet_preference: int, diseases: list) -> str:
    #     data = pd.read_csv(settings.DATASET_PATH)

    #     # Convert the diseases list to lowercase for comparison
    #     diseases_lower = [disease.lower() for disease in diseases]

    #     # Modify the filtering logic to check if the disease is a string before calling .lower()
    #     fetch = data[
    #         data['Disease'].apply(lambda x: any(disease.lower() in str(x).lower() for disease in diseases_lower)) & 
    #         (data['Dietary Preference'] == diet_preference) & 
    #         (data['Scaling'] == score)
    #     ]
        
    #     breakfast = ', '.join(fetch['Breakfast Suggestion'].dropna().head(4).tolist())
    #     lunch = ', '.join(fetch['Lunch Suggestion'].dropna().head(4).tolist())
    #     dinner = ', '.join(fetch['Dinner Suggestion'].dropna().head(4).tolist())
    #     snack = ', '.join(fetch['Snack Suggestion'].dropna().head(4).tolist())
        
    #     return {
    #         "breakfast": breakfast,
    #         "lunch": lunch,
    #         "dinner": dinner,
    #         "snack": snack
    #     }
    def fetch_recommendation(self, score: str, diet_preference: int, diseases: list) -> dict:
            data = pd.read_csv(settings.DATASET_PATH)
            diseases_lower = [d.lower() for d in diseases]

            fetch = data[
                data['Disease'].apply(lambda x: any(disease in str(x).lower() for disease in diseases_lower)) &
                (data['Dietary Preference'] == diet_preference) &
                (data['Scaling'] == score)
            ]

            def unique_join(series):
                seen = set()
                return ', '.join([x for x in series if not (x in seen or seen.add(x))])

            breakfast = unique_join(fetch['Breakfast Suggestion'].dropna().head(4).tolist())
            lunch = unique_join(fetch['Lunch Suggestion'].dropna().head(4).tolist())
            dinner = unique_join(fetch['Dinner Suggestion'].dropna().head(4).tolist())
            snack = unique_join(fetch['Snack Suggestion'].dropna().head(4).tolist())

            return {
                "breakfast": breakfast,
                "lunch": lunch,
                "dinner": dinner,
                "snack": snack
            }