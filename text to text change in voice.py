# Python program to show
# how to convert text to speech
import pyttsx3

# Initialize the converter
voice_handler = pyttsx3.init()
voices = voice_handler.getProperty('voices')
voice_handler.setProperty('voice',voices[0].id)

# Set properties before adding
# Things to say...

# Sets speed percent
# Can be more than 100
voice_handler.setProperty('rate', 200)
# Set volume 0-1
voice_handler.setProperty('volume', 14)

# Queue the entered text
# There will be a pause between
# each one like a pause in
# a sentence
voice_handler.say("About india")
voice_handler.say("India, country that occupies the greater part of South Asia. Its capital is New Delhi, built in the 20th century just south of the historic hub of Old Delhi to serve as India’s administrative centre. Its government is a constitutional republic that represents a highly diverse population consisting of thousands of ethnic groups and likely hundreds of languages. With roughly one-sixth of the world’s total population, India is the second most populous country, after China.")

# Empties the say() queue
# Program will not continue
# until all speech is done talking
voice_handler.runAndWait()
