import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

a = turtle.Turtle()
a.hideturtle()
a.penup()
x = 0
state_list = []
data = pandas.read_csv("50_states.csv")
master_states = data["state"].to_list()

while x < 51:
        answer_state = screen.textinput(title=f"{x}/50 States Correct", prompt="What's another states name").title()
        if answer_state in master_states:
            state = data[data.state == answer_state]
            x_cor = int(state.x)
            y_cor = int(state.y)
            a.goto(x_cor,y_cor)
            a.write(answer_state)
            x += 1
            state_list.append(answer_state)
        if answer_state =='Exit':
            missing_states = list(set(master_states)- set(state_list))
            with open("missing_states.csv", "w") as f:
                f.write(str(missing_states))

screen.exitonclick()