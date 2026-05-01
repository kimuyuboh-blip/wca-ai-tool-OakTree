# OakTree Report Summarizer
## A Comprehensive Project Report

---

## 1. Cover Page

**Project Name:** OakTree Report Summarizer

**Group Name:** OakTree Group

**Team Members:** 
- Kimuyu Carlos
- Favour Azu
- Loise Owoko
- Rose Kariuki
- Eugene Kiprono

**GitHub Repository:** [https://github.com/kimuyuboh-blip/wca-ai-tool-OakTree](https://github.com/kimuyuboh-blip/wca-ai-tool-OakTree)

**Tool Name:** OakTree Report Summarizer

**Date:** April 26, 2026

**Version:** 1.0

---

## 2. Problem Statement

### The Challenge
In today's information-saturated world, professionals across industries face an overwhelming volume of documents that require analysis: business reports, research papers, legal contracts, policy documents, and more. Reading and comprehending these lengthy documents consumes valuable time that could be spent on strategic decision-making and implementation.

### The Problem OakTree Solves
OakTree addresses this critical pain point by automating the document summarization process. Instead of spending hours reading lengthy reports, users can now:
- Upload a PDF or Word document
- Receive an AI-generated executive summary in minutes
- Extract key insights, findings, and actionable recommendations
- Download results for further use

### Who Benefits
**Primary Users:**
- **Business Professionals:** Executives, managers, and analysts who need to quickly review reports, market analyses, and strategic documents
- **Legal Professionals:** Lawyers and paralegals who need to summarize contracts, case briefs, and legal documents
- **Researchers:** Academics and researchers who need to extract key findings from literature reviews and research papers
- **Students:** Graduate and undergraduate students working with thesis research and academic papers
- **Government Officials:** Policy makers and administrators reviewing lengthy proposals and administrative documents

### The Impact
Without OakTree, users must invest significant time reading entire documents. With OakTree, they can:
1. **Save Time:** Reduce document review time from hours to minutes
2. **Improve Productivity:** Focus on decision-making rather than information gathering
3. **Enhance Comprehension:** Get structured, bulleted summaries that highlight critical points
4. **Enable Scale:** Process multiple documents efficiently

---

## 3. Tool Description

### Overview
OakTree Report Summarizer is a web-based application built with Streamlit that leverages OpenAI's GPT-4o model to analyze and summarize PDF and Word documents. The tool intelligently handles documents of any length by chunking them into manageable pieces while maintaining context coherence.

### Key Features
1. **Web-Based Interface:** User-friendly Streamlit application accessible through a web browser
2. **Multi-Format Support:** Accepts both PDF (.pdf) and Word (.docx) file formats
3. **Smart Document Chunking:** Automatically splits large documents to stay within API token limits
4. **Advanced AI Summarization:** Uses GPT-4o for accurate, professional summaries
5. **Session Persistence:** Maintains summary results across page interactions
6. **Easy Download:** Export summaries as text files for external use
7. **Robust Error Handling:** Clear error messages for API authentication and rate-limit issues
8. **Secure API Handling:** API keys are not stored—used only during the session

### How Users Interact With OakTree

**Step 1: Launch the Application**
```
streamlit run oakTree.py
```
The application opens in a browser at `http://localhost:8501`

**Step 2: Enter API Key**
- User enters their OpenAI API key in the left sidebar
- The key is kept confidential and used only for the current session

**Step 3: Upload Document**
- User clicks "Upload PDF or DOCX" and selects a document
- The application displays the selected file name

**Step 4: Initiate Summarization**
- User clicks the "Summarize with OakTree" button
- A loading spinner appears indicating processing

**Step 5: Review Results**
- The summary appears on the screen in a structured format
- Key sections include: Core Objective, Key Insights, and Critical Implications

**Step 6: Take Action**
- **Download as Text:** Save the summary locally for sharing or archiving
- **Clear Results:** Reset the app to process another document

### User Flow Diagram
```
User Launches App
      ↓
Enter OpenAI API Key
      ↓
Upload PDF or DOCX File
      ↓
Click "Summarize with OakTree"
      ↓
OakTree Processes & Chunks Document
      ↓
AI Generates Summaries for Each Chunk
      ↓
AI Synthesizes Final Summary
      ↓
User Views Summary
      ↓
Download or Clear for Next Document
```

---

## 4. AI Instruction Design: R-T-C-C-O Prompt Analysis

OakTree uses carefully designed system prompts following the R-T-C-C-O framework (Role, Task, Context, Constraints, Output).

### Prompt 1: Individual Chunk Summarization

**Prompt Content:**
```
[Role] Act as a senior business analyst and expert technical writer.

[Context] I am providing a long, detailed document (PDF/report). I need to understand the core message, 
critical insights, and action items quickly without reading the entire text.

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

**Justification:**
- **Role Definition:** Establishes the AI as a senior business analyst, which encourages professional, strategic thinking rather than superficial summarization
- **Context Clarity:** Explains the real-world scenario and user need, helping the AI understand the urgency and professional context
- **Task Specificity:** Clear directive to create an "executive summary" rather than a generic summary—this implies high-level thinking
- **Constraints:** Prevents output bloat and ensures relevance; the 300-word limit maintains focus on critical information
- **Format Specification:** Structured output ensures consistency across all chunks, making the final synthesis easier

### Prompt 2: Multi-Chunk Synthesis

**Prompt Content:**
```
Synthesize the following partial summaries into one final bulleted report (max 300 words). 
Focus only on primary findings and recommended actions.
```

**Justification:**
- **Simplicity:** After individual chunks are summarized, the synthesis task is simpler—combining summaries rather than summarizing raw text
- **Consistency:** Maintains the 300-word limit across final output
- **Focus:** Explicitly asks for "primary findings" to eliminate redundancy and secondary information
- **Actionability:** Emphasizes "recommended actions" to ensure the final summary is practical

### Design Choices

**Temperature Setting: 0.3 (Low)**
- Ensures consistent, deterministic output for reliable summaries
- Reduces hallucination and creative elaboration
- Appropriate for factual document summarization

**Model: GPT-4o**
- State-of-the-art reasoning capabilities for nuanced document analysis
- Superior performance on multi-step tasks (chunking → summarization → synthesis)
- Balanced cost-to-performance ratio

**Max Tokens: 400 per Chunk**
- Allows detailed summaries without exceeding output limits
- Provides buffer above the 300-word constraint for structured formatting

---

## 5. Technical Overview

### Architecture Overview

OakTree follows a modular, single-file architecture suitable for Streamlit applications:

```
Imports & Configuration
        ↓
System Prompts Definition
        ↓
Helper Functions (chunk_text, extract_text, format_summary_as_json)
        ↓
Streamlit Page Setup
        ↓
Sidebar API Configuration
        ↓
Session State Management
        ↓
File Processing Pipeline
        ↓
Results Display & Export
```

### Core Components

#### 1. **Imports**
```python
import streamlit as st                  # Web framework
from openai import OpenAI              # API client
from pypdf import PdfReader            # PDF processing
from docx import Document              # Word document processing
import json                            # Data formatting
from datetime import datetime          # Timestamps
```

**Purpose:** Each import serves a specific function:
- Streamlit creates the interactive web UI
- OpenAI client enables GPT-4o integration
- pypdf and python-docx handle multi-format document parsing
- json and datetime support export functionality

#### 2. **Text Chunking Function**
```python
def chunk_text(text, max_tokens=12000):
    """Simple character-based chunking to stay within context limits."""
    return [text[i : i + max_tokens] for i in range(0, len(text), max_tokens)]
```

**Why 12,000 characters?**
- OpenAI's GPT-4o model has a 128K token context window
- Rough conversion: 1 token ≈ 4 characters
- 12,000 characters ≈ 3,000 tokens per chunk (leaves buffer for system prompt and response)
- Ensures safe operation within token limits

**Algorithm:**
- Simple character-based chunking (not word-aware)
- Advantage: Guaranteed size limits
- Trade-off: Chunks may split mid-sentence, but individual LLM calls are short-lived

#### 3. **Text Extraction Pipeline**

**PDF Processing:**
```python
if uploaded_file.type == "application/pdf":
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"
```
- Uses pypdf library to read PDF page-by-page
- Preserves document structure with newline separators

**Word Document Processing:**
```python
elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
    doc = Document(uploaded_file)
    for para in doc.paragraphs:
        text += para.text + "\n"
```
- Uses python-docx to access paragraph structure
- Maintains formatting through paragraph-level extraction

**Output:** Unified plain text representation of both formats

#### 4. **Session State Management**
```python
if "summary" not in st.session_state:
    st.session_state.summary = ""
```

**Purpose:** 
- Streamlit reruns the entire script on user interaction
- Session state persists variables across reruns
- Without this, the summary would disappear after each interaction

#### 5. **Summarization Pipeline**

**Step 1: Chunk Processing**
```python
text_chunks = chunk_text(doc_text)
summaries = []

for i, chunk in enumerate(text_chunks):
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_CHUNK},
            {"role": "user", "content": f"Summarize this part of the report:\n\n{chunk}"}
        ],
        max_tokens=400,
        temperature=0.3
    )
    summaries.append(response.choices[0].message.content)
