import speech_recognition as sr
from djitellopy import Tello

def initialize_tello():
    tello = Tello()    
    try:
        tello.connect()
        print('La batterie est à : ', tello.query_battery(),"%")
        return tello
    except Exception as e:
        return None
    
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
       
    

def recognize_speech_from_mic(recognizer, microphone):
    """Transcrire la parole enregistrée à partir du `microphone`."""

    # Vérifier que les arguments de reconnaissance et de microphone 
    # sont du type approprié
    if not isinstance(recognizer, sr.Recognizer):
        raise TypeError("`recognizer` doit être une instance de `Recognizer`")

    if not isinstance(microphone, sr.Microphone):
        raise TypeError("`microphone` doit être une instance de `Microphone`")

    # Ajuster la sensibilité du reconnaisseur au bruit ambiant et enregistrer 
    # l’audio à partir du microphone
    with microphone as source:
        # Cette ligne a été ajoutée pour ajuster le seuil d'énergie basé sur le bruit ambiant.
        # Le paramètre duration détermine combien de secondes de bruit ambiant le reconnaisseur doit analyser.
        # recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

    # Configurer l’objet de réponse
    response = {
        "success": True,
        "error": None,
        "transcription": None
    }

    # Essayer de reconnaître la parole dans l'enregistrement
    # Si une erreur RequestError ou UnknownValueError est capturée,
    # mettre à jour l'objet de réponse en conséquence
    try:
        response["transcription"] = recognizer.recognize_google(audio, language="fr-FR")
    except sr.RequestError:
        # L'API était inaccessible ou sans réponse
        response["success"] = False
        response["error"] = "API indisponible"
    except sr.UnknownValueError:
        # Le mot était incompréhensible
        response["error"] = "Impossible de reconnaître le mot"
        response["success"] = False

    return response


if __name__ == "__main__":
    tello = initialize_tello()
    if tello is not None:
        print ("Drône initialisé!")
    else:
        print("Échec de l'initialisation du drone.")

    # set the list of words, maxnumber of guesses, and prompt limit
    NUM_GUESSES = 9999999
   
    # Créer des instances du reconnaisseur et du microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    
    # Cette ligne a été ajoutée pour configurer le microphone.
    # Le paramètre noise_level détermine le seuil au-dessus duquel le son est considéré 
    # comme un signal plutôt que comme du bruit.
    microphone.dynamic_noise_adjustment = False
    microphone.energy_threshold = 4000

    for i in range(NUM_GUESSES):
        print('Listening ....')
        guess = recognize_speech_from_mic(recognizer, microphone)
        if guess["transcription"]:
            command = guess["transcription"]
            do_action(command)
            # Afficher la transcription de la parole
            print("You said: {}".format(guess["transcription"]))
            
        if not guess["success"]:
            continue

        # S'il y avait une erreur, arrêter la boucle
        if guess["error"]:
            print("ERROR: {}".format(guess["error"]))
