import turtle
import pandas
screen = turtle.Screen()
tim = turtle.Turtle()
image = "blank_states_img.gif"
screen.addshape(image)
tim.shape(image)

# Use to this code to find coordinates of states
# def sates_cor(a, b):
#     print(a, b)
# turtle.onscreenclick(sates_cor)
# turtle.mainloop()
data = pandas.read_csv("50_states.csv")
all_data = data.state.to_list()
guesses_state = []


while len(guesses_state) < 50:
    answer_state = screen.textinput(title=f"{len(guesses_state)}/50 correct answer", prompt="Whats another States name?").title()
    if answer_state == "Exit":
        missing_states =[]
        for state_1 in all_data:
            if state_1 not in guesses_state:
                missing_states.append(state_1)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("state_to_learn.csv")
        break

    if answer_state in all_data:
        state = data[data.state == answer_state]
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()
        t.goto(int(state.x), int(state.y))
        t.write(answer_state)
        guesses_state.append(answer_state)

# screen.exitonclick()