```

**Processing Details:**
- Iterates through each text chunk
- Sends chunk to GPT-4o with role-based system prompt
- Collects AI response in summaries list
- max_tokens=400 prevents excessively long individual summaries

**Step 2: Synthesis (Multi-Chunk Documents)**
```python
if len(summaries) > 1:
    final_input = "\n\n".join(summaries)
    final_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": SYSTEM_PROMPT_SYNTHESIS},
            {"role": "user", "content": final_input}
        ]
    )
    st.session_state.summary = final_response.choices[0].message.content
else:
    st.session_state.summary = summaries[0]
```

**Logic:**
- If document had multiple chunks: Combine all summaries and ask GPT-4o to create a unified final summary
- If document fit in one chunk: Use that summary directly (no synthesis needed)

#### 6. **Error Handling**
```python
except Exception as e:
    error_msg = str(e).lower()
    if "api_key" in error_msg or "authentication" in error_msg:
        st.error("❌ Authentication Error: Your API key is invalid.")
    elif "rate_limit" in error_msg:
        st.error("❌ Rate Limit: You've sent too many requests. Please wait a moment.")
    else:
        st.error(f"❌ Error: {str(e)}")
```

**Error Types Handled:**
- API Authentication: Invalid or missing API key
- Rate Limiting: Too many requests sent too quickly
- Generic Errors: Catch-all for unexpected issues

### Data Flow Diagram

```
User Upload
    ↓
