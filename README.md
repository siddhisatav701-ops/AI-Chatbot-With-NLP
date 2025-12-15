# AI-Chatbot-With-NLP
COMPANY: CODTECH IT SOLUTIONS

NAME: SIDDHI TANAJI SATAV

INTERN ID: CTIS0158

DOMAIN: Python Programming

DURATION: 4 WEEEKS

MENTOR: NEELA SANTOSH

Internship Project Submission

CODTECH Internship – Task 3
Title: AI Chatbot with NLP in Python

1. Objective
Build an AI chatbot using Natural Language Processing (NLP) libraries (spaCy) that can understand basic user queries and respond appropriately. The chatbot runs in the terminal and answers questions about the CODTECH tasks as well as simple greetings and help.

2. Tech Stack
Language: Python 3
Libraries:
spacy – NLP processing (tokenization, POS tagging, etc.)
en_core_web_sm – pre‑trained English model for spaCy
Install dependencies:
bash
pip install spacy
python -m spacy download en_core_web_sm

3. Script Overview (chatbot.py)
3.1. NLP Setup
python
import spacy
nlp = spacy.load("en_core_web_sm")
The model converts raw user text into a Doc object with tokens, parts of speech, and other linguistic features used to detect intent.
3.2. Intent Detection
A simple rule‑based function checks the processed text for keywords:
Greeting: hi, hello, hey, good morning, etc.
Goodbye: bye, goodbye, exit, quit.
Thanks: thank you, thanks.
Task‑specific:
Task‑1 / weather API and visualization.
Task‑2 / PDF report generation.
Task‑3 / chatbot itself.
Help: messages containing help.
Unknown: anything that doesn’t match rules.
The function returns an intent label like "greeting", "task1", "help", or "unknown".
3.3. Response GeneratioN
generate_response(user_input):
Processes user text: doc = nlp(user_input).
Calls the intent detector.
Returns a response string based on the intent, for example:
Greeting: introduces the CODTECH chatbot and offers help.
Task‑1: explains the weather dashboard project.
Task‑2: explains the PDF report project.
Task‑3: explains the NLP chatbot project.
Help: lists what the user can ask.
For unknown intent, it extracts nouns from doc using token.pos_ and echoes them back in a clarification message (“You mentioned: … Can you ask about a CODTECH task or say ‘help’?”). This shows a basic use of NLP features beyond simple keyword matching.
3.4. Chat Loop
The main() function creates an interactive console chatbot:
python
print("CODTECH AI Chatbot (Task‑3)")
print("Type 'exit' or 'bye' to quit.\n")
while True:
    user_input = input("You: ")
    if user_input.strip().lower() in ("exit", "quit", "bye", "goodbye"):
        print("Bot: Bye! Good luck with your projects.")
        break
    response = generate_response(user_input)
    print("Bot:", response)
Continuously reads user input.
Stops cleanly when the user types a quit word.
Prints the chatbot’s response each turn.

4. How to Run
Ensure chatbot.py is in your project folder.
Install spaCy and the English model (if not already installed):
bash
pip install spacy
python -m spacy download en_core_web_sm
Run the chatbot from terminal / PowerShell:
bash
python chatbot.py
Example interaction:
text
CODTECH AI Chatbot (Task‑3)
Type 'exit' or 'bye' to quit.
You: hi
Bot: Hello! I am your CODTECH internship chatbot. How can I help you today?
You: what is task 1
Bot: Task‑1: Use Python to fetch data from a public API like OpenWeather and create visualizations using Matplotlib or Seaborn.
You: tell me about task 3
Bot: Task‑3: Build an AI chatbot using NLP (spaCy or NLTK). This console chatbot is one implementation of that requirement.
You: bye
Bot: Bye! Good luck with your projects.
A screenshot of such a session can be used as proof of a working chatbot for your internship.

5. Deliverables
Python Script: chatbot.py – complete chatbot implementation.
Working Demo: console interaction (screenshot or transcript).
Documentation: this README_Task3.md describing setup, logic, and usage.
This satisfies CODTECH Task‑3: building an NLP‑based AI chatbot using Python.

Output
<img width="1068" height="393" alt="image" src="https://github.com/user-attachments/assets/bef11b04-38e1-434b-a208-d9fe1b8bec95" />





