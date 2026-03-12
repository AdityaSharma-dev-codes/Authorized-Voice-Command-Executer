# Authorized Voice Command Executer

## Project Overview
The goal of this project is to develop a personal voice authentication system that allows only the registered user to execute commands on a computer system. The system provides a lightweight, offline biometric security mechanism by integrating voice recognition with system command execution.

## Features
- **Speaker Verification:** Identify if the speaker matches a registered voice profile.
- **Voice Profile Creation:** Generate unique voice embeddings from recorded samples.
- **Similarity Scoring:** Uses cosine similarity to compare voice embeddings.
- **Offline Processing:** Designed to run locally with minimal dependencies.
- **Transcription (Upcoming):** Integrated Whisper model for transcribing voice commands.

## Installation

### Prerequisites
- Python 3.8+
- [PortAudio](http://www.portaudio.com/) (required for `sounddevice`)

### Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/authorized-voice-command-executor.git
   cd Authorized-Voice-Command-Executer
   ```

2. Install the required dependencies:
   ```bash
   pip install numpy resemblyzer sounddevice scipy openai-whisper
   ```

3. Create the necessary directories:
   ```bash
   mkdir Samples Voice_Profiles Test_voices
   ```

## Usage

### 1. Record Voice Samples
Run `voice_rec.py` to collect audio samples of your voice. Rename the saved file after each recording to avoid overwriting (e.g., `Samples/sample_1.wav`, `Samples/sample_2.wav`).
```bash
python voice_rec.py
```

### 2. Generate Voice Profile
After collecting several samples in the `Samples/` directory, run `voice_auth.py` to create your biometric voice profile (`Voice_Profiles/Voice_Profile.npy`).
```bash
python voice_auth.py
```

### 3. Verify Identity
To test the authentication, run `voice_ver.py`. It will record 5 seconds of audio and compare it against your stored profile.
```bash
python voice_ver.py
```

### 4. Speech Recognition and Command Execution(Experimental)
Transcribe voice commands using OpenAI's Whisper `small` model and execute system commands.
1. Run `speech_rec.py` to record and transcribe audio:
```bash
python speech_rec.py
```
2. Run `command_exec.py` to execute the transcribed command:
```bash
python command_exec.py
```
Currently supported commands (searched in transcription):
- **"browser"**: Opens the Firefox web browser.
- **"terminal"**: Opens the `gnome-terminal`.
- **"close"**: Kills the currently focused window using `xdotool`.
- **"shutdown"**: Initiates a system shutdown.
- **"restart"** or **"reboot"**: Reboots the system.

## Project Structure
- `voice_rec.py`: Records voice samples for training.
- `voice_auth.py`: Generates a voice profile from the collected samples.
- `voice_ver.py`: Performs live voice authentication.
- `speech_rec.py`: Transcribes audio and saves it to `commands.txt` using Whisper.
- `command_exec.py`: Reads `commands.txt` and executes corresponding system commands.
- `commands.txt`: Stores the transcription of the latest voice command.
- `Samples/`: Directory for storing training voice samples.
- `Voice_Profiles/`: Directory for storing the generated `.npy` profile.
- `Test_voices/`: Directory for storing temporary recordings for verification.

## Future Goals
- Implement continuous authentication.
- Map authenticated voice commands to system actions.
- Improve security with anti-spoofing techniques.