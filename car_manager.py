from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_SPEED = 5
MOVE_INCREMENT = 10


class Cars(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars = []
        self.hideturtle()
        self.current_speed = STARTING_SPEED

    def generate_car(self):
        car_position = random.randint(-240, 240)
        car_color = random.choice(COLORS)
        random_chance = random.randint(1, 6)

        if random_chance == 6:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.setheading(180)
            new_car.color(car_color)
            new_car.goto(320, car_position)
            self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
            x_position = car.xcor() - self.current_speed
            car.goto(x_position, car.ycor())

    def increase_speed(self):
        self.current_speed += MOVE_INCREMENT

    def refresh(self):
        for actual_car in self.all_cars:
            actual_car.hideturtle()
        self.all_cars.clear()
