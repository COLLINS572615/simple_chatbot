import random
import nltk
from nltk.chat.util import Chat, reflections

#Pairs of input patterns and responses
pairs = [
    [
        r'My name is (.*)',
        ['Hello %1, How can I help you today?',]
    ],
    [
r'What is your name?',
['I am a chatbot. You can call me Bot!']
    ],
    [
r'how are you?',
['I am just a bot. But I am funtioning as expected']
    ],
    [
        r'quit'
        ['Goodbye. Have a good day!']
    ],
]