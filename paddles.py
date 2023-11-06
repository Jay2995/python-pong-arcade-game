from turtle import Turtle;

class Paddle():
    def __init__(self):
        self.paddle = Turtle("square");
        self.paddle.color("green");
        self.paddle.pu();
        self.paddle.shapesize(stretch_wid=5, stretch_len=1);
        self.paddle.goto(x=350, y=0);
    

    def move_up(self):
        new_y = self.paddle.ycor() + 20;
        self.paddle.goto(self.paddle.xcor(), new_y);

    def move_down(self):
        new_y = self.paddle.ycor() - 20;
        self.paddle.goto(self.paddle.xcor(), new_y);