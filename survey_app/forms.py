from django import forms
from .models import SurveyResponse


class Page1Form(forms.ModelForm):
    
    other_category = forms.CharField(required=False, widget=forms.TextInput(attrs={'placeholder': 'Specify Category'}))

    class Meta:
        model = SurveyResponse
        fields = ['full_name', 'gender', 'mobile_number', 'email', 'date_of_birth', 
                  'height_feet', 'height_inches', 'weight', 'description', 'category', 'coach_name']
        widgets = {
            'date_of_birth': forms.DateInput(attrs={'type': 'date'}),
        }

from django import forms

class Page2Form(forms.ModelForm):
    class Meta:
        model = SurveyResponse
        fields = [
            'infections_diagnosed', 'autoimmune_condition', 'reproductive_urinary_conditions',
            'cardiovascular_conditions', 'nervous_bone_muscle_conditions', 'sleep_disorder_medications',
            'allergies_asthma', 'skin_conditions', 'acne_history', 'mental_health_conditions', 
            'blood_transfusion', 'high_risk_yellow_fever', 'hospitalization_surgery', 'contagious_diseases',
            'multi_drug_resistant_organisms', 'heart_blood_pressure_diabetes_medication', 'mold_exposure',
            'genetic_conditions', 'antibiotics_taken', 'most_recent_antibiotic_treatment', 'covid_tested_positive'
        ]
        widgets = {
            'reproductive_urinary_conditions': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'cardiovascular_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'nervous_bone_muscle_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'sleep_disorder_medications': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'allergies_asthma': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'skin_conditions': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'acne_history': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'mental_health_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'blood_transfusion': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'high_risk_yellow_fever': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'hospitalization_surgery': forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
            'contagious_diseases': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'mold_exposure': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'genetic_conditions': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
            'covid_tested_positive': forms.RadioSelect( choices=[(True, 'Yes'), (False, 'No')]),
        }

class Page3Form(forms.ModelForm):
    # hair_loss = forms.ChoiceField(
    #     choices=[('yes', 'Yes'), ('no', 'No')],
    #     widget=forms.RadioSelect,
    #     initial='no'
    #  <label class="form-label me-3 mb-4">Reproductive/Urinary Conditions :</label>
    #  <div class="d-flex align-items-center">
    #                 <div  class="form-check">
    #                     <input class="form-check-input" type="radio" name="reproductive_urinary_conditions" id="reproductive_yes" value="True">
    #                     <label class="form-check-label" for="reproductive_yes">Yes</label>
    #                 </div>
    #                 <div class="form-check mx-3">
    #                     <input class="form-check-input " type="radio" name="reproductive_urinary_conditions" id="reproductive_no" value="False">
    #                     <label class="form-check-label" for="reproductive_no">No</label>
    #                 </div>
    #             </div>
    # )
    class Meta:
        model = SurveyResponse
        fields = [
            'hair_loss', 'vision_problems', 'blood_donation', 'body_fat_percentage', 'birth_type', 'birth_state',
            'pin_code', 'current_city', 'exercise_hours_per_day', 'exercise_days_per_week', 'physical_activities',
            'proficiency_level', 'upbringing', 'blood_group', 'smoking', 'alcohol_consumption', 'breastfeeding',
            'bowel_movements', 'bloating_acidity', 'digestive_issues', 'food_intolerances', 'meals_per_day',
            'snacks_per_day', 'home_cooked_meals', 'dairy_consumption', 'diet_type', 'meat_type', 'meat_frequency',
            'local_cuisine', 'medications_taken', 'covid_vaccination', 'covid_vaccine'
        ]
        widgets = {
        'hair_loss' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        'vision_problems' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        'blood_donation' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        'food_intolerances' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        'dairy_consumption' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        'medications_taken' : forms.RadioSelect(choices=[(True, 'Yes'), (False, 'No')]),
        }