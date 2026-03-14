from voice_ver import verify_voice
from speech_rec import recognize_speech
from command_exec import exec_command
import os

def main():

    os.chdir("/home/aditya/PycharmProjects/SpeechAI")
    os.system('notify-send "Voice Assistant" "Listening..."')

    authenticated = verify_voice()

    if authenticated:
        os.system('notify-send "Voice Assistant" "Authenticated"')
        text = recognize_speech("command.wav")
        exec_command(text)

    else:
        os.system('notify-send "Voice Assistant" "Authentication Failed"')

if __name__ == "__main__":
    main()