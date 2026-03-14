from voice_ver import verify_voice
from speech_rec import recognize_speech
from command_exec import exec_command

def main():
    authenticated = verify_voice()

    if authenticated:
        text = recognize_speech("command.wav")
        print("command: ", text)
        exec_command(text)

    else:
        print("User not authorized")

if __name__ == "__main__":
    main()