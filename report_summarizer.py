#!/usr/bin/env python3
"""Report Summarizer Tool - Generates executive summaries using OpenAI API."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI
from pypdf import PdfReader
from docx import Document

load_dotenv()


class ReportSummarizer:
    """Summarizes reports using OpenAI's API."""
    
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = model
    
    def extract_pdf_text(self, file_path):
        """Extract text from PDF file."""
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        return text
    
    def extract_docx_text(self, file_path):
        """Extract text from Word document."""
        doc = Document(file_path)
        return "\n".join([para.text for para in doc.paragraphs])
    
    def read_file(self, file_path):
        """Read text from PDF, DOCX, or TXT file."""
        path = Path(file_path)
        
        if path.suffix.lower() == ".pdf":
            return self.extract_pdf_text(file_path)
        elif path.suffix.lower() == ".docx":
            return self.extract_docx_text(file_path)
        else:
            return path.read_text(encoding="utf-8")
    
    def summarize(self, content, max_bullets=8):
        """Generate executive summary with bullet points."""
        if len(content) < 50:
            raise ValueError("Content too short")
        
        response = self.client.chat.completions.create(
            model=self.model,
            messages=[
                {"role": "system", "content": "Create clear, concise executive summaries."},
                {"role": "user", "content": f"Summarize this in {max_bullets} bullet points:\n\n{content[:5000]}"}
            ],
            max_tokens=500,
            temperature=0.7
        )
        
        return response.choices[0].message.content


if __name__ == "__main__":
    summarizer = ReportSummarizer()
    
    if len(sys.argv) > 1:
        file_path = sys.argv[1]
        try:
            content = summarizer.read_file(file_path)
            summary = summarizer.summarize(content, max_bullets=5)
            print(f"Summary of {file_path}:\n\n{summary}")
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found.")
        except Exception as e:
            print(f"Error: {e}")
    else:
        # Demo with sample text
        sample = """The quarterly report shows mixed results. Revenue increased 12% to $4.2B, 
        but costs rose due to supply chain issues. North America grew 8%, Europe declined 3%, 
        while Asia surged 24%. Key wins: 3 new products, 15% better retention. Challenges: 
        supply delays, competition, rising energy costs."""
        
        print(summarizer.summarize(sample, max_bullets=5))
