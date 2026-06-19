# POC 3 - AI DevOps Agent

## Overview

This project is an AI-powered DevOps Agent built using FastAPI and OpenAI. The agent follows a multi-step reasoning process where it investigates system issues by calling tools, analyzing results, and providing recommendations.

The project demonstrates how Large Language Models (LLMs) can interact with external tools to solve real-world operational problems.

---

## Features

* AI Agent Loop
* Tool Calling Architecture
* Log Retrieval and Analysis
* Runbook Recommendations
* FastAPI REST API
* OpenAI Integration
* Multi-Step Reasoning

---

## Project Architecture

User Query
↓
AI Agent
↓
Tool Selection
↓
Tool Execution
↓
Tool Result
↓
Reasoning
↓
Final Answer

---

## Available Tools

### 1. fetch_logs(service, window)

Retrieves logs from a log source.

Example:

```python
fetch_logs("checkout", "1h")
```

### 2. analyze_logs()

Analyzes retrieved logs and identifies potential issues.

Example Output:

```text
Payments service causing timeout.
Database latency increased.
```

### 3. lookup_runbook(query)

Provides recommended actions based on detected issues.

Example Output:

```text
Restart payments service.
Check service health.
Monitor API latency.
```

---

## Tech Stack

* Python
* FastAPI
* OpenAI API
* JSON
* Uvicorn

---

## Project Structure

```text
POC3-AI-Agent/
│
├── agent/
│   ├── loop.py
│   └── llm.py
│
├── tools/
│   ├── devops_tools.py
│   └── registry.py
│
├── schemas/
│   └── agent_schema.py
│
├── sample_logs.txt
├── main.py
├── requirements.txt
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone <repository-url>
cd POC3-AI-Agent
```

Create virtual environment:

```bash
python -m venv venv
```

Activate environment:

Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## Environment Variables

Create a `.env` file:

```env
OPENAI_API_KEY=your_api_key_here
```

---

## Running the Application

Start FastAPI server:

```bash
python -m uvicorn main:app --reload
```

Open Swagger UI:

```text
http://127.0.0.1:8000/docs
```

---

## Example Query

Input:

```text
Checkout API is slow
```

Agent Execution:

```text
STEP 1 → fetch_logs
STEP 2 → analyze_logs
STEP 3 → final answer
```

Output:

```text
The checkout API is slow due to payments service timeout and increased database latency.
```

---

## Learning Outcomes

Through this project, I learned:

* AI Agent Architecture
* Tool Calling Workflows
* OpenAI Integration
* FastAPI Development
* Multi-Step Reasoning Systems
* Building Real-World AI Applications

---

## Future Improvements

* Real Log Management Integration
* Database Storage
* OpenAI Function Calling
* Authentication & Security
* Deployment on Cloud Platforms
* Advanced Monitoring Tools

---

## Author

Iram Khaliq

AI Engineering Learning Projects
