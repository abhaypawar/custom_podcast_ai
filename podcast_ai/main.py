import json
from pathlib import Path
from utils.conversation import run_podcast_conversation, grade_conversation

TOPIC = input("Enter the topic: ") # Prompt the user to enter a topic
print(f"The topic is: {TOPIC}")

FEEDBACK_FILE = Path("feedback/history.json")

def save_feedback(topic, conversation, grade):
    FEEDBACK_FILE.parent.mkdir(parents=True, exist_ok=True)
    history = []
    if FEEDBACK_FILE.exists():
        history = json.loads(FEEDBACK_FILE.read_text())
    history.append({
        "topic": topic,
        "conversation": conversation,
        "grade": grade
    })
    FEEDBACK_FILE.write_text(json.dumps(history, indent=2))

def main():
    conversation = run_podcast_conversation(TOPIC)
    print("\n🎙️ Podcast Conversation:\n")
    for i, turn in enumerate(conversation):
        print(turn)

    grade = grade_conversation(conversation, TOPIC)
    print(f"\n📊 Conversation Grade: {grade}/10")
    save_feedback(TOPIC, conversation, grade)

if __name__ == "__main__":
    main()

