from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline
import torch
import os

MODEL_PATH = os.path.join(os.path.dirname(__file__), "..", "models", "model_name")

tokenizer = AutoTokenizer.from_pretrained(MODEL_PATH)
model = AutoModelForCausalLM.from_pretrained(
    MODEL_PATH,
    torch_dtype=torch.float16 if torch.cuda.is_available() else torch.float32,
    device_map="auto"
)

generator = pipeline("text-generation", model=model, tokenizer=tokenizer, max_new_tokens=120)

def generate_response(prompt: str) -> str:
    result = generator(prompt, do_sample=True, temperature=0.7, top_p=0.95)[0]["generated_text"]
    return result[len(prompt):].strip()

def run_podcast_conversation(topic: str, num_turns=6):
    intro = f"Topic: {topic}\nLet's listen to a conversation between a curious Host and an expert Guest."
    history = [intro]

    for i in range(num_turns):
        speaker = "Host" if i % 2 == 0 else "Guest"
        prompt = "\n".join(history[-2:]) + f"\n{speaker}:"
        response = generate_response(prompt)
        history.append(f"{speaker}: {response.strip()}")
    
    return history[1:]

def grade_conversation(conversation, topic):
    topic_words = set(topic.lower().split())
    relevant_turns = 0
    for turn in conversation:
        turn_text = turn.split(":")[1].strip().lower()
        if any(word in turn_text for word in topic_words):
            relevant_turns += 1
    return min(10, round((relevant_turns / len(conversation)) * 10))

