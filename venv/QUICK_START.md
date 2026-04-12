# Quick Start Guide - Report Summarizer

## 🚀 5-Minute Setup

### Step 1: Copy Environment Template
```bash
cp .env.example .env
```

### Step 2: Add Your API Key
Edit `.env` and replace `your_api_key_here` with your OpenAI API key:
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
```

Get your key: https://platform.openai.com/api-keys

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Run Demo
```bash
python report_summarizer.py
```

You should see a sample financial report being summarized!

---

## 💡 Common Usage Patterns

### Pattern 1: Quick Summary in Python
```python
from report_summarizer import ReportSummarizer

summarizer = ReportSummarizer()
text = "Your long document here..."
summary = summarizer.summarize_from_text(text)
print(summary)
```

### Pattern 2: From a File
```python
summarizer = ReportSummarizer()
summary = summarizer.summarize_from_file("report.pdf")
print(summary)
```

### Pattern 3: Interactive Mode
```bash
python report_summarizer.py --interactive
```
Then follow the prompts to:
- Upload a file (.txt, .pdf, .docx)
- Or paste text directly

### Pattern 4: Jupyter Notebook
```python
from report_summarizer import ReportSummarizer

# Initialize once
summarizer = ReportSummarizer()

# Summarize multiple reports
for report_file in ['report1.txt', 'report2.pdf', 'report3.docx']:
    summary = summarizer.summarize_from_file(report_file)
    print(f"\n{report_file}:\n{summary}")
```

---

## 📊 Output Format

Executive summaries are returned as numbered bullet points:

```
1. Revenue grew 12% YoY, with strong performance across all regions.
2. Operating costs increased 8% due to supply chain challenges.
3. Customer satisfaction improved to 94%, up from 91% last quarter.
4. New product line contributed 15% of total revenue.
5. Market expansion into three new territories under way.
```

---

## 🔧 Customization

### Control Number of Bullets
```python
summary = summarizer.summarize_from_text(text, max_bullets=10)
```

### Change AI Model
```python
summarizer = ReportSummarizer(model="gpt-4")  # Higher accuracy, higher cost
```

### Custom System Prompt
Modify the `prompt` variable in the `summarize()` method for different output styles.

---

## 💰 Cost Estimate

Using GPT-3.5-turbo (default):
- **~$0.001** per summary (average 500 word document)
- **~1000 summaries** per $1 USD
- Input: $0.0005 per 1K tokens
- Output: $0.0015 per 1K tokens

---

## ⚠️ Troubleshooting

| Error | Solution |
|-------|----------|
| `No module named 'openai'` | Run `pip install -r requirements.txt` |
| `API key not found` | Check that `.env` file exists and contains `OPENAI_API_KEY` |
| `PDF read error` | Ensure `pypdf` is installed: `pip install pypdf` |
| `Rate limited` | Add delay: `import time; time.sleep(1)` between calls |
| `Content too short` | Documents must be at least 50 characters |

---

## 📚 File Structure

```
report_summarizer.py       # Main script
requirements.txt          # Python dependencies
.env.example             # Environment template
.env                     # Your API key (create from .env.example)
SETUP_GUIDE.md           # Detailed documentation
QUICK_START.md           # This file
examples.py              # Usage examples
```

---

## 🎯 What's Next?

1. ✅ Try the demo: `python report_summarizer.py`
2. ✅ Run interactive mode: `python report_summarizer.py --interactive`
3. ✅ Review examples: `python examples.py`
4. ✅ Integrate into your project: `from report_summarizer import ReportSummarizer`

---

## 📝 Notes

- API calls are **not logged** by default - your data is only sent to OpenAI's API
- Summaries are generated fresh each time (not cached)
- Max input size: ~4000 words (to stay within token limits)
- Temperature set to 0.7 for balance between consistency and creativity

---

## 🆘 Need Help?

1. Check inline code comments in `report_summarizer.py`
2. Review docstrings: `python -c "from report_summarizer import ReportSummarizer; help(ReportSummarizer)"`
3. Run examples: `python examples.py`
4. OpenAI API docs: https://platform.openai.com/docs/

Happy summarizing! 🎉
