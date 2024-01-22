from djitellopy import Tello

MAX_STEP_DISTANCE = 100
MAX_HEIGHT = 100

tello = Tello()

tello.connect()
battery_level = tello.get_battery()
print("Niveau de batterie : {}%".format(battery_level))

tello.takeoff(MAX_HEIGHT)
tello.move_forward(MAX_STEP_DISTANCE)
tello.move_forward(MAX_STEP_DISTANCE)
tello.move_forward(MAX_STEP_DISTANCE)
tello.rotate_counter_clockwise(90)
tello.move_back(MAX_STEP_DISTANCE)
tello.flip_back()
tello.flip_forward()
tello.flip_left()
tello.flip_right()
tello.move_forward(MAX_STEP_DISTANCE)
tello.rotate_counter_clockwise(270)
tello.land()