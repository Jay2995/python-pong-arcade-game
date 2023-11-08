from turtle import Turtle;
from turtle import Screen;
from paddles import Paddles;
from ball import Ball;
from scoreboard import Scoreboard;
import time;


screen = Screen();
screen.bgcolor("black");
screen.setup(width= 800, height= 600);
screen.title("Pong arcade");
screen.tracer(0);


paddle_r = Paddles((350, 0),"Green");
paddle_l = Paddles((-350,0), "Blue");
ball = Ball();
scoreboard = Scoreboard();


screen.listen();

screen.onkey(paddle_r.move_up, "Up");
screen.onkey(paddle_r.move_down, "Down");
screen.onkey(paddle_l.move_up, "w");
screen.onkey(paddle_l.move_down, "s");


game_is_running = True;
while game_is_running:
    time.sleep(ball.move_speed);
    screen.update();
    ball.move();

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y();
    
    if ball.xcor() > 320 and ball.distance(paddle_r) < 50 or ball.xcor() < -320 and ball.distance(paddle_l) < 50:
        ball.bounce_x()
    

    if ball.xcor() > 380:
        ball.reset_position();  
        scoreboard.add_score_l();
    

    if ball.xcor() < -380:
        ball.reset_position();
        scoreboard.add_score_r();

    







screen.exitonclick()