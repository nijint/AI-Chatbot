
# 🤖 AI Chatbot — Desktop Interface

A modular **Python-based AI chatbot** built with **CustomTkinter** that integrates Google’s Gemini Generative AI API into a lightweight desktop application.
Designed for experimentation, academic prototyping, and rapid UI-driven AI workflows.

---

## 🚀 Overview

This project demonstrates a structured implementation of a **local GUI chatbot client** capable of interacting with cloud-based LLM services through secure environment configuration.
The architecture separates UI logic from model communication, enabling extensibility and maintainability.

---

## ✨ Core Features

* 🧠 **Gemini AI Integration** — Direct interaction using `google-generativeai`
* 🖥️ **Modern Desktop UI** — Built with `CustomTkinter`
* 🔐 **Environment Variable Security** — `.env` based API key handling
* ⚡ **Modular Design** — Decoupled UI and chatbot logic
* 📦 **Virtual Environment Ready** — Clean dependency isolation
* 🧩 **Extensible Structure** — Easy integration of additional AI tools or APIs

---

## 🏗️ Project Architecture

```
ai-chatbot/
│
├── ui.py                # CustomTkinter user interface
├── gemini_chatbot.py    # Gemini API interaction layer
├── .env                 # Environment variables (not tracked)
├── requirements.txt     # Dependency list
└── venv/                # Local virtual environment (ignored)
```

---

## ⚙️ Technology Stack

| Layer                 | Technology        |
| --------------------- | ----------------- |
| Language              | Python 3          |
| UI Framework          | CustomTkinter     |
| AI Backend            | Google Gemini API |
| Config Management     | python-dotenv     |
| Environment Isolation | venv              |

---

## 🧪 Installation

Clone the repository:

```bash
git clone https://github.com/nijint/ai-chatbot.git
cd ai-chatbot
```

Create virtual environment:

```bash
python -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## 🔑 Environment Setup

Create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

---

## ▶️ Running the Application

```bash
python ui.py
```

Or use the run script:

```bash
./run.sh
```

---

## 📐 Design Goals

* Maintain clear separation between presentation and AI layers
* Ensure reproducible environments through dependency locking
* Provide an entry-level experimentation platform for desktop AI tooling


---

## 📊 Potential Use Cases

* Academic AI experimentation
* Rapid chatbot prototyping
* Desktop AI interface development
* Learning resource for GUI + API integration

---

## 📌 Future Enhancements

* Streaming response rendering
* Chat history persistence
* Plugin-based AI provider abstraction
* Voice input integration

---

## 👨‍💻 Author
@nijint  

(Developed as part of a learning-focused AI experimentation workflow)

