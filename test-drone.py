from djitellopy import Tello

def initialize_tello():
    tello = Tello()    
    try:
        tello.connect()
        return tello
    except Exception as e:
        return None

if __name__ == "__main__":
    tello = initialize_tello()
    if tello is not None:
        print ("Drône initialisé!")
        battery_level = tello.get_battery()
        print("Niveau de batterie : {}%".format(battery_level))
    else:
        print("Échec de l'initialisation du drone.")
