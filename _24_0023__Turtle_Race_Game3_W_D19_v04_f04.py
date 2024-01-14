
from turtle import Turtle, Screen
import random

is_game_on = False

screen = Screen()
screen.setup(width=500, height=400)   #this sets the width and heigth of a window of our choosing!! (use the Keyword arguements, because width and heigth
# could be inverted as default, so just specify them with Keyword arguements, for clarity! especially if someone else is going to be viewing your code (interviewer)


# TODO 1: Pick a color.

user_bet = screen.textinput(title="Make your bet!!", prompt="Which turtle will win the race? Enter a color: ")    #text input into the window
# print(user_bet)

turtle_colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [125, 75, 25, -25, -75, -125]

list_of_all_turtles = []   #make an empty list of turtles, and append to create the list



# TODO 2: Set up the Race properly.

#TOD #1


for turtle_index_iteration in range(0, 6):
    new_turtle_instance = Turtle(shape="turtle")
    new_turtle_instance.color(turtle_colors[turtle_index_iteration])
    new_turtle_instance.penup()
    new_turtle_instance.goto(x=-230, y=y_positions[turtle_index_iteration])
    list_of_all_turtles.append(new_turtle_instance)   #up until the line abive this one, we've created LOTS of turtles, but we haven't done anything with them! Generate this List, and append to add it!
    #individual instances


if user_bet: #(implied as default: (exists)) # if the user made a bet, then switch the game on!!
    is_game_on = True

while is_game_on:


    for new_turtle_instance in list_of_all_turtles:
        if new_turtle_instance.xcor() >= 230:
            winning_color = new_turtle_instance.pencolor()
            if winning_color == user_bet:
                print(f"Hay!! You won!!! The {winning_color} turtle is the winner!")
                is_game_on = False
            else:
                print(f"Sorry, bet again. The {winning_color} turtle was the winner.")
                is_game_on = False
        random_distance_pacing = random.randint(0, 10)
        new_turtle_instance.forward(random_distance_pacing)



# TODO 3: Run the Race

# TODO 4: Determine who won the Race.

# TODO 5: Tell us if we lost or won the game, and which color won the race!


screen.exitonclick()


#our turtles are 40 pixels wide (in turtle graphics), so we want to divide in half and subtract from the goalpost to get the official point of the Goalpost.
# 250 - (40 / 2) = 230


'''

Adding the turtles to a list allows you to easily manage and access them. In your program, you need to keep track of each turtle's position and attributes for various tasks like checking which turtle wins the race, moving the turtles, and other operations.

By adding the turtles to a list, you can:

Iterate through the list to update the positions of each turtle in the race loop.

Easily check if any turtle has reached the finish line (e.g., turtle.xcor() > 230).

Compare the color of the winning turtle with the user's bet.

Manage and modify the attributes of individual turtles more efficiently, especially when dealing with a dynamic number of turtles.

The list of turtles serves as a convenient way to organize and work with multiple turtle instances simultaneously. It's a common programming practice to use data structures like lists to store and manage multiple similar objects, making your code more structured and maintainable.

'''

'''
# apparently the body of the turtle is the pencolor

This code:

    for new_turtle_instance in list_of_all_turtles:
        if new_turtle_instance.xcor() >= 230:
            print(new_turtle_instance.color())
            
Results in this:

('orange', 'orange')
('orange', 'orange')
('orange', 'orange')
('orange', 'orange')
('purple', 'purple')
('orange', 'orange')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('yellow', 'yellow')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
('orange', 'orange')
('yellow', 'yellow')
('green', 'green')
('blue', 'blue')
('purple', 'purple')
('red', 'red')
'''