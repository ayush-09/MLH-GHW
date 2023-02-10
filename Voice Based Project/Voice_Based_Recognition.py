# -*- coding: utf-8 -*-
"""
Created on Fri Feb 10 19:28:09 2023

@author: ayush
"""

import speech_recognition as sr
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

# Initialize the recognizer class (for recognizing the speech)
r = sr.Recognizer()

# Function to convert text to speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to recognize speech
def get_audio():
    with sr.Microphone() as source:
        audio = r.listen(source)
        said = ""
        
        try:
            said = r.recognize_google(audio)
        except Exception as e:
            print("Exception:", str(e))
        
    return said.lower()

# Initialize a list to store the user's tasks
tasks = []

# Main loop
while True:
    print("Listening...")
    text = get_audio()
    
    if "add task" in text:
        task = text.replace("add task", "").strip()
        tasks.append(task)
        speak(f"Task added: {task}")
        
    elif "show pending tasks" in text:
        if not tasks:
            speak("No pending tasks.")
        else:
            speak("Your pending tasks are:")
            for task in tasks:
                print(task)
                speak(task)
                
    elif "mark task as complete" in text:
        task = text.replace("mark task as complete", "").strip()
        if task in tasks:
            tasks.remove(task)
            speak(f"Task marked as complete: {task}")
        else:
            speak(f"Task not found: {task}")
