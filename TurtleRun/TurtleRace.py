
from turtle import Turtle, Screen
import random

#Winnie Kam

class TurtleRace:
    NUM_OF_TURTLES = 5
    SCREEN_WIDTH = 500
    SCREEN_HEIGHT = 500
    SIZE_OF_TURTLE = 40
    INIT_X = -1 * SCREEN_WIDTH / 2 + SIZE_OF_TURTLE * 2
    INIT_Y = -1 * SCREEN_HEIGHT / 4
    STEP = 30
    TURTLES_SPACE_APART = 50
    COLOR_MODE = 255

    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=self.SCREEN_WIDTH, height=self.SCREEN_HEIGHT)
        self.screen.colormode(self.COLOR_MODE)
        self._initialize_turtles()

    def _initialize_turtles(self):
        x = self.INIT_X
        y = self.INIT_Y
        self.turtles_list = []
        turtle_colors_selection = ["red", "orange", "green", "blue", "purple", "pink"]
        assert len(turtle_colors_selection) >= self.NUM_OF_TURTLES, "not enough color to choose from"
        for i in range(self.NUM_OF_TURTLES):
            turtle_color = random.choice(turtle_colors_selection)
            turtle_colors_selection.remove(turtle_color)
            cur_turtle = Turtle()
            self.turtles_list.append(cur_turtle)
            cur_turtle.penup()
            cur_turtle.shape("turtle")
            cur_turtle.color(turtle_color)
            cur_turtle.setpos(x=x, y=y)
            y += self.TURTLES_SPACE_APART

    def run_race(self, turtle):
        turtle.forward(random.randint(1, self.STEP))

    def at_finish_line(self, turtle):
        (x, y) = turtle.position()
        if x >= self.SCREEN_WIDTH / 2 - self.SIZE_OF_TURTLE:
            print(f"{turtle.color()[1]} turtle won")
            return True
        return False

    def start_race(self):
        race_on = True
        while race_on:
            for turtle in self.turtles_list:
                self.run_race(turtle)
                if self.at_finish_line(turtle):
                    race_on = False
                    break
        self.screen.exitonclick()


race = TurtleRace()
race.start_race()
