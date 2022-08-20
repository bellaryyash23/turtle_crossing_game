import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Tutle Crossing Game")
screen.tracer(0)
screen.setup(width=600, height=600)
screen.listen()
player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    car_manager.create_car()
    car_manager.move_car()

    # Detect collision with car
    for car in car_manager.all_cars:
        if car.distance(player) < 22:
            scoreboard.game_over()
            game_is_on = False

    # Detect level up condition
    if player.ycor() > 260:
        player.start()
        scoreboard.level_up()
        car_manager.level_up()


screen.exitonclick()
