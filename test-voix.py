import speech_recognition as sr


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
        # Cette ligne a été ajoutée pour ajuster le reconnaisseur au bruit ambiant.
        # Le paramètre duration détermine combien de secondes de bruit ambiant le reconnaisseur doit analyser.
        recognizer.adjust_for_ambient_noise(source, duration=1)
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
        response["transcription"] = recognizer.recognize_google(
            audio, language="fr-FR")
    except sr.RequestError:
        # L'API était inaccessible ou sans réponse
        response["success"] = False
        response["error"] = "API indisponible"
    except sr.UnknownValueError:
        # La parole était incompréhensible
        response["error"] = "Impossible de reconnaître le mot"
        response["success"] = False

    return response


if __name__ == "__main__":
    # Créer des instances du reconnaisseur et du microphone
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    # Le paramètre noise_level détermine le seuil au-dessus duquel le son est considéré
    # comme un signal plutôt que comme du bruit.
    # microphone.dynamic_noise_adjustment = False
    # microphone.energy_threshold = 4000

    for i in range(55):  # Vous pouvez ajuster le nombre de tentatives d'enregistrement ici
        print('Listening ....')
        guess = recognize_speech_from_mic(recognizer, microphone)
        print(guess)
        if guess["transcription"]:
            # Afficher la transcription de la parole
            print("You said: {}".format(guess["transcription"]))

        if not guess["success"]:
            continue

        # S'il y avait une erreur, arrêter la boucle
        if guess["error"]:
            print("ERREUR : {}".format(guess["error"]))
            break
