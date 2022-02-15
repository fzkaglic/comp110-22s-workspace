"""EX04 - Valentine's Day Card.

Line 28 and Line 72 utilize the
turtle.write function. The while loop
spanning lines 44-47 uses the
turtle.circle function.
"""

__author__ = "730501608"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    love: Turtle = Turtle()
    date(love, 97.0, 120.0, 245, 4, 39)
    rose(love, -250.0, -100.0, 30, 232, 51, 51, 134, 12, 12)
    rose(love, -220.0, 20.0, 50, 251, 250, 79, 238, 152, 45)
    rose(love, -190.0, 85.0, 20, 225, 139, 236, 161, 50, 176)
    card(love, -50.0, 45.0, 180, 31, 109, 255, 217, 237)
    note(love, 100.0, -150.0, 195, 29, 53)
    done()


def date(love: Turtle, x: float, y: float, p_red: int, p_green: int, p_blue: int) -> None:
    """Announce the date for Valentine's Day."""
    love.penup()
    love.goto(x, y)
    love.setheading(0.0)
    love.pendown()
    love.color(p_red, p_green, p_blue)
    love.write("FEBRUARY 14", False, align="center", font=('Arial', 24, 'bold'))
    love.hideturtle()


def rose(love: Turtle, x: float, y: float, radius: int, p_red: int, p_green: int, p_blue: int, f_red: int, f_green: int, f_blue: int) -> None:
    """Draw a cute flower for Valentine's Day."""
    love.penup()
    love.goto(x, y)
    love.pendown()
    love.color((p_red, p_green, p_blue), (f_red, f_green, f_blue))
    love.begin_fill()
    i: int = 0
    while i < 5:
        love.circle(radius)
        love.right(100)
        i = i + 1
    love.end_fill()
    love.hideturtle()


def card(love: Turtle, x: float, y: float, p_red: int, p_green: int, p_blue: int, f_red: int, f_green: int, f_blue: int) -> None:
    """Draw a card for Valentine's Day."""
    love.penup()
    love.goto(x, y)
    love.setheading(0.0)
    love.pendown()
    love.color((p_red, p_green, p_blue), (f_red, f_green, f_blue))
    love.begin_fill()
    i: int = 0
    while i < 4:
        love.forward(300)
        love.right(90)
        i = i + 1
    love.end_fill()
    love.hideturtle()


def note(love: Turtle, x: float, y: float, p_red: int, p_green: int, p_blue: int) -> None:
    """Write a message for the Valentine's Day card."""
    love.penup()
    love.goto(x, y)
    love.setheading(0.0)
    love.pendown()
    love.pencolor(p_red, p_green, p_blue)
    love.write("Happy Valentine's Day, \nCOMP 110 Team!\n", False, align="center", font=('Times New Roman', 18, 'italic'))
    love.hideturtle()


if __name__ == "__main__":
    main()