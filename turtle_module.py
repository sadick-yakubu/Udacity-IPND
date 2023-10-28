import turtle
Amy = turtle.Turtle()
rainbow = ["red", "orange", "yellow", "green", "blue", "purple"]
Amy.width(5)
for color in rainbow:
    Amy.color(color)
    for side in [1, 2, 3, 4, 5]:
        Amy.forward(50)
        Amy.right(144)
    Amy.right(60)
    Amy.penup()
    Amy.forward(50)
    Amy.pendown()

turtle.Screen().exitonclick()