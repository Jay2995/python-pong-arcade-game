from turtle import Turtle;
from turtle import Screen;
from paddles import Paddle;

screen = Screen();
screen.bgcolor("black");
screen.setup(width= 800, height= 600);
screen.title("Pong arcade");
screen.tracer(0);


paddles = Paddle();



screen.listen();

screen.onkey(paddles.move_up, "Up");
screen.onkey(paddles.move_down, "Down");


game_is_running = True;
while game_is_running:
    screen.update();







screen.exitonclick()