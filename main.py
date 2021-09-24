from tkinter import *
import numpy as np
import pandas as pd

#List of the symptoms is listed here in list l1.
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

# List of Diseases is listed in list disease.
disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
' Migraine','Cervical spondylosis',
'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
'Impetigo']

l2=[]
for i in range(0,len(l1)):
    l2.append(0)


df=pd.read_csv("Prototype.csv")

# Replace the values in the imported file by pandas by the inbuilt function replace in pandas.
df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

#check the df
#print(df.head())

X= df[l1]

#print(X)

y = df[["prognosis"]]
np.ravel(y)

#print(y)

#Read a csv named Testing.csv

tr=pd.read_csv("Prototype-1.csv")

#Use replace method in pandas.

tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
'Migraine':11,'Cervical spondylosis':12,
'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
'(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
'Impetigo':40}},inplace=True)

X_test= tr[l1]
y_test = tr[["prognosis"]]

#print(y_test)

np.ravel(y_test)

def DecisionTree(psymptoms):
    from sklearn import tree

    clf3 = tree.DecisionTreeClassifier()
    clf3 = clf3.fit( X, y )

    from sklearn.metrics import accuracy_score
    y_pred = clf3.predict( X_test )
    print( accuracy_score( y_test, y_pred ) )
    print( accuracy_score( y_test, y_pred, normalize=False ) )

    # psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range( 0, len( l1 ) ):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf3.predict( inputtest )
    predicted = predict[0]

    h = 'no'
    for a in range( 0, len( disease ) ):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        return disease[a]
    else:
        return 'Not Found'


def randomforest(psymptoms):
    from sklearn.ensemble import RandomForestClassifier
    clf4 = RandomForestClassifier()
    clf4 = clf4.fit( X, np.ravel( y ) )

    # calculating accuracy
    from sklearn.metrics import accuracy_score
    y_pred = clf4.predict( X_test )
    print( accuracy_score( y_test, y_pred ) )
    print( accuracy_score( y_test, y_pred, normalize=False ) )

    # psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]

    for k in range( 0, len( l1 ) ):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = clf4.predict( inputtest )
    predicted = predict[0]

    h = 'no'
    for a in range( 0, len( disease ) ):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        return disease[a]
    else:
        return 'Not Found'
    

def NaiveBayes(psymptoms):
    from sklearn.naive_bayes import GaussianNB
    gnb = GaussianNB()
    gnb = gnb.fit( X, np.ravel( y ) )

    from sklearn.metrics import accuracy_score
    y_pred = gnb.predict( X_test )
    print( accuracy_score( y_test, y_pred ) )
    print( accuracy_score( y_test, y_pred, normalize=False ) )

    # psymptoms = [Symptom1.get(), Symptom2.get(), Symptom3.get(), Symptom4.get(), Symptom5.get()]
    for k in range( 0, len( l1 ) ):
        for z in psymptoms:
            if (z == l1[k]):
                l2[k] = 1

    inputtest = [l2]
    predict = gnb.predict( inputtest )
    predicted = predict[0]

    h = 'no'
    for a in range( 0, len( disease ) ):
        if (predicted == a):
            h = 'yes'
            break

    if (h == 'yes'):
        return disease[a]
    else:
        return "Not Found" 
    
    
# print(l1)
# print(len(l1))

# convert l1 to 2D list of 6*16
from itertools import islice 
  
def convert(lst, var_lst): 
    idx = 0
    for var_len in var_lst: 
        yield lst[idx : idx + var_len] 
        idx += var_len 

n = [6]*16
symptomsList = list(convert(l1, n))
for i in symptomsList:
    print(len(i), i)


# GUI Starts here
import pygame

# Initialize
pygame.init()
clock = pygame.time.Clock()

# Screen
win = pygame.display.set_mode((1000, 700))

# Color
colorActive = (255, 255, 255)
colorPassive = (150, 150, 150)

# Title
pygame.display.set_caption("Disease Predictor")
 
# bg
bg = pygame.image.load("bg1.jpg")
bg = pygame.transform.scale(bg, (1000, 700))

# Main Text
mainText = pygame.font.Font(None, 80)
mText1 = "Disease"
mText2 = "Predictor"

text = pygame.font.Font(None, 30)

# Patient Name
nameText = "Patient's Name"
name = ''
recName = pygame.Rect(220,135,150,30)
activeName = False