File Type Check (PDF/DOCX)
    ↓
Text Extraction (PDF Reader / DOCX Parser)
    ↓
Plain Text → Chunking (12K char chunks)
    ↓
For Each Chunk: OpenAI API Call
    ├─ System Prompt (Role, Context, Task)
    ├─ Chunk Text
    └─ Response: Individual Summary
    ↓
Collect All Summaries
    ↓
If Multiple Chunks:
    ├─ Combine All Summaries
    └─ OpenAI Synthesis Call → Final Summary
    
Final Summary → Display & Export
```

### Key Technical Decisions

| Decision | Rationale |
|----------|-----------|
| **Streamlit Framework** | Rapid development, built-in components, no frontend expertise required |
| **Character-Based Chunking** | Guarantees size limits; simpler than token counting |
| **GPT-4o Model** | Superior reasoning for multi-step summarization tasks |
| **Low Temperature (0.3)** | Consistent, deterministic output for factual documents |
| **Two-Phase Approach** | Handles arbitrarily large documents by chunking + synthesis |
| **Session State** | Persists results across user interactions without database |
| **Streamlined UI** | Sidebar for config, main area for processing—clean UX |

---

## 6. Challenges & Solutions

### Challenge 1: Handling Arbitrary Document Sizes

**The Problem:**
- OpenAI API has token limits (even with GPT-4o's 128K context window)
- Users might upload 100+ page documents
- Sending entire documents to API would exceed limits and cause errors

**The Solution: Two-Phase Chunking & Synthesis**
1. **Phase 1 - Chunking:** Break document into 12K character chunks
2. **Phase 2 - Summarization:** Process each chunk individually with GPT-4o
3. **Phase 3 - Synthesis:** Combine all chunk summaries into one final summary

**Why This Works:**
- No single API call exceeds token limits
- Individual summaries capture key points from each section
- Synthesis merges summaries while eliminating redundancy
- Scalable to documents of any length

**Trade-offs Accepted:**
- Chunking may split mid-sentence
- Slightly higher API costs (multiple calls instead of one)
- Small risk of losing context at chunk boundaries

**Mitigation:**
- Added buffer tokens to prevent mid-word splits (12K chars ≈ 3K tokens per chunk)
- System prompts emphasize focus on "critical information" to reduce redundancy
- Synthesis phase explicitly asks for "primary findings" to eliminate duplicates

---

### Challenge 2: Multi-Format Document Support

**The Problem:**
- PDFs and Word documents have different internal structures
- PDF text extraction can produce formatting artifacts
- Word documents have embedded formatting that must be stripped

**The Solution: Format-Specific Extraction**
```python
# PDF: Use pypdf library with page-by-page iteration
if uploaded_file.type == "application/pdf":
    reader = PdfReader(uploaded_file)
    for page in reader.pages:
        text += page.extract_text() + "\n"

