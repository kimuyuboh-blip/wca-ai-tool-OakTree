# WCA AI Tool

An AI-powered document processing tool that processes PDF and Word documents using OpenAI's API to generate intelligent summaries and analysis.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [Running the Script](#running-the-script)
- [Configuration](#configuration)
- [Project Structure](#project-structure)

---

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- **Python 3.7 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** - [Download Git](https://git-scm.com/downloads)
- **OpenAI API Key** - Sign up at [OpenAI Platform](https://platform.openai.com/) to get your API key

---

## Setup Instructions

### 1. Clone the Repository

First, clone this repository to your local machine:

```bash
git clone https://github.com/kimuyuboh-blip/wca-ai-tool-OakTree.git
cd wca-ai-tool-OakTree
```

### 2. Create a Virtual Environment

A virtual environment isolates your project dependencies from other Python projects on your system. Create one using:

```bash
python3 -m venv venv
```

This creates a new folder called `venv` in your project directory.

### 3. Activate the Virtual Environment

Activate the virtual environment for your operating system:

**On macOS/Linux:**
```bash
source venv/bin/activate
```

**On Windows:**
```bash
venv\Scripts\activate
```

You'll know it's activated when you see `(venv)` at the beginning of your terminal prompt.

### 4. Install Dependencies

With the virtual environment activated, install all required packages from `requirements.txt`:

```bash
pip install -r requirements.txt
```

This installs all necessary dependencies including:
- OpenAI SDK for API calls
- PDF and document processing libraries
- Environment variable management (.env support)

### 5. Configure Environment Variables

Create a `.env` file in the project root directory with your OpenAI API key:

```bash
echo "OPENAI_API_KEY=your-api-key-here" > .env
```

Or manually create a `.env` file and add:

```
OPENAI_API_KEY=your-api-key-here
```

**Security Note:** The `.env` file is listed in `.gitignore` and is never committed to Git, keeping your API key safe.

---

## Running the Script

Once setup is complete, run the main script:

```bash
python3 report_summarizer.py
```

Or with your virtual environment activated:

```bash
(venv) python3 report_summarizer.py
```

The script will process your documents and generate the output.

---

## Configuration

### Environment Variables

The script uses environment variables stored in the `.env` file. These are automatically loaded by the `python-dotenv` package.

**Required:**
- `OPENAI_API_KEY` - Your OpenAI API key for authentication

You can add additional configuration variables to the `.env` file as needed.

### .gitignore Explanation

The `.gitignore` file prevents certain files from being committed to Git. This protects sensitive data:

```
.env                 # Keeps your API key secure
__pycache__/         # Python cache files (system-generated)
*.pyc                # Compiled Python files
venv/                # Virtual environment (not needed in git)
.vscode/             # VS Code settings (optional)
*.egg-info/          # Egg metadata files
dist/ & build/       # Distribution artifacts
```

---

## Project Structure

```
wca-ai-tool-OakTree/
├── venv/                    # Virtual environment (ignored in git)
├── .env                     # Environment variables (ignored in git)
├── .gitignore               # Git ignore rules
├── README.md                # This file
├── requirements.txt         # Python dependencies
└── report_summarizer.py     # Main script that processes documents
```

---

## Troubleshooting

### "Command not found: python3"
Make sure Python is installed and added to your PATH. Check with `python --version`.

### "ModuleNotFoundError"
Ensure your virtual environment is activated and you've run `pip install -r requirements.txt`.

### "API Key not found"
Verify that your `.env` file exists in the project root and contains your `OPENAI_API_KEY`.

### Permission denied on venv/bin/activate
On macOS/Linux, you may need to make the script executable:
```bash
chmod +x venv/bin/activate
```

---

## Deactivating the Virtual Environment

When finished working on the project, deactivate the virtual environment:

```bash
deactivate
```

Your terminal prompt will return to normal.