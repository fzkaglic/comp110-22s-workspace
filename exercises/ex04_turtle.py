"""EX04 - Valentine's Day Card."""

__author__ = "730501608"

from turtle import Turtle, colormode, done
colormode(255)


def main() -> None:
    """The entrypoint of my scene."""
    love: Turtle = Turtle()
    cupid: Turtle = Turtle()
    rose(love, -250.0, -100.0, 30, 232, 51, 51, 134, 12, 12)
    rose(love, -220.0, 20.0, 50, 251, 250, 79, 238, 152, 45)
    arrow(cupid, -230.0, 45.0, 251, 250, 79, 238, 152, 45)
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


def arrow(cupid: Turtle, x: float, y: float, p_red: int, p_green: int, p_blue: int, f_red: int, f_green: int, f_blue: int) -> None:
    """Draw Cupid's arrows for Valentine's Day."""
    cupid.penup()
    cupid.goto(x, y)
    cupid.pendown()
    cupid.color((p_red, p_green, p_blue), (f_red, f_green, f_blue))
    cupid.begin_fill()
    cupid.shape("arrow")
    cupid.end_fill()
    cupid.hideturtle()


if __name__ == "__main__":
    main()