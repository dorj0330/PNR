import speech_recognition as sr

recognizer = sr.Recognizer()

with sr.Microphone() as source:
    print("Adjusting for ambient noise...")
    recognizer.adjust_for_ambient_noise(source)  # Adjust for ambient noise
    print("Listening for your command...")
    audio = recognizer.listen(source)  # Listen to the first available source

print(audio)

# Recognize speech using Google's Speech API
try:
    print("You said: " + recognizer.recognize_google(audio))
except sr.UnknownValueError:
    print("Google Speech Recognition could not understand the audio")
except sr.RequestError as e:
    print(f"Could not request results from Google Speech Recognition service; {e}")