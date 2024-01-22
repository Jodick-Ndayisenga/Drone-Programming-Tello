# Tello Drone Voice Control

This project allows you to control a Tello drone using voice commands. The code integrates the DJITelloPy library for drone control and the SpeechRecognition library for voice recognition. With this setup, you can give commands to the Tello drone using your voice.

### Requirements

    Python 3.x
    Install required libraries using the following:

```python
    pip install djitellopy
    pip install SpeechRecognition
```

## How to Use

    Connect your computer to the Tello drone's Wi-Fi.
    Run the script, and the Tello drone will be initialized.
    The program will continuously listen for voice commands.

## Voice Commands

### The following voice commands are supported:

    Takeoff: Say any of the following to initiate takeoff: "d'école", "décolle", "démarre", "déconne", "école".
    Land: Say any of the following to initiate landing: "atterrit", "atterrir", "stop".
    Move Forward: Use commands like "avance" or "avant" to move the drone forward.
    Move Backward: Commands like "récule" or "arrière" will make the drone move backward.
    Move Left: The drone will move left with commands like "gauche".
    Move Right: The drone will move right with commands like "droite".
    Flip Forward: Commands like "tourne", "roule", "rôle", or "flip" will make the drone flip forward.
    Flip Left: Say "flip gauche" to make the drone flip to the left.
    Flip Back: Use "flip arrière" to make the drone flip backward.
    Flip Right: Say "flip droit" to make the drone flip to the right.

Feel free to experiment with the voice commands and customize them as needed.
Important Note

Ensure that your microphone is properly configured and connected. Adjust the noise level threshold if needed. The program will continuously listen for voice commands until manually stopped.

Note: This code assumes that the Tello drone is connected to the computer running the script through Wi-Fi. Adjust the Wi-Fi connection settings accordingly. Additionally, ensure that the Tello drone is in a suitable environment for safe flight.
