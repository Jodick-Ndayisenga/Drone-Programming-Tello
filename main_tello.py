from djitellopy import Tello
import time

tello = Tello()

tello.connect()

battery_level = tello.get_battery()
print("Niveau de batterie : {}%".format(battery_level))

tello.takeoff()
time.sleep(3)

while True:
    commande = input("Commande: ").lower()
    if commande == "stop":
        tello.land()
        time.sleep(3)
    else:
        if commande == "fo":
            tello.move_forward(100)
            time.sleep(3)

        elif commande == "left":
            tello.move_left(100)
            time.sleep(3)

        elif commande == "flipfo":
            tello.flip_forward()
            time.sleep(3)
        elif commande == "fliple":

            tello.flip_left()
            time.sleep(3)

        elif commande == "flipri":
            tello.flip_right()
            time.sleep(3)

        elif commande == "flipba":

            tello.flip_back()
            time.sleep(3)
        elif commande == "moveri":
            tello.move_right(100)
            time.sleep(3)

        elif commande == "rotate":
            tello.rotate_counter_clockwise(360)
            time.sleep(3)
        else:
            tello.move_forward(100)
            time.sleep(3)

