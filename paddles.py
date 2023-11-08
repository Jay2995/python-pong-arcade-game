from turtle import Turtle;

class Paddles(Turtle):
    def __init__(self, position, color):
        super().__init__();
        self.shape("square");
        self.color(color);
        self.pu();
        self.shapesize(stretch_wid=5, stretch_len=1);
        self.goto(position);
    

    def move_up(self):
        new_y = self.ycor() + 20;
        self.goto(self.xcor(), new_y);

    def move_down(self):
        new_y = self.ycor() - 20;
        self.goto(self.xcor(), new_y);






