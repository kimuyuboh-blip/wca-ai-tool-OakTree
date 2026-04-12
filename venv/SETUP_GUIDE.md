# Report Summarizer - Setup Guide

## Overview
This tool summarizes long documents or reports using OpenAI's API, returning clean executive summaries in bullet points.

## Prerequisites
- Python 3.8 or higher
- OpenAI API key (get it from https://platform.openai.com/api-keys)

## Installation

### 1. Install Required Packages
```bash
pip install -r requirements.txt
```

### 2. Set Up API Key

#### Option A: Environment Variable (Recommended)
Create a `.env` file in the project directory:
```
OPENAI_API_KEY=your_api_key_here
```

Or set it directly in your terminal:
```bash
export OPENAI_API_KEY=your_api_key_here
```

#### Option B: Pass API Key Directly
```python
summarizer = ReportSummarizer(api_key="your_api_key_here")
```

## Usage

### Demo Mode (Default)
```bash
python report_summarizer.py
```
This runs with a sample financial report to demonstrate functionality.

### Interactive Mode
```bash
python report_summarizer.py --interactive
```
This allows you to:
- Summarize documents from files (.txt, .pdf, .docx)
- Summarize text pasted directly
- Run multiple summaries in one session

### Using in Your Code

#### From a File
```python
from report_summarizer import ReportSummarizer

summarizer = ReportSummarizer()
summary = summarizer.summarize_from_file("path/to/document.txt", max_bullets=8)
print(summary)
```

#### From Text Input
```python
from report_summarizer import ReportSummarizer

summarizer = ReportSummarizer()
text = "Your long report text here..."
summary = summarizer.summarize_from_text(text, max_bullets=8)
print(summary)
```

## Features

✅ **Multiple Input Formats**
- Plain text (.txt)
- PDF documents (.pdf)
- Word documents (.docx)
- Direct text input

✅ **Customizable Summaries**
- Control number of bullet points (default: 8)
- Adjustable output length
- Configurable AI model

✅ **Robust Error Handling**
- File validation
- API error handling
- Clear error messages

✅ **Well-Documented Code**
- Comprehensive comments
- Type hints
- Docstrings for all functions

## Parameters

### ReportSummarizer Constructor
- `api_key` (str, optional): OpenAI API key
- `model` (str): AI model to use (default: "gpt-3.5-turbo")

### Summarize Methods
- `max_bullets` (int): Number of bullet points (default: 8)

## Supported Models

- `gpt-3.5-turbo` (fast, cost-effective) - **Default**
- `gpt-4` (more accurate, higher cost)
- `gpt-4-turbo-preview` (balanced)

## Pricing Estimate

With GPT-3.5-turbo:
- ~1,000 summaries per $1 USD
- Input: $0.0005 per 1K tokens
- Output: $0.0015 per 1K tokens

## Troubleshooting

### "API key not provided"
- Check that OPENAI_API_KEY environment variable is set
- Or pass `api_key` parameter to constructor

### "No module named 'openai'"
```bash
pip install openai
```

### PDF/DOCX File Errors
```bash
# For PDF support
pip install pypdf

# For DOCX support
pip install python-docx
```

### Rate Limiting
If you hit rate limits:
- Add delays between requests: `time.sleep(1)`
- Use a lower-cost model
- Implement exponential backoff

## Example Output

```
📋 EXECUTIVE SUMMARY
═══════════════════════════════════════════════════════════════════════════

1. Quarterly revenue increased 12% YoY to $4.2B, with exceptional Asian growth but European headwinds.
2. Launched three new enterprise solutions and expanded into two new markets this quarter.
3. Successfully improved customer retention by 15% through enhanced product offerings.
4. Operational costs rose due to supply chain disruptions and increased raw material expenses.
5. Asian markets performed exceptionally with 24% growth, driven by new product launches.
```

## License
MIT

## Support
For issues or questions, refer to the inline comments in the script or the docstrings.
