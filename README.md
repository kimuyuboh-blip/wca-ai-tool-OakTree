# OakTree Report Summarizer

A Streamlit web application that analyzes and summarizes PDF and Word documents using OpenAI's GPT-4o API. OakTree intelligently chunks large documents to handle token limits and generates concise, actionable summaries.

## Table of Contents

- [Features](#features)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)

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

## Project Structure

```
wca-ai-tool-OakTree/
├── venv/                    # Virtual environment
├── oakTree.py               # Main Streamlit application
├── requirements.txt         # Python dependencies
├── README.md                # This file explains everything

```