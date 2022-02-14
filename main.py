import turtle
import player
import car_manager
import time
import scoreboard

screen = turtle.Screen()
screen.setup(600, 600)
screen.tracer(0)

player = player.Player()
scoreboard = scoreboard.Scoreboard()
cars = car_manager.Cars()

screen.listen()
screen.onkey(player.move_up, "Up")

keep_running = True
while keep_running:
    time.sleep(0.1)
    screen.update()
    cars.generate_car()
    cars.move_car()

    if player.ycor() > 280:
        player.reposition()
        scoreboard.update()
        cars.increase_speed()
        cars.refresh()

    for some_car in cars.all_cars:
        if some_car.distance(player) < 20:
            scoreboard.game_over()
            keep_running = False

screen.exitonclick()