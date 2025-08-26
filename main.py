#Note: the image is in .gif and not .png or .jpg is because turtle only works with this one image format. so in order to display an image, we need to convert it into a .gif file
import os


os.environ['TCL_LIBRARY'] = r'C:\Program Files\Python313\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Program Files\Python313\tcl\tk8.6'

import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []


while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state name?")

    if answer_state is None:  # If user clicks "Cancel", exit the loop
        break

    answer_state = answer_state.title()  # Convert to title case

    if answer_state == "Exit":
        missing_states = [state for state in all_states if
                          state not in guessed_states]  # List comprehension to find missing states

        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

# we dont need this below code as we already have values but it will be needy to find out coordinates on the mouse click
# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)         #this is an event listener, so it's gonna listen when the mouse clicks and then it's going to call our get_mouse_click_coor() function and it's gonna pass over the X and Y coordinates of that click location
#
# turtle.mainloop()     #alternative way of keeping our screen open even though our code has finished running


#If answer_state is one of the states in all the states of the 50_states.csv
    if answer_state in all_states:     #note:  this is something that you wont be able to do so checking for membership using the "in" keyword unless you have converted the data in "all_states" to list
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]   #this pulls out the row
        t.goto(state_data.x.item(), state_data.y.item())   # by using ".item", this way we're accessing the single item contained in our Panda series
        #If they got it right:
        t.write(answer_state)    #create a turtle to write the name of the state at the state's x and y coordinate
