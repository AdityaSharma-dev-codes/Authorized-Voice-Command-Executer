from resemblyzer import VoiceEncoder, preprocess_wav
import glob
import numpy as np
import os
print("Current directory:", os.getcwd())

embeddings = []
files = glob.glob("sample_*.wav")
print("Found Files: ", files)
encoder = VoiceEncoder()

print("Processing...")

for f in files:
    wav = preprocess_wav(f)
    embed = encoder.embed_utterance(wav)
    embeddings.append(embed)

print(embeddings)

voice_profile = np.mean(embeddings, 0)
np.save("Voice_Profile.npy", voice_profile)
print("Voice profile created")