# DOCX: Use python-docx with paragraph-level access
elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
    doc = Document(uploaded_file)
    for para in doc.paragraphs:
        text += para.text + "\n"
```

**Why This Works:**
- pypdf is the industry standard for PDF text extraction
- python-docx parses the XML structure of .docx files properly
- Both libraries extract clean text without formatting artifacts
- Separate file type handling prevents cross-contamination

---

### Challenge 3: Streamlit Rerun Behavior

**The Problem:**
- Streamlit reruns the entire script on every user interaction
- Without proper state management, summary results would disappear when user interacts with the page
- Naive implementation would trigger summarization multiple times

**The Solution: Session State Management**
```python
if "summary" not in st.session_state:
    st.session_state.summary = ""

# ... later, after summarization ...
st.session_state.summary = final_response.choices[0].message.content

# ... display results ...
if st.session_state.summary:
    st.markdown(st.session_state.summary)
```

**Why This Works:**
- Streamlit's session_state is a dictionary that persists across reruns
- Check for summary existence prevents re-processing on page interactions
- Summary persists until user clicks "Clear Results"

---

### Challenge 4: API Key Security

**The Problem:**
- Users enter sensitive OpenAI API keys into the app
- Storing keys in code or files is a security liability
- Users worry about key theft or misuse

**The Solution: Session-Only Key Storage**
```python
api_key = st.text_input("Enter your OpenAI API Key", type="password")
# Key exists only in RAM during this session
# No persistent storage; no file writes
```

**Why This Works:**
- `type="password"` masks the input visually
- Key stored in RAM only for the session duration
- When browser closes or session ends, key is discarded
- No database or file system involvement

**User Education:**
- Clear sidebar message: "Your key is not stored. It is used only for the duration of this session."

---

### Challenge 5: API Error Handling & User Experience

**The Problem:**
- Generic API errors confuse users
- Users don't know whether to retry, check their key, or wait
- Poor error messages reduce trust in the tool

**The Solution: Specific Error Detection & Clear Messages**
```python
except Exception as e:
    error_msg = str(e).lower()
    if "api_key" in error_msg or "authentication" in error_msg:
        st.error("❌ Authentication Error: Your API key is invalid.")
    elif "rate_limit" in error_msg:
        st.error("❌ Rate Limit: You've sent too many requests. Please wait a moment.")
    else:
        st.error(f"❌ Error: {str(e)}")
```

**Error Categories & Responses:**
| Error Type | User Action |
|-----------|-------------|
| Authentication | Check/update API key |
| Rate Limit | Wait and retry |
| Generic | Share error with support |

**Why This Works:**
- Users understand what went wrong
- Clear next steps reduce frustration
- Distinguishes user errors (invalid key) from system issues (rate limits)

---

### Challenge 6: Summary Quality & Consistency

**The Problem:**
- Without specific prompts, GPT-4o produces variable summary formats
- Unstructured summaries are hard to scan quickly
- Different chunks might use different formats

**The Solution: Structured Prompt with Format Specification**
```
[Format] Return the output in the following structure:
    Executive Summary: [Insert Document Title]
    - Core Objective/Purpose: [1-2 sentences]
    - Key Insights/Findings: [3-5 concise bullet points]
    - Critical Implications/Recommendations: [2-3 bullet points]
