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
    gridWidth = 83
    gridHeight = 30
    margin = 15
    grid = [[0]*10]*10
    running = True
    while running:
        win.fill ((0,0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
                    
        for row in range(10):
            for column in range(10):
                color = (255, 255, 255)
                pygame.draw.rect(win, 
                                 color, 
                                 [(margin + gridWidth) * column + margin,
                                  (margin + gridHeight) * row + margin,
                                  gridWidth,
                                  gridHeight])
        
        desclaimerText = f"Select for one symptom from the blocks above"
        blitdesclaimerText = text.render(desclaimerText.upper(), True, (161, 191, 35))
        win.blit(blitdesclaimerText, (220, 520))
        
        desclaimerText = f"or"
        blitdesclaimerText = text.render(desclaimerText.upper(), True, (77, 184, 216))
        win.blit(blitdesclaimerText, (470, 570))
        
        desclaimerText = f"Press Esc to go back"
        blitdesclaimerText = text.render(desclaimerText.upper(), True, (221, 136, 20))
        win.blit(blitdesclaimerText, (365, 620))
        
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
