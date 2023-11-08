from turtle import Turtle;
import random;

def random_colour():
    color = "#{:06x}".format(random.randint(0, 0xFFFFFF));
    return color;

class Ball(Turtle):
    def __init__(self):
        super().__init__();
        self.shape("square");
        self.color(random_colour())
        self.pu();
        # self.shapesize(stretch_wid=0.5, stretch_len=0.5);
        self.x_move = 10;
        self.y_move = 10;
    
    def move(self):
        new_x = self.xcor()+ self.x_move;
        new_y = self.ycor()+ self.y_move;
        self.goto(new_x, new_y);
    

    def bounce_y(self):
        self.y_move *= -1;

    def bounce_x(self):
        self.x_move *= -1;


    def reset_position(self):
        self.goto(0,0);
        self.bounce_x();