```

**Why This Works:**
- Explicit format specification ensures consistent output
- Structured format is scannable and professional
- Bullet points are easier to read than paragraph prose
- Sections organize information logically

---

## 7. Ethics Reflection

### 1. Bias & Fairness Considerations

**Potential Bias Issues:**
- **Source Bias:** Documents written with bias (e.g., reports favoring one political viewpoint) will be preserved in summaries
- **Training Data Bias:** GPT-4o was trained on internet data with inherent societal biases
- **Selection Bias:** Users might cherry-pick documents to summarize, reinforcing their own perspectives

**Our Approach:**
- **Transparency:** Users should understand that summaries reflect the source material's perspective
- **Education:** We recommend users summarize multiple viewpoints on controversial topics
- **Neutrality:** Our system prompts ask for "critical information" and "key findings," not opinions—neutral language

**Limitations We Accept:**
- We cannot eliminate bias present in source documents
- GPT-4o reflects training data biases that are difficult to measure
- Tool design cannot force balanced information consumption

---

### 2. Privacy & Data Handling

**Privacy Concerns:**
- Users upload potentially confidential documents (contracts, financial reports, medical information)
- Documents are sent to OpenAI's servers
- Uploaded content may be used for model improvements (depending on OpenAI's policies)

**Our Safeguards:**
- **API Key Only:** We do not store documents; they're processed in-memory and sent directly to OpenAI
- **No Persistence:** Summaries exist only in session state; no database storage
- **Clear Warnings:** We display session-only storage information in the sidebar
- **User Control:** Users can clear results immediately after use

**Recommendations for Users:**
1. **Do Not Upload Highly Sensitive Data:** If document contains trade secrets, use OpenAI's enterprise plans with different terms
2. **Check OpenAI's Privacy Policy:** Users should review OpenAI's data handling practices for their organization
3. **Review Exported Summaries:** After export, sensitive information should be stored securely

---

### 3. Responsible AI & Information Integrity

**Potential Misuse:**
- **Misinformation Amplification:** Summaries of false information still convey that information
- **Context Loss:** Summarization may inadvertently remove important caveats or nuance
- **Over-Reliance:** Users might trust summaries without verifying sources
- **Plagiarism:** Users could pass AI-generated summaries off as their own analysis

**Our Mitigation Strategies:**
- **Accuracy Focus:** System prompt emphasizes "ensure the summary is accurate to the original text"
- **Structure Transparency:** Format clearly shows we're presenting "Key Insights" not "Verified Facts"
- **Limitation Acceptance:** We acknowledge that summarization inherently involves some information loss

**User Responsibility:**
- Summaries should be starting points, not definitive analyses
- Always verify key claims with source material
- Attribute summaries to OakTree tool (not personal analysis)
- Use tool responsibly for legitimate document review

---

### 4. Environmental Impact

**Consideration:** Each API call to GPT-4o consumes computational resources and energy.

**Our Approach:**
- **Efficiency Design:** Two-phase chunking is more efficient than naive per-sentence summarization
- **Reasonable Defaults:** 12K character chunks balance accuracy and cost
- **User Choice:** Users decide whether summarization value justifies energy use

**Future Improvements:**
- Allow local model alternatives (less energy, no API calls)
- Implement caching to avoid redundant summarization
- Provide cost/environmental transparency

---

### 5. Accessibility & Inclusivity

**Current Considerations:**
- Streamlit interface is reasonably accessible to keyboard navigation
- No support for non-English documents (GPT-4o does support other languages, but prompts are English)
- No text-to-speech or screen reader optimization

**Our Commitment:**
- Keep interface simple and navigable
- Provide clear error messages
- Consider internationalization in future versions

---

## 8. Conclusion & Future Improvements

### Project Summary
OakTree Report Summarizer successfully addresses the growing challenge of document overload in professional and academic settings. By combining Streamlit's intuitive interface, intelligent document chunking, and GPT-4o's reasoning capabilities, OakTree enables users to transform lengthy documents into actionable insights in minutes rather than hours.

### Key Achievements
✅ **Multi-Format Support:** Seamlessly handles PDF and Word documents  
✅ **Scalable Architecture:** Processes documents of arbitrary length through intelligent chunking  
✅ **User-Friendly Interface:** Clean, intuitive web interface requiring no technical expertise  
✅ **Reliable Error Handling:** Clear feedback for common issues (invalid API key, rate limiting)  
✅ **Secure Design:** No persistent storage of sensitive data or API keys  
✅ **Professional Output:** Structured summaries with clear sections and bullet points

### Future Improvement Opportunities

#### 1. **Local Model Integration**
- **Benefit:** Reduce API costs and privacy concerns
- **Implementation:** Add support for open-source models (e.g., Llama 2, Mistral) via local deployment
- **Impact:** Enable on-premise deployment for enterprises

#### 2. **Advanced Customization**
- **Benefit:** Users can specify summary focus and detail level
- **Implementation:** Add UI sliders for summary length, focus area (technical vs. executive), and depth level
- **Example:** "Technical Summary for Engineers" vs. "Executive Summary for C-Suite"

#### 3. **Multi-Language Support**
- **Benefit:** Serve global users with non-English documents
- **Implementation:** Auto-detect language, translate to English (or process native), provide multilingual UI
- **Impact:** Expand addressable market

#### 4. **Caching & History**
- **Benefit:** Faster re-summarization, document library management
- **Implementation:** Store document hashes + summaries for quick retrieval
- **Trade-off:** Requires persistent storage (database) vs. current session-only design

#### 5. **Batch Processing**
- **Benefit:** Summarize multiple documents in one session
- **Implementation:** Allow folder upload, queue processing, downloadable summary pack
- **Use Case:** Analysts reviewing 50+ quarterly reports at once

#### 6. **Comparative Analysis**
- **Benefit:** Compare summaries of similar documents
- **Implementation:** Highlight similarities, differences, contradictions between summaries
- **Use Case:** Competitive intelligence, legal document review

#### 7. **Export Enhancements**
- **Benefit:** Better integration with productivity tools
- **Implementation:** Add export to PDF, Word, Google Docs, Notion
- **Current:** Text-only export
- **Improvement:** Formatted documents with styling

#### 8. **Real-Time Streaming**
- **Benefit:** Faster user feedback, more responsive interface
- **Implementation:** Stream summary as it's generated (rather than waiting for complete response)
- **Technology:** OpenAI streaming API + Streamlit streaming support

#### 9. **Summary Confidence Scoring**
- **Benefit:** Users know when a summary is reliable vs. uncertain
- **Implementation:** Add confidence scores for key points based on source text repetition
- **Output:** "★★★ High Confidence" vs. "★ Low Confidence"

#### 10. **Analytics Dashboard**
- **Benefit:** Track tool usage, cost, and effectiveness
- **Implementation:** Log summaries (with user consent), provide usage statistics
- **Data:** Documents processed, API costs, processing time

#### 11. **Mobile App**
- **Benefit:** Summarize on-the-go
- **Implementation:** React Native or Flutter app with same functionality
- **Challenge:** Managing API key securely on mobile

#### 12. **AI-Powered Q&A**
- **Benefit:** Users ask questions about documents rather than just reading summaries
- **Implementation:** Store document embeddings, allow follow-up questions via retrieval-augmented generation (RAG)
- **Use Case:** "What is the contract renewal date?" on a large contract

### Why These Matter
The roadmap balances:
- **User Needs:** Customization, multi-language support, batch processing
- **Technical Feasibility:** Most improvements use existing technologies
- **Business Value:** Expanded use cases (batch processing, B2B) and differentiation (comparative analysis, analytics)
- **Responsibility:** Caching reduces environmental impact; confidence scores improve information integrity

### Realistic Timeline (Hypothetical)
- **Month 1-2:** Advanced Customization + Batch Processing
- **Month 2-3:** Caching & History + Real-Time Streaming
- **Month 3-4:** Multi-Language Support + Export Enhancements
- **Month 4-5:** Local Model Integration + Analytics Dashboard
- **Month 5-6:** AI-Powered Q&A + Mobile Prototype

### Conclusion
OakTree demonstrates how thoughtful AI tool design can solve real problems while maintaining user trust through privacy, transparency, and ethical practice. The combination of intelligent chunking, structured prompting, and clean UI creates a solution that feels both powerful and simple. With future improvements, OakTree can expand from a document summarization tool to a comprehensive document intelligence platform.

---

## 9. Appendix: Full Source Code

### File: `oakTree.py`

```python
# ============================================================================
# IMPORTS: Required libraries for the Streamlit web app and AI integration
# ============================================================================
import streamlit as st                  # Web app framework for building UI
from openai import OpenAI              # OpenAI API client for GPT models
from pypdf import PdfReader            # Library to extract text from PDF files
from docx import Document              # Library to extract text from Word documents
import json                            # JSON library for data serialization and formatting
from datetime import datetime          # For adding timestamp metadata to exports

