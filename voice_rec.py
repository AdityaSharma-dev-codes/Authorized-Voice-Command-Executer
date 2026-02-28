import sounddevice as sd
from scipy.io.wavfile import write
samplerate = 16000 # Quality
time = 5 # Seconds

def rec_audio(filename ,sample_rate, duration):
    print(f"Recording for {duration} seconds...")
    audio = sd.rec(int(sample_rate * duration), samplerate = sample_rate, channels = 1, dtype = "float32")
    sd.wait()
    print("Recording Complete")
    write(filename, sample_rate, audio)

rec_audio("sample_1", samplerate, time) #Change filename for each sample Collected