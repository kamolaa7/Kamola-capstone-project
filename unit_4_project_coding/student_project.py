"""
Lists
Student Project
Project Title: Ms. Leva's Students
"""

## -- Import library -- ##
import tsapp
import random

## -- Ms. Leva's Classrooms' Set Up -- ##
window = tsapp.GraphicsWindow()
background = tsapp.Sprite("Frame.jpg", 0, 0)
class1 = tsapp.Sprite("CanvasSmall.png", 200, 250, 0.7)
class2 = tsapp.Sprite("CanvasSmall.png", 600, 250, 0.7)
class1_num = tsapp.TextLabel("Archivo-MediumItalic.ttf", 90, 240, 390, 100, "201", tsapp.GRAY)
class2_num = tsapp.TextLabel("Archivo-MediumItalic.ttf", 90, 640, 390, 100, "202", tsapp.GRAY)

# Class 1 background
class1_back = tsapp.Sprite("TextBoxBlackboardWide.png", 0, -30, 2.45)

# Class 2 background
class2_back = tsapp.Sprite("TextBoxBlackboardWide.png", 0, -30, 2.45)

# Asks user what classroom they want to see
show_text = tsapp.TextLabel("Archivo-Regular.ttf", 30, 143, 175, 800, 
                            "Which classroom would you like to see today?", tsapp.WHITE)

# Class 201 data list
class1_names = ["Oliver", "Charlette", "William", "Pat", "Mia", "Lucy"]
class1_scores = ["90", "81", "85", "96", "100", "98"]
# Updated list
class1_updated = []

# Class 202 data list
class2_names = ["Linda", "Lucas", "Noah", "Carmel", "Carlos", "Nora"]
class2_scores = ["89", "92", "89", "90", "96", "100"]
# Updated list
class2_updated = []

# Ask if user is ready b/c the sprites don't show unless user inputs something
ready1 = input("Click enter to continue")

## -- Main Loop -- ##
while window.is_running:
    # Add background sprites
    window.add_object(background)
    window.add_object(show_text)
    window.add_object(class1)
    window.add_object(class2)
    # Add and bring class #s in front of canvas
    window.add_object(class1_num)
    window.add_object(class2_num)
    window.move_to_front(class1_num)
    window.move_to_front(class2_num)
    
    # Shows class 201 data
    x, y = tsapp.get_mouse_position() 
    
    if class1.is_colliding_point(x,y) and tsapp.was_mouse_pressed():
        
        background.visible = False
        class1.visible = False
        class2.visible = False
        class1_num.visible = False
        class2_num.visible = False
        show_text.visible = False
        # Overlay class1's background
        window.add_object(class1_back)
        
        # Loop through each student and position them dynamically
        for i in range(len(class1_names)):
            class1_all = class1_names[i] + ": " + class1_scores[i] + "%"
            # Calculate y position of names
            y_position = 70 + (i * 90)  # 90 spaces between each line
            # Create the TextLabel
            name_text = tsapp.TextLabel("Graduate-Regular.ttf", 40, 100, y_position, 800, class1_all, tsapp.WHITE)
            name_text.align = "center"  # Center the text 
            class1_updated.append(name_text)
            window.add_object(name_text)     
        
        
        # Finish the frame so that user can answer inside the console 
        window.finish_frame()
        
        # Start loop so user can enter and change however much they like to
        while True:
            # Ask user which student's score they want to change
            student = input("Enter student name whose score you want to change (or type 'exit' to go back) ")
            
            # Exit and return to main page
            if student == "exit":
                # Makes main page visible
                background.visible = True
                class1.visible = True
                class2.visible = True
                class1_num.visible = True
                class2_num.visible = True
                show_text.visible = True
                break
                
            # Check is student is in list of 201 class names
            if student in class1_names: 
                # Ask what score user wants to change current score to
                new_score = str(input("Enter " + student + "'s new score: "))
                # Checks if new_score input is a digit
                while not new_score.isdigit():
                    new_score = str(input("Please enter a valid number"))
                    
                # Create for range loop to find index and elements
                for i in range(len(class1_names)):
                    if class1_names[i] == student:
                        # Updates scores 
                        class1_scores[i] = new_score
                        # Changes the text labels displayed to user's new score
                        class1_updated[i].text = student + ": " + new_score + "%"     
                        window.finish_frame()
            
    
    # Shows class 202 data  
    if class2.is_colliding_point(x,y) and tsapp.was_mouse_pressed():
        background.visible = False
        class1.visible = False
        class2.visible = False
        class1_num.visible = False
        class2_num.visible = False
        show_text.visible = False
        # Show class2's background
        window.add_object(class2_back)
        
        # Loop through each student and position them dynamically
        for i in range(len(class2_names)):
            class2_all = class2_names[i] + ": " + class2_scores[i] + "%"
            
            # Calculate y position of names
            y_position = 70 + (i * 90)  # Adds 90 spaces between each line
            
            # Create the TextLabel
            name_text = tsapp.TextLabel("Graduate-Regular.ttf", 40, 100, y_position, 800, class2_all, tsapp.WHITE)
            name_text.align = "center"  # Center the text 
            # Add to updated list
            class2_updated.append(name_text)
            window.add_object(name_text)   
        
        # Finish the frame so that user can answer inside the console 
        window.finish_frame()
        
        
        # Start identical loop for class 202
        while True:
            # Ask user which student's score they want to change
            student = input("Enter student name whose score you want to change (or type 'exit' to go back) ")
            
            
            # Exit and return to main page
            if student == "exit":
                # Makes main page visible
                background.visible = True
                class1.visible = True
                class2.visible = True
                class1_num.visible = True
                class2_num.visible = True
                show_text.visible = True
                break
                
                
            # This if condition is to continue with the updating score
            if student in class2_names: 
                # Ask what score user wants to change current score to
                new_score = str(input("Enter " + student + "'s new score: "))
                # Checks if new_score input is a digit
                while not new_score.isdigit():
                    new_score = str(input("Please enter a valid number"))
                # Create for range loop to find index and elements
                for i in range(len(class2_names)):
                    # Check's if the name of student is in the class 201 list of names
                    if class2_names[i] == student:
                        # Updates scores 
                        class2_scores[i] = new_score
                        # Changes the text labels displayed to user's new score
                        class2_updated[i].text = student + ": " + new_score + "%"                      
                        window.finish_frame()
             
                    
    
    window.finish_frame()