# ============================================================================
# SYSTEM PROMPTS: AI Instructions for Summarization
# ============================================================================
SYSTEM_PROMPT_CHUNK = """[Role] Act as a senior business analyst and expert technical writer.

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
"""

SYSTEM_PROMPT_SYNTHESIS = """Synthesize the following partial summaries into one final bulleted report (max 300 words). Focus only on primary findings and recommended actions."""

# ============================================================================
# FUNCTION 1: chunk_text()
# Purpose: Break large documents into smaller chunks to avoid token limits
# This prevents context window overflow when sending to OpenAI API
# ============================================================================
def chunk_text(text, max_tokens=12000):
    """Simple character-based chunking to stay within context limits."""
    return [text[i : i + max_tokens] for i in range(0, len(text), max_tokens)]

# ============================================================================
# FUNCTION 2: extract_text()
# Purpose: Read and extract text content from uploaded PDF or DOCX files
# Supports both PDF and Word document formats
# ============================================================================
def extract_text(uploaded_file):
    """Extract text from PDF or DOCX files."""
    text = ""
    # Handle PDF files
    if uploaded_file.type == "application/pdf":
        reader = PdfReader(uploaded_file)
        # Loop through each page and extract text
        for page in reader.pages:
            text += page.extract_text() + "\n"
    # Handle Word documents (.docx)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        doc = Document(uploaded_file)
        # Loop through each paragraph and extract text
        for para in doc.paragraphs:
            text += para.text + "\n"
    return text

