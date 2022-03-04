from turtle import Turtle, Screen
import pandas

screen = Screen()
bg = Turtle()
screen.title('U.S States Game')
background_img = 'blank_states_img.gif'
screen.setup(height=461, width=725)
screen.addshape(background_img)
bg.shape(background_img)

data = pandas.read_csv('50_states.csv')
all_states = data.state.to_list()


def new_state():
    turtle = Turtle(visible=False)
    turtle.penup()
    guess = data[data.state == answer]
    turtle.goto(int(guess.x), int(guess.y))
    turtle.write(answer, align='center', font=('Arial', 12, 'normal'))


correct_guesses = []
while True:
    answer = screen.textinput(title=f'{len(correct_guesses)}/50 States Correct', prompt='What\'s another state\'s name').title()
    if answer in all_states:
        new_state()
        correct_guesses.append(answer)
        all_states.remove(answer)
    elif answer == 'Exit':
        break

all_states = {'state': all_states}
all_states = pandas.DataFrame(all_states)
all_states.to_csv('missed_states.csv')
