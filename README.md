# 🚀 AI Resume & Job Application Agent

An intelligent, stateful AI-powered job application automation agent built using **LangGraph + LLMs + Tavily Search**.

This system evaluates a resume against a target job role, provides structured recruiter-style feedback, suggests improvements, fetches relevant job links and courses, and is being extended to automate recruiter outreach and application tracking.

---

## 🔎 Overview

This project is designed to simulate how a real technical recruiter evaluates a candidate profile.

The agent:

- Extracts and structures resume content from a PDF
- Evaluates alignment with a job role using LLM-based reasoning
- Applies deterministic scoring logic for missing required fields
- Routes execution dynamically based on evaluation score
- Fetches live job opportunities and relevant learning resources

It combines deterministic validation with LLM reasoning to produce structured and actionable output.

---

## 🧠 System Workflow
<img width="310" height="630" alt="output" src="https://github.com/user-attachments/assets/55697e6c-7a75-4ba2-a3a4-657255c0c51a" />


### Flow Logic

- If overall quality score < threshold → Suggest resume improvements + reference resumes
- If overall quality score ≥ threshold → Fetch relevant job links
- Both branches converge to recommended course suggestions

The system is built using stateful orchestration with LangGraph.

---

## 🛠 Tech Stack

- Python
- LangGraph (stateful orchestration)
- LangChain
- Google Gemini (gemini-2.5-flash)
- Tavily Search API
- Pydantic
- PDF document loader
- Deterministic scoring engine

---

## 📊 Features

### Resume Processing
- PDF text extraction
- Section segmentation (Summary, Skills, Experience, Projects, etc.)
- Missing field detection (GitHub, LinkedIn, Email, LeetCode)

### AI Evaluation
- Resume-to-role alignment scoring
- Recruiter-style feedback
- Structured improvement suggestions
- Quality classification (Poor / Average / Good / Excellent)

### Smart Routing
- Conditional workflow based on score
- Resume reference suggestions for weak profiles
- Live fresher job link discovery for strong profiles
- Course recommendations

--

## 🚧 Upcoming Enhancements

### Automated Recruiter Outreach
If:
- Resume quality score is high
- Job description alignment is strong

The agent will:
- Send structured recruiter email
- Send direct LinkedIn message
- Log the application in an Excel tracker
- Create a directory per job role for tracking

### UI Dashboard
- Resume score visualization
- Feedback panel
- Job tracking interface
- Application status manager