# ============================================================================
# FUNCTION 3: format_summary_as_json()
# Purpose: Convert summary text to structured JSON format with metadata
# Useful for integration with other systems or APIs
# ============================================================================
def format_summary_as_json(summary, filename="report"):
    """Convert summary to JSON format with metadata."""
    json_data = {
        "metadata": {
            "tool": "OakTree Report Summarizer",
            "version": "1.0",
            "timestamp": datetime.now().isoformat(),
            "source_file": filename
        },
        "summary": summary
    }
    return json.dumps(json_data, indent=2)


# ============================================================================
# STREAMLIT PAGE CONFIGURATION
# Sets the browser tab title and page icon
# ============================================================================
st.set_page_config(page_title="OakTree Summarizer", page_icon="🌳")
st.title("OakTree Report Summarizer")

# ============================================================================
# SIDEBAR CONFIGURATION
# Purpose: Collect API key and display user information in a collapsible menu
# The sidebar keeps the main area clean and organized
# ============================================================================
with st.sidebar:
    st.header("Configuration")
    api_key = st.text_input("Enter your OpenAI API Key", type="password")
    st.info("Your key is not stored. It is used only for the duration of this session.")

# ============================================================================
# SESSION STATE INITIALIZATION
# Purpose: Store the summary result across page reruns in Streamlit
# Session state persists data while the user interacts with the app
# ============================================================================
if "summary" not in st.session_state:
    st.session_state.summary = ""

# ============================================================================
# API KEY VALIDATION
# Purpose: Ensure user has provided an API key before proceeding
# If no key is provided, stop execution and prompt the user
# ============================================================================
if not api_key:
    st.warning("Please enter your OpenAI API key in the sidebar to proceed.")
    st.stop()

# ============================================================================
# INITIALIZE OPENAI CLIENT
# Purpose: Create OpenAI API client with the user's API key for API calls
# ============================================================================
client = OpenAI(api_key=api_key)

# ============================================================================
# FILE UPLOADER WIDGET
# Purpose: Allow users to upload PDF or DOCX files for summarization
# Only accepts these file types to prevent processing unsupported formats
# ============================================================================
uploaded_file = st.file_uploader("Upload PDF or DOCX", type=["pdf", "docx"])

