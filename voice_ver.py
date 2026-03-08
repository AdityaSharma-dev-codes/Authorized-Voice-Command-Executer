import sounddevice as sd
from scipy.io.wavfile import write
import numpy as np
from resemblyzer import VoiceEncoder, preprocess_wav
from numpy.linalg import norm

SAMPLE_RATE = 16000
DURATION = 5
THRESHOLD = 0.75 # authentication threshold

def cosine_similarity(a, b):
    return np.dot(a, b) / (norm(a) * norm(b))

# Record live audio
print("Speak now for authentication...")

audio = sd.rec( int(DURATION * SAMPLE_RATE), samplerate=SAMPLE_RATE, channels=1, dtype="float32" )
sd.wait()
write("Test_voices/test_1.wav", SAMPLE_RATE, audio)

# Check for silence or low audio energy
audio_energy = np.sqrt(np.mean(audio**2))

if audio_energy < 0.0001: # Threshold for silence
    print("Similarity Score: 0.000")
    print("ACCESS DENIED — No voice detected (Silence)")
else:
    print("Processing voice...")
    
    encoder = VoiceEncoder()
    
    wav = preprocess_wav("Test_voices/test_1.wav")
    current_embedding = encoder.embed_utterance(wav)
    
    # Load stored voice profile
    voice_profile = np.load("Voice_Profiles/Voice_Profile.npy")
    
    # Compare voices
    similarity = cosine_similarity(current_embedding, voice_profile)
    print(f"Similarity Score: {similarity:.3f}")

    if similarity > THRESHOLD:
        print("AUTHENTICATED — Voice Match")
    else:
        print("ACCESS DENIED — Voice Mismatch")