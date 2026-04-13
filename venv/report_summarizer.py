#!/usr/bin/env python3
"""Report Summarizer Tool - Generates executive summaries using OpenAI API."""

import os
import sys
from pathlib import Path
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


class ReportSummarizer:
    """Summarizes reports using OpenAI's API."""
    
    def __init__(self, api_key=None, model="gpt-3.5-turbo"):
        self.client = OpenAI(api_key=api_key or os.getenv("OPENAI_API_KEY"))
        self.model = modelodel
    
    def read_file(self, file_path):
        """Read text from a file."""
        return Path(file_path).read_text(encoding="utf-8")
    
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
    
    sample = """The quarterly report shows mixed results. Revenue increased 12% to $4.2B, 
    but costs rose due to supply chain issues. North America grew 8%, Europe declined 3%, 
    while Asia surged 24%. Key wins: 3 new products, 15% better retention. Challenges: 
    supply delays, competition, rising energy costs."""
    
    print(summarizer.summarize(sample, max_bullets=5))