# Symptoms
button = pygame.font.Font(None, 25)
symptomText = "Choose Symptoms"
symtom1Text = "Symptom 1"
symptom1Button = pygame.Rect(60, 240, 100, 30)
symtom2Text = "Symptom 2"
symptom2Button = pygame.Rect(240, 240, 100, 30)
symtom3Text = "Symptom 3"
symptom3Button = pygame.Rect(420, 240, 100, 30)
symtom4Text = "Symptom 4"
symptom4Button = pygame.Rect(600, 240, 100, 30)
symtom5Text = "Symptom 5"
symptom5Button = pygame.Rect(780, 240, 100, 30)

pressed1 = False
pressed2 = False
pressed3 = False
pressed4 = False
pressed5 = False


def symptoms():
    gridWidth = 149
    gridHeight = 25
    margin = 15
    text = pygame.font.SysFont('calibri', 13)
    
    running = True
    while running:
        win.fill ((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        for row in range(16):
            for column in range(6):
                color = (255, 255, 255)
                
                pygame.draw.rect(win, 
                                 color, 
                                 [(margin + gridWidth) * column + margin,
                                  (margin + gridHeight) * row + margin,
                                  gridWidth,
                                  gridHeight])
                
                try:
                    blitSymptomTextList = text.render(symptomsList[row][column], True, (0,0,0))
                    win.blit(blitSymptomTextList, ((margin + gridWidth) * column + 10 + margin, (margin + gridHeight) * row + 5 + margin))
                except:
                    pass
        
        desclaimerText = f"Select for one symptom from the blocks above or Press ESC to go back"
        blitdesclaimerText = text.render(desclaimerText.upper(), True, (77, 184, 216))
        win.blit(blitdesclaimerText, (75, 660))
                
        pygame.display.update()
        clock.tick(30)
        
        
# Submit
submitText = "SUBMIT"
submitButton = pygame.Rect(450, 320, 100, 40)
submitPressed = False

# Result
recResult = pygame.Rect(80,400,840,80)

run = True
while run:
    win.fill((255,255,255))
    mouse = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            if recName.collidepoint(event.pos):
                activeName = True
            else:
                activeName = False
        
            if symptom1Button.collidepoint(event.pos):
                pressed1 = True    
            if symptom2Button.collidepoint(event.pos):
                pressed2 = True    
            if symptom3Button.collidepoint(event.pos):
                pressed3 = True    
            if symptom4Button.collidepoint(event.pos):
                pressed4 = True    
            if symptom5Button.collidepoint(event.pos):
                pressed5 = True   
                
            if submitButton.collidepoint(event.pos):
                submitPressed = True 
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN or event.key == pygame.K_KP_ENTER:
                activeName = False
            
            if activeName:
                if event.key == pygame.K_BACKSPACE:
                    name = name[:-1]
                else:
                    name += event.unicode
        
        # Background Image
        win.blit(bg, [0,0])
        
        # Render Main Text
        blitMainText1 = mainText.render(mText1, True, (255,255,255))
        win.blit(blitMainText1, (40, 40)) 
        
        blitMainText2 = mainText.render(mText2, True, (249, 209,0))
        win.blit(blitMainText2, (270, 40)) 
        
        # Patient Name
        blitNameText = text.render(nameText, True, (255,255,255))
        win.blit(blitNameText, (50, 140))
                
        if activeName:
            boxColor = colorActive
        else:
            boxColor = colorPassive
        pygame.draw.rect(win, boxColor, recName, 3)
        blitNameIP = button.render(name, True, (255,255,255))
        win.blit(blitNameIP, (230, 142))
        recName.w = max(150, blitNameIP.get_width() + 20)
        
        # Symptom
        blitSymtomText = text.render(symptomText, True, (255, 255, 255))
        win.blit(blitSymtomText, (50, 200))

        if 60 + 100 > mouse[0] > 60 and 240 + 30 > mouse[1] > 240:
            pygame.draw.rect(win, (255, 255, 255), symptom1Button)
            blitSymptom1Button = button.render(symtom1Text, True, (77, 184, 216))
            win.blit(blitSymptom1Button, (65, 245))
        else:
            pygame.draw.rect(win, (77, 184, 216), symptom1Button)
            blitSymptom1Button = button.render(symtom1Text, True, (0,0,0))
            win.blit(blitSymptom1Button, (65, 245))
        
        if 240 + 100 > mouse[0] > 240 and 240 + 30 > mouse[1] > 240:
            pygame.draw.rect(win, (255, 255, 255), symptom2Button)
            blitSymptom2Button = button.render(symtom2Text, True, (161, 191, 35))
            win.blit(blitSymptom2Button, (245, 245))
        else:
            pygame.draw.rect(win, (161, 191, 35), symptom2Button)
            blitSymptom2Button = button.render(symtom2Text, True, (0,0,0))
            win.blit(blitSymptom2Button, (245, 245))
        
        if 420 + 100 > mouse[0] > 420 and 240 + 30 > mouse[1] > 240:
            pygame.draw.rect(win, (255, 255, 255), symptom3Button)
            blitSymptom3Button = button.render(symtom3Text, True, (47, 107, 177))
            win.blit(blitSymptom3Button, (425, 245))
        else:
            pygame.draw.rect(win, (47, 107, 177), symptom3Button)
            blitSymptom3Button = button.render(symtom3Text, True, (0,0,0))
            win.blit(blitSymptom3Button, (425, 245))
        
        if 600 + 100 > mouse[0] > 600 and 240 + 30 > mouse[1] > 240:
            pygame.draw.rect(win, (255, 255, 255), symptom4Button)
            blitSymptom4Button = button.render(symtom4Text, True, (221, 136, 20))
            win.blit(blitSymptom4Button, (605, 245))
        else:
            pygame.draw.rect(win, (221, 136, 20), symptom4Button)
            blitSymptom4Button = button.render(symtom4Text, True, (0,0,0))
            win.blit(blitSymptom4Button, (605, 245))
        
        if 780 + 100 > mouse[0] > 780 and 240 + 30 > mouse[1] > 240:
            pygame.draw.rect(win, (255, 255, 255), symptom5Button)
            blitSymptom5Button = button.render(symtom5Text, True, (224, 34, 36))
            win.blit(blitSymptom5Button, (785, 245))
        else:    
            pygame.draw.rect(win, (224, 34, 36), symptom5Button)
            blitSymptom5Button = button.render(symtom5Text, True, (0,0,0))
            win.blit(blitSymptom5Button, (785, 245))
            
        if pressed1 or pressed2 or pressed3 or pressed4 or pressed5:
            symptoms()
            if pressed1:
                pass
            if pressed2:
                pass
            if pressed3:
                pass
            if pressed4:
                pass
            if pressed5:
                pass
        
        pressed1 = False
        pressed2 = False
        pressed3 = False
        pressed4 = False
        pressed5 = False
        
        # Submit Button
        if 450 + 100 > mouse[0] > 450 and 320 + 40 > mouse[1] > 320:
            pygame.draw.rect(win, (255,255,255), submitButton)
            blitSubmitButton = button.render(submitText, True, (143,37,129))
            alignCenter = blitSubmitButton.get_rect(center=(500, submitButton.y + 20))
            win.blit(blitSubmitButton, alignCenter)
            
        else:
            pygame.draw.rect(win, (143, 37, 129), submitButton)
            blitSubmitButton = button.render(submitText, True, (255,255,255))
            alignCenter = blitSubmitButton.get_rect(center=(500, submitButton.y + 20))
            win.blit(blitSubmitButton, alignCenter)
        
        # Prediction Print
        resultText = f"Hey {name}, we think that you are suffering from either of below:"
        pygame.draw.rect(win, (255, 255, 255), recResult, 3)
        # x = False
        # if submitPressed:
        #     if len(name)==0:
        #             blitErrorName = text.render("(Please Enter Name)", True, (255, 0, 0))
        #             win.blit(blitErrorName, (420, 140))
        #             submitPressed == False
        #             x = False
        #     if pressed1 == False and pressed2 == False and pressed3 == False and pressed4 == False and pressed5 == False:
        #             blitErrorSymptom = text.render("(Please Select atleast 1 Symptom)", True, (255, 0, 0))
        #             win.blit(blitErrorSymptom, (300, 200))
        #             submitPressed == False
        #             x = False
        #     if len(name)>0 and (pressed1 == True or pressed2 == True or pressed3 == True or pressed4 == True or pressed5 == True):
        #         x = True
                
        if submitPressed:
            blitResultText = text.render(resultText, True, (255, 255, 255))
            alignCenter = blitResultText.get_rect(center=(500, 440))
            win.blit(blitResultText, alignCenter)
                
        # Display Update
        pygame.display.update()
        clock.tick(120)
        
pygame.quit()
