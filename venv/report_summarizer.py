#!/usr/bin/env python3
"""
Report Summarizer Tool
This script takes a long document or report and generates a clean executive summary
using an AI API (OpenAI by default). The summary is formatted as bullet points.

Author: Python Scripts with API Integration
Date: 2026
"""

import os
import sys
import json
from typing import Optional
from pathlib import Path

# Third-party imports for API integration
try:
    import requests
    from openai import OpenAI
except ImportError:
    print("Error: Required packages not found.")
    print("Install with: pip install openai requests python-dotenv")
    sys.exit(1)

# Optional: for environment variable management
try:
    from dotenv import load_dotenv
except ImportError:
    load_dotenv = None


class ReportSummarizer:
    """
    A class to handle report summarization using OpenAI's API.
    
    Features:
    - Reads documents from file or direct text input
    - Sends content to OpenAI API
    - Returns formatted bullet point summaries
    - Includes error handling and logging
    """
    
    def __init__(self, api_key: Optional[str] = None, model: str = "gpt-3.5-turbo"):
        """
        Initialize the ReportSummarizer.
        
        Args:
            api_key: OpenAI API key. If None, loads from OPENAI_API_KEY env variable
            model: The model to use for summarization (default: gpt-3.5-turbo)
        """
        # Load environment variables if dotenv is available
        if load_dotenv:
            load_dotenv()
        
        # Get API key from parameter or environment variable
        self.api_key = api_key or os.getenv("OPENAI_API_KEY")
        
        if not self.api_key:
            raise ValueError(
                "API key not provided. Set OPENAI_API_KEY environment variable "
                "or pass api_key parameter."
            )
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=self.api_key)
        self.model = model
        self.max_tokens = 500  # Limit output length for summaries
    
    def read_document(self, file_path: str) -> str:
        """
        Read a document from a file.
        
        Args:
            file_path: Path to the document file (supports .txt, .pdf, .docx, etc.)
        
        Returns:
            The content of the document as a string
        
        Raises:
            FileNotFoundError: If the file doesn't exist
            ValueError: If the file format is not supported
        """
        file_path = Path(file_path)
        
        # Check if file exists
        if not file_path.exists():
            raise FileNotFoundError(f"File not found: {file_path}")
        
        # Handle different file types
        if file_path.suffix.lower() == ".txt":
            # Simple text file
            with open(file_path, "r", encoding="utf-8") as f:
                return f.read()
        
        elif file_path.suffix.lower() == ".pdf":
            # PDF file handling (requires pypdf library)
            try:
                import pypdf
                with open(file_path, "rb") as f:
                    pdf_reader = pypdf.PdfReader(f)
                    text = "".join(
                        page.extract_text() for page in pdf_reader.pages
                    )
                return text
            except ImportError:
                raise ValueError(
                    "PDF support requires 'pypdf'. Install with: pip install pypdf"
                )
        
        elif file_path.suffix.lower() == ".docx":
            # DOCX file handling (requires python-docx library)
            try:
                from docx import Document
                doc = Document(file_path)
                text = "\n".join(paragraph.text for paragraph in doc.paragraphs)
                return text
            except ImportError:
                raise ValueError(
                    "DOCX support requires 'python-docx'. "
                    "Install with: pip install python-docx"
                )
        
        else:
            raise ValueError(
                f"Unsupported file format: {file_path.suffix}. "
                "Supported: .txt, .pdf, .docx"
            )
    
    def summarize(self, content: str, max_bullets: int = 8) -> str:
        """
        Generate an executive summary from the provided content.
        
        Args:
            content: The text to summarize
            max_bullets: Maximum number of bullet points in the summary (default: 8)
        
        Returns:
            A formatted string with bullet point summary
        
        Raises:
            ValueError: If content is empty or too short
            Exception: If API call fails
        """
        # Validate content
        if not content or len(content.strip()) < 50:
            raise ValueError(
                "Content is too short or empty. Minimum 50 characters required."
            )
        
        # Prepare the prompt for the AI model
        prompt = f"""Please provide a concise executive summary of the following document in exactly {max_bullets} bullet points.

Each bullet point should be:
- Concise (10-20 words)
- Specific and actionable
- Written in simple language

Document:
{content[:5000]}

Format the response as a numbered list with bullet points."""
        
        print("📊 Sending report to AI API for summarization...")
        
        try:
            # Call the OpenAI API
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {
                        "role": "system",
                        "content": "You are an expert business analyst skilled at creating clear, actionable executive summaries."
                    },
                    {
                        "role": "user",
                        "content": prompt
                    }
                ],
                max_tokens=self.max_tokens,
                temperature=0.7  # Balanced between creativity and consistency
            )
            
            # Extract the summary from the response
            summary = response.choices[0].message.content.strip()
            return summary
        
        except Exception as e:
            raise Exception(f"API call failed: {str(e)}")
    
    def summarize_from_file(self, file_path: str, max_bullets: int = 8) -> str:
        """
        Read a document from file and generate a summary.
        
        Args:
            file_path: Path to the document file
            max_bullets: Maximum number of bullet points
        
        Returns:
            Formatted executive summary
        """
        print(f"📂 Reading document: {file_path}")
        content = self.read_document(file_path)
        print(f"✓ Document loaded ({len(content)} characters)")
        
        return self.summarize(content, max_bullets)
    
    def summarize_from_text(self, text: str, max_bullets: int = 8) -> str:
        """
        Generate a summary from direct text input.
        
        Args:
            text: The text content to summarize
            max_bullets: Maximum number of bullet points
        
        Returns:
            Formatted executive summary
        """
        print(f"📝 Processing text input ({len(text)} characters)")
        return self.summarize(text, max_bullets)


