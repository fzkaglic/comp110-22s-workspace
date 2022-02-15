"""EX04 - Valentine's Day Card."""

__author__ = "730501608"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    love: Turtle = Turtle()
    joy: Turtle = Turtle()
    rose(love, -250.0, -100.0, 30, 232, 51, 51, 134, 12, 12)
    rose(love, -250.0, -100.0, 60, 251, 250, 79, 238, 152, 45)
    heart(joy, -115.0, -50.0, 251, 250, 79, 238, 152, 45)
    heart(joy, 0.0, -50.0, 251, 250, 79, 238, 152, 45)
    done()


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


def heart(joy: Turtle, x: float, y: float, p_red: int, p_green: int, p_blue: int, f_red: int, f_green: int, f_blue: int) -> None:
    """Draw a heart for Valentine's Day."""
    joy.penup()
    joy.goto(x, y)
    joy.pendown()
    joy.color((p_red, p_green, p_blue), (f_red, f_green, f_blue))
    joy.begin_fill()
    joy.shape("heart")
    joy.hideturtle()


if __name__ == "__main__":
    main()