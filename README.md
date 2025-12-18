# 🚀 Agentic IDE – Production-Grade LLM Code Generator

## 📌 Overview

This project is a **production-grade Agentic IDE backend** that converts **natural language instructions into real project files** (HTML, CSS, backend code, etc.) using **agent-based orchestration**.

Unlike prompt-based demos, this system is designed with **real-world LLM behavior** in mind — including output truncation, reliability issues, and scalability concerns.

The core idea is simple but powerful:

> **Design the system around LLM limitations, not against them.**

This repository demonstrates how modern **AI-powered developer tools** can be built using **agentic architecture**.

---

## 🧠 Why Agentic IDE?

Most AI code generators fail in production because they:

* Generate multiple large files in a single response
* Rely on fragile JSON parsing
* Break due to token limits or truncated outputs
* Are tightly coupled to a single LLM provider

This Agentic IDE solves those issues using:

* **Planner → Executor agent design**
* **One-file-per-LLM-call strategy**
* **LLM-agnostic architecture**
* **FastAPI-based orchestration layer**

This approach mirrors how real-world tools like modern AI IDEs and autonomous coding agents are architected.

---

## 🏗️ Architecture

### 🔹 High-Level Flow

```
User Instruction
      ↓
Planner Agent (decides required files)
      ↓
Executor Agent (generates one file per call)
      ↓
File Writer (creates folders & writes files)
```

### 🔹 Key Design Decision

> **Never ask an LLM to generate multiple long files in a single response.**

Each file is generated independently, which:

* Prevents truncation
* Improves reliability
* Scales to large projects
* Makes retries safe and cheap

---

## 🤖 Agent Responsibilities

### 1️⃣ Planner Agent

* Analyzes the user instruction
* Determines required project files
* Returns a **small, safe JSON response**

Example:

```json
{
  "files": [
    "frontend/index.html",
    "frontend/style.css"
  ]
}
```

---

### 2️⃣ Executor Agent

* Generates **only one file at a time**
* Outputs **raw file content** (no JSON, no markdown)
* Prevents partial or broken outputs

---

### 3️⃣ File Writer

* Creates directories automatically
* Writes files atomically to disk
* Ensures safe persistence of generated code

---

## ⚙️ Tech Stack

* **Python**
* **FastAPI** – API orchestration layer
* **Agentic AI Architecture**
* **LLM APIs** (pluggable)
* **Ollama** (local LLM support)

---

## 🔌 LLM-Agnostic Design

This system is intentionally built to work with **any LLM provider**, including:

* Google Gemini
* OpenAI APIs
* Groq
* Local models via **Ollama**

Switching LLMs requires minimal changes and **no architectural refactor**, ensuring:

* Vendor independence
* Future-proof design
* Easy experimentation

---

## 🌐 FastAPI Backend

The entire agent system is exposed through a **FastAPI backend**, making it easy to:

* Integrate with a frontend IDE UI
* Build a CLI tool
* Connect external developer tools

### Example Endpoint

```
POST /generate
```

**Request Body:**

```json
{
  "instruction": "Create a modern login page using HTML and CSS"
}
```

**Behavior:**

* Planner agent decides file structure
* Executor agent generates files
* Files are written to disk

---

## 📁 Project Structure

```
backend/
├── agents/
│   └── frontend_agent.py   # Planner + Executor logic
├── llm/
│   └── gemini.py           # LLM adapter (swappable)
├── main.py                 # FastAPI entry point

frontend/                   # Generated output (gitignored)
```

---

## 🧪 Reliability & Production Considerations

This project explicitly handles:

* ❌ Long JSON responses (avoided by design)
* ❌ LLM output truncation
* ❌ Broken multi-file generations
* ❌ Vendor lock-in

Instead, it uses:

* Small JSON planning steps
* Deterministic file generation
* Stateless execution per file
* Clear separation of concerns

---

## 🚀 How to Run Locally

### 1️⃣ Clone the repository

```bash
git clone <your-repo-url>
cd agentic-ide
```

### 2️⃣ Create & activate virtual environment

```bash
python -m venv myenv
myenv\Scripts\activate   # Windows
```

### 3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Set API Key

```bash
setx GEMINI_API_KEY "YOUR_API_KEY"
```

### 5️⃣ Run FastAPI server

```bash
uvicorn backend.main:app --reload --port 8000
```

---

## 📈 Future Enhancements

* Multi-agent review & validation
* Diff-based regeneration
* Streaming file generation
* Frontend IDE UI
* LangGraph-based orchestration
* Persistent project memory

---

## 🎯 Key Takeaway

This project is not about prompting an LLM.

It’s about **engineering reliable GenAI systems** that work under real-world constraints.

If you’re interested in **Agentic AI, GenAI engineering, or AI-powered developer tools**, this project demonstrates a **production-ready mindset**.

---

## 🤝 Feedback & Contributions

Feedback, ideas, and discussions are always welcome.

Let’s build better **agent-driven AI systems** 🚀
