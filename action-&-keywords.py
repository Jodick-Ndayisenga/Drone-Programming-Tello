from djitellopy import Tello

tello = Tello()
tello.connect()

def keywords_in_command(words: list, command: str):
    for word in words:
        if word.lower() in command.lower():
            return True
    return False

def do_action(command):
    """
    Cette fonction effectue une action correspondant à la commande vocale reçue.
    command (str): La commande vocale à traiter.
    """

    # Définition du dictionnaire de correspondance entre les actions et les commandes vocales
    actions = {
     'takeoff': ["d'école", 'décolle', 'démarre',"déconne","école"],
     'land': ['atterrit' , 'atterrir' , 'stop'],
     'move_forward': ['avance', 'avant'],
     'move_backward': ['récule' , 'arrière', 'recule'],
     'move_left': ['gauche'],
     'move_right': ['droite'],
     'flip_forward': ['tourne', 'roule', 'rôle','flip'],
     #
     'flip_left': ['flip gauche'],
     'flip_back': ['flip arrière'],
     'flip_forward1': ['flip avant'],
     'flip_right': ['flip droit'],
     
    }

    # Pour chaque action possible, vérifie si la commande vocale correspond 
    # à l'action si c'est le cas, effectue l'action correspondante sur le drone

    if keywords_in_command(actions['takeoff'], command) :
        print("Decoded Text : {}".format(actions['takeoff']))
        tello.takeoff()
    
    if keywords_in_command(actions['land'], command) :
        print("Decoded Text : {}".format(actions['land']))
        tello.land()
        
    if keywords_in_command(actions['move_forward'], command) :
        print("Decoded Text : {}".format(actions['move_forward']))
        tello.move_forward(100) 
      
    if keywords_in_command(actions['move_backward'], command) :
        tello.move_back(100)
        print("Decoded Text : {}".format(actions['move_backward']))
    
    if keywords_in_command(actions['move_left'], command) :
        tello.move_left(100)
        print("Decoded Text : {}".format(actions['move_left']))
        
    if keywords_in_command(actions['move_right'], command):
        tello.move_right(100)
        print("Decoded Text : {}".format(actions['move_right']))
        
    if keywords_in_command(actions['flip_forward'], command):
        tello.flip_forward()
        print("Decoded Text : {}".format(actions['flip_forward']))
        
    #
    if keywords_in_command(actions['flip_left'], command):
         tello.flip_left()
         print("Decoded Text : {}".format(actions['flip_left']))
    if keywords_in_command(actions['flip_back'], command):
        tello.flip_back()
        print("Decoded Text : {}".format(actions['flip_back']))
    if keywords_in_command(actions['flip_right'], command):
        tello.flip_right()
        print("Decoded Text : {}".format(actions['flip_right']))
    if keywords_in_command(actions['flip_forward1'], command):
        tello.flip_forward()
        print("Decoded Text : {}".format(actions['flip_forward']))
        