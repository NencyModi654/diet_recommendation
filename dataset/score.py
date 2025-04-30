import pandas as pd

data = pd.read_csv('food_and_nutrition.csv')
def calculate_score(row):
    # Example conditions for the score
    def calculate_score(row):
        if row['age'] == 'young' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'vegetarian':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'obese' and row['activity'] == 'sedentary' and row['diet'] == 'non_veg':
            return 'low'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'overweight' and row['activity'] == 'moderate' and row['diet'] == 'vegan':
            return 'moderate'
        elif row['age'] == 'young' and row['bmi'] == 'underweight' and row['activity'] == 'sedentary' and row['diet'] == 'eggitarian':
            return 'low'
        elif row['age'] == 'elderly' and row['bmi'] == 'normal' and row['activity'] == 'moderate' and row['diet'] == 'vegetarian':
            return 'moderate'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'obese' and row['activity'] == 'active' and row['diet'] == 'non_veg':
            return 'high'
        elif row['age'] == 'young' and row['bmi'] == 'underweight' and row['activity'] == 'active' and row['diet'] == 'vegan':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'overweight' and row['activity'] == 'moderate' and row['diet'] == 'non_veg':
            return 'low'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'normal' and row['activity'] == 'sedentary' and row['diet'] == 'vegetarian':
            return 'low'
        elif row['age'] == 'young' and row['bmi'] == 'obese' and row['activity'] == 'sedentary' and row['diet'] == 'non_veg':
            return 'low'
        elif row['age'] == 'elderly' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'eggitarian':
            return 'high'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'underweight' and row['activity'] == 'moderate' and row['diet'] == 'non_veg':
            return 'moderate'
        elif row['age'] == 'young' and row['bmi'] == 'overweight' and row['activity'] == 'active' and row['diet'] == 'vegetarian':
            return 'moderate'
        elif row['age'] == 'elderly' and row['bmi'] == 'underweight' and row['activity'] == 'active' and row['diet'] == 'vegan':
            return 'moderate'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'overweight' and row['activity'] == 'sedentary' and row['diet'] == 'eggitarian':
            return 'low'
        elif row['age'] == 'young' and row['bmi'] == 'normal' and row['activity'] == 'moderate' and row['diet'] == 'non_veg':
            return 'moderate'
        elif row['age'] == 'elderly' and row['bmi'] == 'obese' and row['activity'] == 'moderate' and row['diet'] == 'vegetarian':
            return 'low'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'vegan':
            return 'high'
        elif row['age'] == 'young' and row['bmi'] == 'normal' and row['activity'] == 'sedentary' and row['diet'] == 'eggitarian':
            return 'low'
        elif row['age'] == 'elderly' and row['bmi'] == 'overweight' and row['activity'] == 'active' and row['diet'] == 'vegetarian':
            return 'moderate'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'non_veg':
            return 'high'
        elif row['age'] == 'young' and row['bmi'] == 'obese' and row['activity'] == 'active' and row['diet'] == 'vegan':
            return 'moderate'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'underweight' and row['activity'] == 'active' and row['diet'] == 'vegetarian':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'normal' and row['activity'] == 'sedentary' and row['diet'] == 'eggitarian':
            return 'low'
        elif row['age'] == 'young' and row['bmi'] == 'overweight' and row['activity'] == 'sedentary' and row['diet'] == 'non_veg':
            return 'low'
        elif row['age'] == 'elderly' and row['bmi'] == 'obese' and row['activity'] == 'active' and row['diet'] == 'vegetarian':
            return 'moderate'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'underweight' and row['activity'] == 'sedentary' and row['diet'] == 'non_veg':
            return 'low'
        elif row['age'] == 'young' and row['bmi'] == 'normal' and row['activity'] == 'moderate' and row['diet'] == 'vegetarian':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'overweight' and row['activity'] == 'moderate' and row['diet'] == 'vegan':
            return 'moderate'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'eggitarian':
            return 'high'
        elif row['age'] == 'young' and row['bmi'] == 'underweight' and row['activity'] == 'moderate' and row['diet'] == 'non_veg':
            return 'low'
        elif row['age'] == 'elderly' and row['bmi'] == 'overweight' and row['activity'] == 'sedentary' and row['diet'] == 'vegan':
            return 'low'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'obese' and row['activity'] == 'sedentary' and row['diet'] == 'vegetarian':
            return 'low'
        elif row['age'] == 'young' and row['bmi'] == 'underweight' and row['activity'] == 'active' and row['diet'] == 'non_veg':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'non_veg':
            return 'high'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'overweight' and row['activity'] == 'active' and row['diet'] == 'eggitarian':
            return 'high'
        elif row['age'] == 'young' and row['bmi'] == 'normal' and row['activity'] == 'moderate' and row['diet'] == 'vegan':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'underweight' and row['activity'] == 'active' and row['diet'] == 'vegetarian':
            return 'high'
        elif row['age'] == 'middle_aged' and row['bmi'] == 'obese' and row['activity'] == 'moderate' and row['diet'] == 'eggitarian':
            return 'moderate'
        elif row['age'] == 'young' and row['bmi'] == 'normal' and row['activity'] == 'active' and row['diet'] == 'eggitarian':
            return 'high'
        elif row['age'] == 'elderly' and row['bmi'] == 'overweight' and row['activity'] == 'moderate' and row['diet'] == 'non_veg':
            return 'low'
        else:
            return 'unknown'  # Default if no condition is met

# Step 3: Apply the function to each row and add the result to the 'score' column
data['score'] = data.apply(calculate_score, axis=1)

# Step 4: Save the updated data with the new 'score' column back to a CSV file
data.to_csv('food_and_nutrition.csv', index=False)  # The updated data will be saved in 'updated_data.csv'

print("CSV file updated with 'score' column.")