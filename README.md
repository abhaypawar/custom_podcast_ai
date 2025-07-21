### custom_podcast_ai
This is an AI based Host and Guest Talking platform which follows podcast pattern of discussion. The aim of this tool is to explore the local model vs cloud model. Also, the aim is to understand how the feedback mechanism, here grading system, is taken into consideration and how the local model can be trained/finetunned for future performances.

# 🎙️ Custom Podcast AI

Simulate a podcast-style conversation between two AI personas — a **Host** and a **Guest** — on any topic using a **lightweight local language model** (like TinyLlama). After the simulated discussion, the conversation is **graded** for relevance and coherence, and the output is stored for future fine-tuning.

---

## 📂 Project Structure

```

custom\_podcast\_ai/
├── main.py                 # Entry point: runs the podcast conversation
├── conversation.py         # Logic for model interaction and grading
├── requirements.txt        # Python dependencies
├── history.json            # Stores conversations and grading results
├── models/
│   └── model_name/         # Local model files (TinyLlama, etc.)
└── README.md               # You're reading it

````

---

## ✅ Features

- 🔌 Fully local — no API calls, no internet once the model is downloaded
- 🧠 Two AI agents simulate a natural conversation
- 📊 Automatic grading of conversation quality
- 📝 Saves results to `history.json` for review or later fine-tuning
- 🛠️ Uses Hugging Face `transformers` and `pipeline` APIs

---

## 🖥️ Setup Instructions

### 1. Clone or move to your project directory

```bash
cd ~/local
mkdir -p custom_podcast_ai
cd custom_podcast_ai
````

### 2. Create a virtual environment

```bash
python3 -m venv podcast_ai_venv
source podcast_ai_venv/bin/activate
```

> If you run into errors with `venv`, try installing missing packages:
> `sudo apt install python3.12-venv python3-pip python3-distutils -y`

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Download the lightweight model (TinyLlama)

Create and run a one-time Python script:

```python
# download_model.py
from transformers import AutoTokenizer, AutoModelForCausalLM

model_id = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
AutoTokenizer.from_pretrained(model_id).save_pretrained("models/model_name")
AutoModelForCausalLM.from_pretrained(model_id).save_pretrained("models/model_name")
```

Then run:

```bash
python download_model.py
```

---

## 🚀 Run the Project

```bash
python main.py
```

Sample output:

```
🎙️ Podcast Conversation:

Host: What is the impact of AI on education?
Guest: AI can personalize learning, automate grading, and help teachers with insights...

📊 Conversation Grade: 7/10
```

Saved output will be appended to `history.json`.

---

## 📦 Requirements

Your `requirements.txt`:

```text
transformers==4.41.1
torch==2.3.0
sentencepiece==0.2.0
accelerate==0.31.0
```

---

## 🔄 What's Next?

* LoRA fine-tuning on accumulated feedback
* Streamlit interface for topic selection
* Use better grading models with self-critique
* Enable persona customization per run

---

## 📜 License

MIT License. Use freely and modify for any educational or commercial use.

---

## 👤 Author

Created by **Abhay Pawar**
If you'd like me to auto-fill author info or generate a GitHub-ready repo with `.gitignore` and `LICENSE`, just ask!

```
