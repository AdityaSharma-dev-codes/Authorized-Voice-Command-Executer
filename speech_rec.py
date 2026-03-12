import whisper
import sounddevice as sd
from scipy.io.wavfile import write

model = whisper.load_model("small")


samplerate = 16000 # Quality
time = 5 # Seconds

def rec_audio(filename ,sample_rate, duration):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(sample_rate * duration), samplerate = sample_rate, channels = 1, dtype = "float32")
    sd.wait()
    print("Recording Complete")
    write(filename, sample_rate, audio)

rec_audio("Test_voices/live_test.wav", samplerate, time)

result = model.transcribe("Test_voices/live_test.wav",
                          language = "en",
                          fp16 = False
)

text = result["text"].strip().lower()
with open('commands.txt', 'w') as f:
    f.write(text)