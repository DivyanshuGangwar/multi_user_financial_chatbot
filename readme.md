# Multi-User Financial Chatbot

## 📘 Project Overview
**Multi-User Financial Chatbot** is an intelligent chatbot system designed to analyze and interact with company financial documents securely and efficiently.  
The chatbot utilizes advanced LLM (Large Language Model) capabilities to interpret user queries and generate contextual, accurate financial insights based on uploaded or existing company data.

The system ensures **data isolation** by generating **unique user sessions**, preventing any cross-data leakage between different users.

---

## 🧩 Repository Structure

```
multi_user_financial_chatbot/
│
├── aibot.py                # Core class for LLM utilization and prompt creation
├── session_manager.py      # Class for handling multiple user sessions securely
├── /data/                  # Folder containing mock company financial documents
└── main.ipynb              # Colab notebook to execute and demonstrate the chatbot
```

---

## ⚙️ Features

- 💬 **Financial Document Analysis** – Chatbot can read and understand financial reports.
- 🔐 **Session Isolation** – Each user interacts in an isolated environment with no data overlap.
- 🧠 **LLM-Powered Reasoning** – Uses a large language model to process and respond intelligently.
- ⚡ **Multi-User Scalability** – Supports multiple concurrent sessions.
- 🧾 **Mock Data Testing** – Sample financial data for testing and validation provided in `/data`.

---

## 🚀 How to Run

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/multi_user_financial_chatbot.git
cd multi_user_financial_chatbot
```

### 2. Open the Colab Notebook
You can directly open `main.ipynb` in **Google Colab** or **Jupyter Notebook**.

### 3. Run the Cells
Follow the step-by-step instructions inside the notebook to:
- Initialize sessions  
- Load mock financial data  
- Interact with the chatbot  

---

## 🧑‍💻 Author
**Project Maintainer:** [Divyanshu Gangwar]  
**Contact:** [div2015july@gmail.com]

---

## 🪪 License
This project is licensed under the **MIT License** – see the LICENSE file for details.
