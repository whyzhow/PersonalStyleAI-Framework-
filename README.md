# PersonalStyleAI-Framework-
Let AI think and express like you. This framework provides a complete assembly line: from the noise processing of original chat records, to the seamless switching of multi-model adaptation layers, to local lightweight fine-tuning (LoRA).
## 🧭 Working principle (Workflow)

This project divides the personalisation process of AI into three core stages:

1. **Data Alchemy (Extract)**:

Convert messy chat records (including emojis, links, spam) into high-quality conversation pairs.

2. **Adaptor Centre (Adapt)**:

Through a unified interface, your personal style can be easily loaded to GPT-4, Claude or local Llama 3.

3. **Style Evolution (Evolve)**:

Use fine-tuning technology to solidify your language habits in the weight of the model, not just rely on Prompt.

---

## 📊 Example of data conversion

**Input (original chat.txt):**

> User A: Have you eaten yet?

> I: Eat, [expression] I'm really hungry, https://link.com

> User A: Then let's go.

> Me: Indeed, Let'S Go.

**Output (JSONL after cleaning):**

```Json

{

"Messages": [

{"Role": "user", "content": "Have you eaten yet?"},

{"Role": "assistant", "content": "I'm really hungry after eating"}

]

}
```
## 📂 Project structure

```text

PersonalStyleAI-Framework/

├── data/

│ ├── raw/ # Original chat records (such as chat.txt)

│ └── processed/ # JSONL training data set after cleaning

├── src/ # Source code

│ ├── core/ # adaptor logic and factory mode implementation

│ ├── utils/ # Data preprocessing and string cleaning tools

│ └── trainers/ # Model fine-tuning script (based on PEFT/LoRA)

├── pyproject.toml # Modern Python Dependency and Project Configuration

├── preprocess_data.py # Data processing entry script

├── main.py # Style Dialogue Test Entrance

└── .env.example # Environment variable template
```
## 📂 Detailed description of the project module

1. Core adaptor (src/core/)

Adopt factory model design. This means that if you want to switch from OpenAI to local Ollama, you only need to change the one-line configuration without rewriting the business logic.

2. Cleaning toolbox (src/utils/)

Efficient regular expressions are preset and optimised for text exported by social software.

3. Environmental isolation

Use .env to manage sensitive information and manage dependency hierarchy through pyproject.toml.

## 🚀 Quick installation

1.Basic version (only call API)
```
# Clone Project

Git clone [https://github.com/your username/PersonalStyleAI-Framework.git](https://github.com/your username/Personal StyleAI-Framework.git)

Cd PersonalStyleAI-Framework

# Create a virtual environment and install core dependencies

Python -m venv venv

Source venv/bin/activate # Windows use venv\Scripts\activate

Pip install-e.
```
2. Configure the key

Create a .env file and fill in your API Key:
```
cp .env.example .env
```
3. Build your style

Collect data: Put your chat records or articles into data/raw/chat.txt.
Running cleaning:
```
python preprocess_data.py
```
The script will generate data/processed/train.jsonl, which is a "textbook" for AI to learn your style.
4. Run the dialogue
```
python main.py
```
## 🛠 Advanced: local fine-tuning

If you have a graphics card that supports CUDA, you can install fine-tuning components for local training:
Pip install -e ".[train]"
```
# Run the fine-tuning script (need to configure parameters according to src/trainers)

Python run_train.py
```
## 🤝 Contribution and feedback

If you have any suggestions for improvement or want to add more AI adaptors (such as Anthropic or DeepSeek), welcome to submit a Pull Request or open an Issue discussion.
