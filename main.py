import turtle
import pandas

FONT = 'monaco', 15, "bold"

screen= turtle.Screen()
screen.title("Indian States Game")
image="political_map.gif"
screen.setup(height=1037,width=881)
screen.addshape(image)
turtle.shape(image)

#********* CODE TO GET THE COORDINATES OF THE STATES IN MAP ***************
"""
states_of_india = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal"]
states_data={"state":states_of_india,"x":[],"y":[]}
def get_mouse_click_coor(x, y):
    states_data["x"].append(x)
    states_data["y"].append(y)
    print(states_data)
def save_to_csv():
    converted_data=pandas.DataFrame(states_data)
    converted_data.to_csv("states_data_file.csv",index=False)
    print("worked!!!!")
turtle.onscreenclick(get_mouse_click_coor)
turtle.listen()
print("press key!")
turtle.onkey(save_to_csv,"space")

turtle.mainloop()
"""

states_data=pandas.read_csv("states_data_file.csv")
guessedStates=[]
correctAnswer=0
totalStates=28
def checkAnswer(answer):
    print(answer.title())
    if(answer.title() in states_data["state"].tolist() and answer.title() not in guessedStates):
        guessedStates.append(answer.title())
        return True
    else:
        return False
def writeToMap(answer):
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(int(states_data[states_data["state"]==answer.title()].x.iloc[0]),int(states_data[states_data["state"]==answer.title()].y.iloc[0]))
    t.pendown()
    t.write(answer.title(),font=FONT)

def textBoxFocus(): #FIXED- TEXTBOX GETTING OUT OF FOCUS AFTER WRONG ANSWER!
    t=turtle.Turtle()
    t.hideturtle()
    t.penup()
    t.goto(0,0)

def winPrompt():
    tu=turtle.Turtle()
    tu.hideturtle()
    tu.penup()
    tu.goto(0,330)
    tu.pendown()
    tu.write("YOU WON THE GAME!",font=('monaco',30,"bold"))

while(True):
    answer=""
    print()
    if(correctAnswer==0):
        answer=turtle.textinput("Guess the State", "Enter a State name:")
    else:
        answer=turtle.textinput(f"{correctAnswer}/{totalStates} correct guesses","Enter a State Name:")
    if(checkAnswer(answer)==True):
        correctAnswer+=1
        writeToMap(answer)
    else:
        textBoxFocus()

    if(correctAnswer==28):
        print("YOU WON!")
        winPrompt()
        break


turtle.exitonclick()