# ============================================================================
# FILE PROCESSING BLOCK
# Purpose: Handle user interactions after file upload
# ============================================================================
if uploaded_file:
    # Extract text from the uploaded document
    doc_text = extract_text(uploaded_file)
    
    # ========================================================================
    # SUMMARIZATION BUTTON
    # Purpose: Trigger the summarization process when clicked
    # ========================================================================
    if st.button("Summarize with OakTree"):
        # Display a loading indicator while processing
        with st.spinner("OakTree is processing your report..."):
            try:
                # ====================================================================
                # STEP 1: TEXT CHUNKING
                # Purpose: Split large documents into manageable chunks
                # This prevents exceeding OpenAI's token limits per request
                # ====================================================================
                text_chunks = chunk_text(doc_text)
                summaries = []

                # ====================================================================
                # STEP 2: PROCESS EACH CHUNK
                # Purpose: Send each chunk to OpenAI for individual summarization
                # Collects summaries from all chunks
                # ====================================================================
                for i, chunk in enumerate(text_chunks):
                    response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT_CHUNK},
                            {"role": "user", "content": f"Summarize this part of the report:\n\n{chunk}"}
                        ],
                        max_tokens=400,
                        temperature=0.3
                    )
                    summaries.append(response.choices[0].message.content)

                # ====================================================================
                # STEP 3: SYNTHESIZE MULTIPLE SUMMARIES (if needed)
                # Purpose: If document had multiple chunks, combine summaries into one
                # Creates a final consolidated summary with no redundancy
                # ====================================================================
                if len(summaries) > 1:
                    final_input = "\n\n".join(summaries)
                    final_response = client.chat.completions.create(
                        model="gpt-4o",
                        messages=[
                            {"role": "system", "content": SYSTEM_PROMPT_SYNTHESIS},
                            {"role": "user", "content": final_input}
                        ]
                    )
                    st.session_state.summary = final_response.choices[0].message.content
                else:
                    # If only one chunk, use its summary directly
                    st.session_state.summary = summaries[0]

            # ====================================================================
            # ERROR HANDLING
            # Purpose: Catch and display specific error types to help users debug
            # ====================================================================
            except Exception as e:
                error_msg = str(e).lower()
                # Check for authentication issues
                if "api_key" in error_msg or "authentication" in error_msg:
                    st.error("❌ Authentication Error: Your API key is invalid.")
                # Check for rate limiting
                elif "rate_limit" in error_msg:
                    st.error("❌ Rate Limit: You've sent too many requests. Please wait a moment.")
                # Generic error handling
                else:
                    st.error(f"❌ Error: {str(e)}")


# ============================================================================
# DISPLAY RESULTS SECTION
# Purpose: Show the generated summary and provide download/clear options
# Only displays if a summary has been generated
# ============================================================================
if st.session_state.summary:
    st.subheader("Summary")
    # Display the summary in markdown format for better formatting
    st.markdown(st.session_state.summary)

    # ========================================================================
    # ACTION BUTTONS (Download & Clear)
    # Purpose: Provide user options to save or reset the summarization
    # ========================================================================
    col1, col2, col3 = st.columns(3)
    
    # Download button: Allows user to save summary as text file
    with col1:
        st.download_button(
            label="Download as Text",
            data=st.session_state.summary,
            file_name="OakTree_Summary.txt",
            mime="application/text"
        )
    
    # Download button: Allows user to save summary as JSON file
    with col2:
        json_data = format_summary_as_json(st.session_state.summary)
        st.download_button(
            label="Download as JSON",
            data=json_data,
            file_name="OakTree_Summary.json",
            mime="application/json"
        )
    
    # Clear button: Resets the app to allow processing a new document
    with col3:
        if st.button("Clear Results"):
            st.session_state.summary = ""
            # Rerun the app to refresh the UI
            st.rerun()
```

### File: `requirements.txt`

```
altair==6.0.0
annotated-types==0.7.0
anyio==4.13.0
attrs==26.1.0
blinker==1.9.0
cachetools==7.0.5
certifi==2026.2.25
charset-normalizer==3.4.7
click==8.3.2
distro==1.9.0
gitdb==4.0.12
GitPython==3.1.46
h11==0.16.0
httpcore==1.0.9
httpx==0.28.1
idna==3.11
Jinja2==3.1.6
jiter==0.14.0
jsonschema==4.26.0
jsonschema-specifications==2025.9.1
lxml==6.1.0
MarkupSafe==3.0.3
narwhals==2.20.0
numpy==2.4.4
openai==2.32.0
packaging==26.1
pandas==3.0.2
pillow==12.2.0
protobuf==7.34.1
pyarrow==23.0.1
pydantic==2.13.3
pydantic_core==2.46.3
pydeck==0.9.2
pypdf==6.10.2
python-dateutil==2.9.0.post0
python-docx==1.2.0
referencing==0.37.0
requests==2.33.1
rpds-py==0.30.0
six==1.17.0
smmap==5.0.3
sniffio==1.3.1
streamlit==1.56.0
tenacity==9.1.4
toml==0.10.2
tornado==6.5.5
tqdm==4.67.3
typing-inspection==0.4.2
typing_extensions==4.15.0
urllib3==2.6.3
```

### File: `README.md`

```markdown
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

**Repository:** [https://github.com/kimuyuboh-blip/wca-ai-tool-OakTree](https://github.com/kimuyuboh-blip/wca-ai-tool-OakTree)