# ============================================================================
# Main Execution Functions
# ============================================================================

def main():
    """
    Main function to demonstrate the report summarizer.
    """
    print("=" * 70)
    print("🎯 REPORT SUMMARIZER TOOL")
    print("=" * 70)
    
    # Initialize the summarizer with API key from environment
    try:
        summarizer = ReportSummarizer()
    except ValueError as e:
        print(f"❌ Error: {e}")
        return
    
    # Example: Summarize from text input
    sample_report = """
    The quarterly financial report for Q1 2026 shows mixed results across divisions.
    Revenue increased by 12% year-over-year to $4.2 billion, benefiting from strong
    sales in the technology sector. However, operational costs rose significantly due
    to increased raw material expenses and supply chain disruptions.
    
    The North American market maintained steady growth at 8%, while European operations
    faced headwinds with a 3% decline attributed to macroeconomic challenges and 
    regulatory changes. Asian markets showed exceptional performance with 24% growth,
    driven by successful new product launches.
    
    Key achievements this quarter include:
    - Launch of three new enterprise solutions
    - Expansion into two new geographical markets
    - 15% improvement in customer retention rates
    - 22% increase in R&D spending for innovation
    
    Challenges encountered:
    - Supply chain delays impacting delivery schedules
    - Increased competition in core markets
    - Rising energy costs affecting manufacturing
    - Talent acquisition difficulties in key markets
    
    Recommendations for Q2:
    - Diversify supplier base to mitigate supply chain risks
    - Invest in automation to reduce costs
    - Accelerate digital transformation initiatives
    - Focus on high-margin product lines
    """
    
    try:
        # Generate summary
        summary = summarizer.summarize_from_text(sample_report, max_bullets=5)
        
        # Display results
        print("\n" + "=" * 70)
        print("📋 EXECUTIVE SUMMARY")
        print("=" * 70)
        print(summary)
        print("\n" + "=" * 70)
        
    except Exception as e:
        print(f"❌ Error during summarization: {e}")


def interactive_mode():
    """
    Interactive mode for user input.
    """
    print("=" * 70)
    print("🎯 REPORT SUMMARIZER - INTERACTIVE MODE")
    print("=" * 70)
    
    try:
        summarizer = ReportSummarizer()
    except ValueError as e:
        print(f"❌ Error: {e}")
        return
    
    while True:
        print("\nOptions:")
        print("1. Summarize from file")
        print("2. Summarize from text input")
        print("3. Exit")
        
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            file_path = input("Enter file path: ").strip()
            try:
                summary = summarizer.summarize_from_file(file_path)
                print("\n" + "=" * 70)
                print("📋 EXECUTIVE SUMMARY")
                print("=" * 70)
                print(summary)
                print("=" * 70)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == "2":
            print("Enter your report text (type 'END' on a new line when done):")
            lines = []
            while True:
                line = input()
                if line.strip() == "END":
                    break
                lines.append(line)
            
            text = "\n".join(lines)
            try:
                summary = summarizer.summarize_from_text(text)
                print("\n" + "=" * 70)
                print("📋 EXECUTIVE SUMMARY")
                print("=" * 70)
                print(summary)
                print("=" * 70)
            except Exception as e:
                print(f"❌ Error: {e}")
        
        elif choice == "3":
            print("Goodbye!")
            break
        
        else:
            print("❌ Invalid choice. Please enter 1, 2, or 3.")


# ============================================================================
# Entry Point
# ============================================================================

if __name__ == "__main__":
    # Check if running in interactive mode or demo mode
    if len(sys.argv) > 1 and sys.argv[1] == "--interactive":
        interactive_mode()
    else:
        # Run demo mode
        main()
