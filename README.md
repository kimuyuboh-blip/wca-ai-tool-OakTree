# OakTree Report Summarizer

A Streamlit web application that analyzes and summarizes PDF and Word documents using OpenAI's GPT-4o API. OakTree intelligently chunks large documents to handle token limits and generates concise, actionable summaries.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [Contributors](#contributors)

---

## Features

- **Web Interface**: User-friendly Streamlit interface for document uploads
- **Multi-Format Support**: Accepts PDF and DOCX files
- **Smart Chunking**: Automatically splits large documents to stay within API token limits
- **GPT-4o Integration**: Uses advanced AI for accurate, professional summaries
- **Session Persistence**: Maintains summary results across page interactions
- **Download Capability**: Save summaries as text files
- **Error Handling**: Clear error messages for authentication and rate-limit issues

---

## Prerequisites

Before getting started, ensure you have:

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **OpenAI API Key** - Sign up at [OpenAI Platform](https://platform.openai.com/) to get your API key

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/kimuyuboh-blip/wca-ai-tool-OakTree.git
cd wca-ai-tool-OakTree
```

### 2. Create and Activate Virtual Environment

**On macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**On Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Running the Application

With the virtual environment activated, start the Streamlit app:

```bash
streamlit run oakTree.py
```

**If the above command doesn't work**, try using Python's module invocation:

```bash
python -m streamlit run oakTree.py
```

The app will open in your browser at `http://localhost:8501`

### Usage Steps

1. **Enter API Key**: Paste your OpenAI API key in the sidebar (secure, not stored)
2. **Upload Document**: Upload a PDF or DOCX file
3. **Click Summarize**: Click the "Summarize with OakTree" button
4. **Review Results**: The summary will appear below with options to:
   - View the formatted summary
   - Download as a text file
   - Clear and process another document

### Full Example

```bash
# Activate virtual environment
source venv/bin/activate

# Run the Streamlit app
streamlit run oakTree.py
```

---

## AI Prompt Design

### Overview

OakTree uses a carefully designed two-stage prompt system to ensure high-quality, actionable summaries from complex documents. The prompts are engineered to balance brevity with comprehensiveness.

### Prompt Architecture

#### Stage 1: Chunk Summarization (`SYSTEM_PROMPT_CHUNK`)

```
[Role] Act as a senior business analyst and expert technical writer.

[Context] I am providing a long, detailed document (PDF/report). I need to understand the core message, critical insights, and action items quickly without reading the entire text.

[Task] Read the provided text and create a concise executive summary.

[Constraints]
    - Focus only on the most critical information (highest impact).
    - Do not include filler words or unnecessary background details.
    - Ensure the summary is accurate to the original text.
    - Keep the total length under 300 words.

[Format] Return the output in the following structure:
    Executive Summary: [Insert Document Title]
    - Core Objective/Purpose: [1-2 sentences]
    - Key Insights/Findings: [3-5 concise bullet points]
    - Critical Implications/Recommendations: [2-3 bullet points]
```

**Design Choices:**
- **Role Definition**: Positions the AI as a domain expert (business analyst + technical writer) to encourage professional, structured output
- **Context Framing**: Establishes the user's pain point (time constraints) to create urgency and focus
- **Constraints Section**: Prevents hallucination and verbosity by setting explicit rules
- **Format Structure**: Uses a clear template with bullet points to ensure parsing-friendly, scannable output
- **Word Limit (300 words)**: Balances detail with conciseness for executive audiences

#### Stage 2: Synthesis (`SYSTEM_PROMPT_SYNTHESIS`)

```
Synthesize the following partial summaries into one final bulleted report (max 300 words). Focus only on primary findings and recommended actions.
```

**Design Choices:**
- **Concise Instruction**: For multi-chunk documents, this prompt consolidates multiple summaries without redundancy
- **Focus on Output**: Prioritizes actionable insights over background information
- **Word Limit**: Maintains the same 300-word constraint for consistency

### Why Two-Stage Summarization?

1. **Token Efficiency**: Breaks large documents into manageable chunks (max 12,000 characters per chunk) to avoid OpenAI's token limits
2. **Quality Control**: Processes each section independently to maintain accuracy before synthesis
3. **Scalability**: Handles documents of any length without quality degradation
4. **Cost Optimization**: Reduces unnecessary API calls through intelligent chunking

### Customization

To modify the prompts, edit the `SYSTEM_PROMPT_CHUNK` and `SYSTEM_PROMPT_SYNTHESIS` variables at the top of `oakTree.py`. Key adjustable parameters:
- **Word limit**: Change the "under 300 words" constraint
- **Output format**: Adjust bullet points, sections, or structure
- **Role/Persona**: Customize the analyst role for domain-specific needs
- **Temperature**: Adjust `temperature=0.3` in the API calls (lower = more consistent, higher = more creative)

# Open http://localhost:8501 in your browser
```

---

## Supported File Formats

- **PDF** - Documents with `.pdf` extension
- **DOCX** - Word documents with `.docx` extension

---

## Troubleshooting

### "ModuleNotFoundError"
Ensure your virtual environment is activated and you've run `pip install -r requirements.txt`.

### "Invalid API Key" Error
Double-check that your OpenAI API key is correct and entered properly in the sidebar. Your key is not stored—it's only used for the duration of the session.

### Rate Limit Error
You've sent too many requests to OpenAI. Wait a moment before processing another document.

### Port Already in Use
If port 8501 is already in use, run:
```bash
streamlit run oakTree.py --server.port 8502
```

---

## Contributors

- [Kimuyu Carlos](https://github.com/kimuyuboh-blip)
- [Favour Azu](https://github.com/favour299)
- [Loise Owoko](https://github.com/Loise-Owoko)
- [Eugene Kiprono](https://github.com/euginesky2)
- [Rose Kariuki](https://github.com/wanjirurosek-arch)



---

## Project Structure

```
wca-ai-tool-OakTree/
├── venv/                    # Virtual environment
├── oakTree.py               # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md                # This file explains everything

```
I developed API Integration for Report Summarizer designed to automate the process of extracting key insights from uploaded reports and generating concise summaries using AI. The project involved connecting a frontend upload interface to a backend service that processes PDF and text documents, extracts the content, and sends it to an AI model API such as OpenAI for summarization.
My role included designing the workflow, writing the backend logic, handling file uploads, and integrating the external AI API. I also implemented response handling so the summarized output could be displayed clearly to users.
The code was written in a clean and modular way using Python (Flask/FastAPI). Error handling was added for failed uploads, invalid files, and API rate limits. Security measures like API key protection through environment variables were also included.
The final system allowed users to upload reports and receive fast, readable summaries within seconds, improving productivity and reducing manual reading time. This project strengthened my skills in REST API integration, backend development, prompt engineering, file handling, and AI-powered automation.
