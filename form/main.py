from flask import Flask, render_template, request,jsonify
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from tkinter import *
import numpy as np
import pandas as pd
import os
import joblib
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes
current_directory = os.path.dirname(os.path.realpath(__file__))

model_path = os.path.join(current_directory, 'disease_classifier.pkl')
model1_path = os.path.join(current_directory, 'disease_classifier_random.pkl')
model2_path = os.path.join(current_directory, 'disease_classifier_bayes.pkl')

model = joblib.load(model_path)
model1 = joblib.load(model1_path)
model2 = joblib.load(model2_path)
# model = joblib.load('disease_classifier.pkl')
# model1 = joblib.load('disease_classifier_random.pkl')
# model2 = joblib.load('disease_classifier_bayes.pkl')

@app.route('/')
def home():
    return render_template('pateint_home.html')

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/schemes')
def schemes():
    return render_template('scheme.html')

@app.route('/symptomes', methods=['POST'])
def symptomes():
    select1 = request.form['select1']
    select2 = request.form['select2']
    select3 = request.form['select3']
    select4 = request.form['select4']
    print(select1,select2,select3,select4)
    l1=['back_pain','constipation','abdominal_pain','diarrhoea','mild_fever','yellow_urine',
    'yellowing_of_eyes','acute_liver_failure','fluid_overload','swelling_of_stomach',
    'swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
    'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs',
    'fast_heart_rate','pain_during_bowel_movements','pain_in_anal_region','bloody_stool',
    'irritation_in_anus','neck_pain','dizziness','cramps','bruising','obesity','swollen_legs',
    'swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
    'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips',
    'slurred_speech','knee_pain','hip_joint_pain','muscle_weakness','stiff_neck','swelling_joints',
    'movement_stiffness','spinning_movements','loss_of_balance','unsteadiness',
    'weakness_of_one_body_side','loss_of_smell','bladder_discomfort','foul_smell_of urine',
    'continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
    'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain',
    'abnormal_menstruation','dischromic _patches','watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum',
    'rusty_sputum','lack_of_concentration','visual_disturbances','receiving_blood_transfusion',
    'receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen',
    'history_of_alcohol_consumption','fluid_overload','blood_in_sputum','prominent_veins_on_calf',
    'palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
    'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose',
    'yellow_crust_ooze']

    disease=['Fungal_infection', 'Allergy', 'GERD', 'Chronic_cholestasis',
       'Drug_Reaction', 'Peptic_ulcer_diseae', 'AIDS', 'Diabetes ',
       'Gastroenteritis', 'Bronchial_Asthma', 'Hypertension ', 'Migraine',
       'Cervical_spondylosis', 'Paralysis_brain_hemorrhage', 'Jaundice',
       'Malaria', 'Chicken_pox', 'Dengue', 'Typhoid', 'hepatitis_A',
       'Hepatitis_B', 'Hepatitis_C', 'Hepatitis_D', 'Hepatitis_E',
       'Alcoholic_hepatitis', 'Tuberculosis', 'Common_Cold', 'Pneumonia',
       'Dimorphic_hemmorhoids', 'Heart_attack', 'Varicose_veins',
       'Hypothyroidism', 'Hyperthyroidism', 'Hypoglycemia',
       'Osteoarthristis', 'Arthritis',
       'Varicose_veins', 'Acne',
       'Urinary_tract_infection', 'Psoriasis', 'Impetigo','Paroymsal_Positional_Vertigo']
    
    l2=[]
    for i in range(0,len(l1)):
        l2.append(0)
    print(l2)
    
    psymptoms=[select1,select2,select3,select4]
    for k in range(0,len(l1)):
     for z in psymptoms:
        if(z==l1[k]):
            l2[k]=1

    inputtest = [l2]
    print(inputtest)
    predicted_disease=[]
    predict1=model.predict(inputtest)
    predicted1=predict1[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted1 == a):
            h='yes'
            break

    predicted_disease.append(disease[a])
    if (h=='yes'):
        print("Predicted disease:", disease[a])
    else:
        print("not found")

    predict2=model1.predict(inputtest)
    predicted2=predict2[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted2 == a):
            h='yes'
            break
    predicted_disease.append(disease[a])
    if (h=='yes'):
        print("Predicted disease:", disease[a])
    else:
        print("not found")  


    predict3=model2.predict(inputtest)
    predicted3=predict3[0]
    h='no'
    for a in range(0,len(disease)):
        if(predicted3 == a):
            h='yes'
            break
    predicted_disease.append(disease[a])
    if (h=='yes'):
        print("Predicted disease:", disease[a])
    else:
        print("not found")
    predicted_disease=list(set(predicted_disease)) 
    print(predicted_disease) 
    predicted_disease[0]

    
    disease_info = {
    "Drug_Reaction": [["stop irritation", "consult nearest hospital", "stop taking drug", "follow up"],
                      "Common -More than 1 million cases per year (India)"],
    "Malaria": [["Consult nearest hospital", "avoid oily food", "avoid non veg food", "keep mosquitos out"],
                "Rare -Fewer than 1 million cases per year (India)"],
    "Allergy": [["apply calamine", "cover area with bandage", "use ice to compress itching"],
                "Very common-More than 10 million cases per year (India)"],
    "Hypothyroidism": [["reduce stress", "exercise", "eat healthy", "get proper sleep"],
                        "Very common-More than 10 million cases per year (India)"],
    "Psoriasis": [["wash hands with warm soapy water", "stop bleeding using pressure", "consult doctor", "salt baths"],
                  "Very common-More than 10 million cases per year (India)"],
    "GERD": [["avoid fatty spicy food", "avoid lying down after eating", "maintain healthy weight", "exercise"],
             "Very common-More than 10 million cases per year (India)"],
    "Chronic_cholestasis": [["cold baths", "anti itch medicine", "consult doctor", "eat healthy"],
                             "Common -More than 1 million cases per year (India)"],
    "hepatitis_A": [["Consult nearest hospital", "wash hands through", "avoid fatty spicy food", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Osteoarthristis": [["acetaminophen", "consult nearest hospital", "follow up", "salt baths"],
                         "Very common-More than 10 million cases per year (India)"],
    "Paroymsal_Positional_Vertigo": [["lie down", "avoid sudden change in body", "avoid abrupt head movment", "relax"],
                                      "Common -More than 1 million cases per year (India)"],
    "Hypoglycemia": [["lie down on side", "check in pulse", "drink sugary drinks", "consult doctor"],
                      "Common -More than 1 million cases per year (India)"],
    "Acne": [["bath twice", "avoid fatty spicy food", "drink plenty of water", "avoid too many products"],
             "Very common-More than 10 million cases per year (India)"],
    "Diabetes": [["have balanced diet", "exercise", "consult doctor", "follow up"],
                 "Very common-More than 10 million cases per year (India)"],
    "Impetigo": [["soak affected area in warm water", "use antibiotics", "remove scabs with wet compressed cloth", "consult doctor"],
                 "Very common-More than 10 million cases per year (India)"],
    "Hypertension": [["meditation", "salt baths", "reduce stress", "get proper sleep"],
                      "Very common-More than 10 million cases per year (India)"],
    "Peptic_ulcer_diseae": [["avoid fatty spicy food", "consume probiotic food", "eliminate milk", "limit alcohol"],
                             "Common -More than 1 million cases per year (India)"],
    "Dimorphic_hemmorhoids": [["avoid fatty spicy food", "consume witch hazel", "warm bath with epsom salt", "consume alovera juice"],
                                "Very common-More than 10 million cases per year (India)"],
    "Common_Cold": [["drink vitamin c rich drinks", "take vapour", "avoid cold food", "keep fever in check"],
                     "Very common-More than 10 million cases per year (India)"],
    "Chicken_pox": [["use neem in bathing", "consume neem leaves", "take vaccine", "avoid public places"],
                    "Rare -Fewer than 1 million cases per year (India)"],
    "Cervical_spondylosis": [["use heating pad or cold pack", "exercise", "take otc pain reliver", "consult doctor"],
                              "Very common-More than 10 million cases per year (India)"],
    "Hyperthyroidism": [["eat healthy", "massage", "use lemon balm", "take radioactive iodine treatment"],
                         "Very common-More than 10 million cases per year (India)"],
    "Urinary_tract_infection": [["drink plenty of water", "increase vitamin c intake", "drink cranberry juice", "take probiotics"],
                                 "Very common-More than 10 million cases per year (India)"],
    "Varicose_veins": [["lie down flat and raise the leg high", "use oinments", "use vein compression", "dont stand still for long"],
                        "Very common-More than 10 million cases per year (India)"],
    "AIDS": [["avoid open cuts", "wear ppe if possible", "consult doctor", "follow up"],
             "Common -More than 1 million cases per year (India)"],
    "Paralysis_brain_hemorrhage": [["massage", "eat healthy", "exercise", "consult doctor"],
                                    "Common -More than 1 million cases per year (India)"],
    "Typhoid": [["eat high calorie vegitables", "antiboitic therapy", "consult doctor", "medication"],
                "Very rare- Fewer than 100 thousand cases per year (India)"],
    "Hepatitis_B": [["consult nearest hospital", "vaccination", "eat healthy", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Fungal_infection": [["bath twice", "use detol or neem in bathing water", "keep infected area dry", "use clean cloths"],
                          "Common -More than 1 million cases per year (India)"],
    "Hepatitis_C": [["Consult nearest hospital", "vaccination", "eat healthy", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Migraine": [["meditation", "reduce stress", "use poloroid glasses in sun", "consult doctor"],
                 "Very common-More than 10 million cases per year (India)"],
    "Bronchial_Asthma": [["switch to loose cloothing", "take deep breaths", "get away from trigger", "seek help"],
                          "Very common-More than 10 million cases per year (India)"],
    "Alcoholic_hepatitis": [["stop alcohol consumption", "consult doctor", "medication", "follow up"],
                             "Rare -Fewer than 1 million cases per year (India)"],
    "Jaundice": [["drink plenty of water", "consume milk thistle", "eat fruits and high fiberous food", "medication"],
                 "Common -More than 1 million cases per year (India)"],
    "Hepatitis_E": [["stop alcohol consumption", "rest", "consult doctor", "medication"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Dengue": [["drink papaya leaf juice", "avoid fatty spicy food", "keep mosquitos away", "keep hydrated"],
               "Very rare- Fewer than 100 thousand cases per year (India)"],
    "Hepatitis_D": [["consult doctor", "medication", "eat healthy", "follow up"],
                     "Rare -Fewer than 1 million cases per year (India)"],
    "Heart_attack": [["call ambulance", "chew or swallow asprin", "keep calm", ""],
                     "Very common-More than 10 million cases per year (India)"],
    "Pneumonia": [["consult doctor", "medication", "rest", "follow up"],
                   "Very common-More than 10 million cases per year (India)"],
    "Arthritis": [["exercise", "use hot and cold therapy", "try acupuncture", "massage"],
                   "Very common-More than 10 million cases per year (India)"],
    "Gastroenteritis": [["stop eating solid food for while", "try taking small sips of water", "rest", "ease back into eating"],
                         "Very common-More than 10 million cases per year (India)"],
    "Tuberculosis": [["cover mouth", "consult doctor", "medication", "rest"],
                      "Common -More than 1 million cases per year (India)"]
}


    for disease_name in predicted_disease:
        precautions = disease_info[disease_name][0]
        # precautions2 = disease_info[disease_name][0][1]
        # precautions3 = disease_info[disease_name][0][2]
        # precautions4 = disease_info[disease_name][0][3]
        occurrences = disease_info[disease_name][1]
        print("Precautions for", disease_name, ":", precautions)
        print("Occurrence of the disease:", occurrences)

    
    return render_template('desease.html', predicted_disease=predicted_disease, precautions=precautions, occurrences=occurrences)

@app.route('/nearby_hospitals')
def nearby_hospitals():
    
    
    return render_template('nearby_hospitals.html')

@app.route('/hospital_info', methods=['POST'])
def hospital_info():
  
    if request.method == 'POST':
        # Get the JSON data from the request
        data = request.get_json()

        # Process the received data as needed
        # For example, you can print the received data
        print("Received hospital names:", data)

        # You can also return a response if needed
        return jsonify({'message': 'Data received successfully'})
    else:
        return jsonify({'message not recieved'})

if __name__ == '__main__':
    app.run(debug=True)