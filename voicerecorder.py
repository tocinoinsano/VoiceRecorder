import sounddevice
from scipy.io.wavfile import write

fs = 44100  # sample rate
seconds = 10 # duration of recording
print("recording..")

recording = sounddevice.rec(int(seconds * fs), samplerate = fs, channels = 1)

sounddevice.wait() # wait for recording to finish

print("donee...")

write("output.wav", fs, recording) # save file as wav file