#!/usr/bin/env python3
"""
Example Usage Patterns for Report Summarizer

This script demonstrates various ways to use the ReportSummarizer class
in different scenarios.
"""

from venv.report_summarizer import ReportSummarizer
import os


def example_1_basic_usage():
    """
    Example 1: Basic usage with text input
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 1: Basic Text Summarization")
    print("=" * 70)
    
    # Initialize summarizer
    summarizer = ReportSummarizer()
    
    # Sample report text
    report = """
    Quarterly Performance Review - Q1 2026
    
    Sales Performance:
    - Total revenue reached $2.5M, exceeding target by 15%
    - Customer acquisition cost decreased by 8%
    - Repeat customer rate improved to 68%
    
    Operations:
    - On-time delivery improved to 96%
    - Employee headcount increased by 12%
    - Training programs completed by 85% of staff
    
    Challenges:
    - Supply chain delays affected 20% of orders
    - Market competition intensified in three sectors
    - Cloud infrastructure costs increased 22%
    
    Outlook:
    - Q2 projections show 18% growth potential
    - Three new product launches planned
    - Expansion into two new geographic markets
    """
    
    try:
        summary = summarizer.summarize_from_text(report, max_bullets=6)
        print(summary)
    except Exception as e:
        print(f"Error: {e}")


def example_2_custom_bullet_count():
    """
    Example 2: Customize the number of bullet points
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 2: Custom Bullet Point Count")
    print("=" * 70)
    
    summarizer = ReportSummarizer()
    
    report = """
    Annual Risk Assessment Report
    
    Identified Risks:
    1. Cybersecurity threats showing 34% increase YoY
    2. Regulatory compliance issues in three regions
    3. Supply chain vulnerability in Asia-Pacific
    4. Currency fluctuation impacting margins by 2-3%
    5. Talent retention challenges in tech roles
    6. Climate-related operational disruptions
    7. Market consolidation reducing competitive space
    8. Technology debt accumulation
    9. Third-party vendor dependency risks
    10. Data privacy regulation changes
    
    Mitigation Strategies:
    - Enhanced security protocols and staffing
    - Compliance team expansion plan
    - Supplier diversification initiatives
    - Hedging strategies for FX exposure
    - Competitive compensation review
    - Business continuity improvements
    """
    
    try:
        # Summary with only 5 bullets
        print("\nSummary with 5 bullets:")
        summary = summarizer.summarize_from_text(report, max_bullets=5)
        print(summary)
        
        # Summary with 10 bullets
        print("\nSummary with 10 bullets:")
        summary = summarizer.summarize_from_text(report, max_bullets=10)
        print(summary)
    except Exception as e:
        print(f"Error: {e}")


def example_3_file_input():
    """
    Example 3: Reading from a file
    
    Note: This example requires an actual file to exist.
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 3: File Input (Demonstration)")
    print("=" * 70)
    
    summarizer = ReportSummarizer()
    
    # Create a temporary test file
    test_file = "/tmp/sample_report.txt"
    
    # Write sample content
    sample_content = """
    Market Analysis Report 2026
    
    Executive Overview:
    Global markets showed resilience despite macroeconomic headwinds. 
    Technology and healthcare sectors outperformed with average growth of 15%,
    while traditional retail faced continued pressure from digital disruption.
    
    Regional Performance:
    - North America: Stable growth at 5%, supported by strong consumer sentiment
    - Europe: Mixed results with 2% growth, impacted by energy cost pressures
    - Asia-Pacific: Strongest performer at 12%, driven by recovery and digital adoption
    - Emerging Markets: Volatile performance ranging from -3% to +8%
    
    Key Trends:
    - ESG investing grew 45% YoY
    - AI/ML adoption accelerating across sectors
    - Supply chain regionalization reducing globalization benefits
    - Energy transition creating both risks and opportunities
    - Digital payment adoption reached 67% in developed markets
    
    Forecast:
    - 2026 overall growth expected at 3-4%
    - Continued tech sector outperformance
    - Potential market correction if interest rates remain elevated
    - Geopolitical tensions adding uncertainty to outlook
    """
    
    try:
        # Write sample file
        with open(test_file, "w") as f:
            f.write(sample_content)
        
        print(f"Created test file: {test_file}")
        
        # Summarize from file
        summary = summarizer.summarize_from_file(test_file, max_bullets=7)
        print(summary)
        
        # Clean up
        os.remove(test_file)
        print(f"\nCleaned up test file")
    except Exception as e:
        print(f"Error: {e}")


def example_4_different_models():
    """
    Example 4: Using different AI models
    
    Note: Different models have different capabilities and costs
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 4: Different AI Models (Demonstration)")
    print("=" * 70)
    
    models_info = {
        "gpt-3.5-turbo": "Fast and cost-effective (recommended for most use cases)",
        "gpt-4": "More accurate and sophisticated (higher cost)",
        "gpt-4-turbo-preview": "Balanced performance and cost"
    }
    
    print("Available models:")
    for model, description in models_info.items():
        print(f"  - {model}: {description}")
    
    # Example of creating summarizer with different model
    try:
        summarizer_gpt4 = ReportSummarizer(model="gpt-4")
        print("\nInitialized with GPT-4 model (higher accuracy, higher cost)")
    except Exception as e:
        print(f"Error: {e}")


