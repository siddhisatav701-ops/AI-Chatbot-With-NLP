import spacy

# Load English NLP model
nlp = spacy.load("en_core_web_sm")

# Some simple intent keywords
GREETINGS = ("hi", "hello", "hey", "good morning", "good evening")
GOODBYES = ("bye", "goodbye", "see you", "quit", "exit")
THANKS = ("thank you", "thanks", "thx")

def get_intent(doc):
    """Very simple rule-based intent detector using spaCy tokens."""
    text = doc.text.lower()

    if any(word in text for word in GREETINGS):
        return "greeting"
    if any(word in text for word in GOODBYES):
        return "goodbye"
    if any(word in text for word in THANKS):
        return "thanks"

    if "weather" in text:
        return "weather_info"
    if "task 1" in text or "task-1" in text or "task1" in text:
        return "task1"
    if "task 2" in text or "task-2" in text or "task2" in text:
        return "task2"
    if "task 3" in text or "task-3" in text or "task3" in text or "chatbot" in text:
        return "task3"

    if "help" in text:
        return "help"

    return "unknown"


def generate_response(user_input: str) -> str:
    doc = nlp(user_input)

    intent = get_intent(doc)

    if intent == "greeting":
        return "Hello! I am your CODTECH internship chatbot. How can I help you today?"
    if intent == "goodbye":
        return "Bye! Good luck with your CODTECH internship tasks."
    if intent == "thanks":
        return "You’re welcome! Happy coding."

    if intent == "weather_info":
        return ("In your Task‑1 project, the weather data is fetched from the "
                "OpenWeather API and visualized using Matplotlib and Seaborn.")

    if intent == "task1":
        return ("Task‑1: Use Python to fetch data from a public API like OpenWeather "
                "and create visualizations using Matplotlib or Seaborn, then save "
                "a dashboard image as output.")
    if intent == "task2":
        return ("Task‑2: Read data from a file (for example, CSV), analyze it using "
                "pandas, and generate a formatted PDF report using a library like FPDF.")

    if intent == "task3":
        return ("Task‑3: Build an AI chatbot using NLP (spaCy or NLTK). "
                "This console chatbot is one implementation of that requirement.")

    if intent == "help":
        return ("You can ask me about Task‑1, Task‑2, Task‑3, weather project, PDF report, "
                "or just say hi / bye.")

    # Fallback answer: use simple NLP features to echo key nouns
    nouns = [token.text for token in doc if token.pos_ in ("NOUN", "PROPN")]
    if nouns:
        return ("I am not fully sure about that. You mentioned: "
                + ", ".join(nouns)
                + ". Can you ask about a CODTECH task or say 'help'?")

    return ("Sorry, I didn’t understand that. "
            "Try asking about Task‑1, Task‑2, Task‑3, or type 'help'.")


def main():
    print("CODTECH AI Chatbot (Task‑3)")
    print("Type 'exit' or 'bye' to quit.\n")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() in ("exit", "quit", "bye", "goodbye"):
            print("Bot: Bye! Good luck with your projects.")
            break

        response = generate_response(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    main()