def example_5_error_handling():
    """
    Example 5: Proper error handling
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 5: Error Handling")
    print("=" * 70)
    
    summarizer = ReportSummarizer()
    
    # Test 1: Empty content
    print("\nTest 1: Empty content handling")
    try:
        summary = summarizer.summarize_from_text("")
    except ValueError as e:
        print(f"✓ Caught error: {e}")
    
    # Test 2: Non-existent file
    print("\nTest 2: Non-existent file handling")
    try:
        summary = summarizer.summarize_from_file("/nonexistent/file.txt")
    except FileNotFoundError as e:
        print(f"✓ Caught error: {e}")
    
    # Test 3: Unsupported file format
    print("\nTest 3: Unsupported file format handling")
    # Create a dummy file with unsupported extension
    dummy_file = "/tmp/test.xyz"
    with open(dummy_file, "w") as f:
        f.write("test content")
    
    try:
        summary = summarizer.summarize_from_file(dummy_file)
    except ValueError as e:
        print(f"✓ Caught error: {e}")
    
    # Clean up
    os.remove(dummy_file)


def example_6_batch_processing():
    """
    Example 6: Processing multiple reports
    """
    print("\n" + "=" * 70)
    print("EXAMPLE 6: Batch Processing Multiple Reports")
    print("=" * 70)
    
    summarizer = ReportSummarizer()
    
    reports = {
        "Q1_Report": """
            Q1 2026 Results: Revenue up 12%, Costs up 8%.
            Key metrics: Customer satisfaction 92%, Churn rate 2.1%.
            Planned initiatives for Q2: Product launch, market expansion.
        """,
        "Q2_Report": """
            Q2 2026 Results: Revenue up 18%, Costs down 3%.
            New product line contributed 35% to revenue growth.
            Expanded operations to two new countries successfully.
        """,
        "Q3_Report": """
            Q3 2026 Results: Revenue flat due to market conditions.
            Cost optimization initiatives yielded 5% savings.
            Invested heavily in R&D for future product pipeline.
        """
    }
    
    try:
        for report_name, content in reports.items():
            print(f"\n{report_name} Summary:")
            print("-" * 50)
            summary = summarizer.summarize_from_text(content, max_bullets=4)
            print(summary)
    except Exception as e:
        print(f"Error: {e}")


# ============================================================================
# Main Execution
# ============================================================================

def main():
    """
    Run all examples
    """
    print("\n")
    print("*" * 70)
    print("* REPORT SUMMARIZER - USAGE EXAMPLES")
    print("*" * 70)
    
    try:
        example_1_basic_usage()
        example_2_custom_bullet_count()
        example_3_file_input()
        example_4_different_models()
        example_5_error_handling()
        example_6_batch_processing()
        
        print("\n" + "*" * 70)
        print("* All examples completed successfully!")
        print("*" * 70 + "\n")
    except Exception as e:
        print(f"\nError running examples: {e}")


if __name__ == "__main__":
    main()
