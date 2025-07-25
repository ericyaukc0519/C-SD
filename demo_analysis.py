#!/usr/bin/env python3
"""
Hong Kong Industry Analysis Framework - Demo Script
Demonstrates all features and capabilities of the analysis framework
"""

import os
import json
import sqlite3
from datetime import datetime
from pathlib import Path

def print_banner():
    """Print demo banner"""
    print("🌟" * 60)
    print("🏢 HONG KONG INDUSTRY ANALYSIS FRAMEWORK - DEMO")
    print("🌟" * 60)
    print("📊 Medical R&D and Patent Brokerage Industry Analysis")
    print("🤖 AI-Powered Classification | 📈 Market Gap Analysis | 🎬 Auto PPT Generation")
    print("🌟" * 60)

def demonstrate_framework_capabilities():
    """Demonstrate all framework capabilities"""
    print("\n🎯 FRAMEWORK CAPABILITIES OVERVIEW")
    print("=" * 50)
    
    capabilities = [
        "🔍 Web Scraping: Companies Registry, HKTDC, IP Department",
        "🧠 AI Classification: NLP-powered industry categorization",
        "📊 Data Analysis: Market gaps, barriers, and opportunities",
        "📈 Visualizations: Professional charts and graphs",
        "🗄️ Database Storage: SQLite with company information",
        "📊 Multi-format Export: JSON, Excel, PowerPoint",
        "🎬 Auto PPT Generation: Professional presentation slides",
        "🔧 Configurable: Customizable keywords and classifications"
    ]
    
    for i, capability in enumerate(capabilities, 1):
        print(f"{i}. {capability}")

def analyze_results(json_file):
    """Analyze and display the results"""
    print(f"\n📋 ANALYSIS RESULTS FROM: {json_file}")
    print("=" * 50)
    
    with open(json_file, 'r') as f:
        results = json.load(f)
    
    # Summary Statistics
    summary = results['summary']
    print(f"📊 SUMMARY STATISTICS:")
    print(f"   • Total Companies Analyzed: {summary['total_companies_analyzed']}")
    print(f"   • Medical R&D Companies: {summary['medical_rd_companies']}")
    print(f"   • Patent Brokerage Companies: {summary['patent_brokerage_companies']}")
    print(f"   • Analysis Date: {summary['analysis_date']}")
    
    # Company Classifications
    print(f"\n🏢 COMPANY CLASSIFICATIONS:")
    
    if results['company_listings']['medical_rd']:
        print(f"   📈 MEDICAL R&D COMPANIES:")
        for company in results['company_listings']['medical_rd']:
            print(f"      • {company['name']}")
            print(f"        Nature: {company['business_nature']}")
            print(f"        Location: {company['address']}")
            print(f"        Confidence: {company['confidence_score']:.1%}")
            print(f"        Classification: ISIC {company['isic_code']} | HSIC {company['hsic_code']}")
    
    if results['company_listings']['patent_brokerage']:
        print(f"   ⚖️ PATENT BROKERAGE COMPANIES:")
        for company in results['company_listings']['patent_brokerage']:
            print(f"      • {company['name']}")
            print(f"        Nature: {company['business_nature']}")
            print(f"        Location: {company['address']}")
    else:
        print(f"   ⚖️ PATENT BROKERAGE COMPANIES: None identified in sample data")
    
    # Market Analysis
    print(f"\n🚧 MARKET BARRIERS IDENTIFIED:")
    barriers = results['market_analysis']['barriers']
    
    print(f"   📈 Medical R&D Barriers:")
    for barrier in barriers['medical_rd']:
        print(f"      • {barrier}")
    
    print(f"   ⚖️ Patent Brokerage Barriers:")
    for barrier in barriers['patent_brokerage']:
        print(f"      • {barrier}")
    
    # Opportunities
    print(f"\n🌟 DEVELOPMENT OPPORTUNITIES:")
    opportunities = results['market_analysis']['opportunities']
    
    print(f"   📈 Medical R&D Opportunities:")
    for opp in opportunities['medical_rd']:
        print(f"      • {opp}")
    
    print(f"   ⚖️ Patent Brokerage Opportunities:")
    for opp in opportunities['patent_brokerage']:
        print(f"      • {opp}")
    
    # Key Findings
    print(f"\n🔍 KEY FINDINGS:")
    findings = results['key_findings']
    print(f"   • Medical R&D: {findings['medical_rd']}")
    print(f"   • Patent Brokerage: {findings['patent_brokerage']}")
    print(f"   • Development Potential: {findings['development_potential']}")
    
    print(f"\n🚨 CRITICAL CLASSIFICATION GAPS:")
    for gap in findings['critical_gaps']:
        print(f"   • {gap}")

def display_classification_framework(results):
    """Display the industry classification framework"""
    print(f"\n📋 INDUSTRY CLASSIFICATION FRAMEWORK (PPT)")
    print("=" * 50)
    
    framework = results['classification_framework']
    
    print(f"I. MEDICAL R&D INDUSTRY")
    medical = framework['medical_rd']
    print(f"   a. ISIC: {medical['isic_code']} ({medical['description']})")
    print(f"   b. HSIC Gap: {medical['hsic_gap']}")
    print(f"   c. Proposed Framework:")
    for item in medical['proposed_framework']:
        print(f"      - {item}")
    
    print(f"\nII. PATENT BROKERAGE")
    patent = framework['patent_brokerage']
    print(f"   a. ISIC: {patent['isic_code']} ({patent['description']})")
    print(f"   b. HSIC Gap: {patent['hsic_gap']}")
    print(f"   c. Proposed Framework:")
    for item in patent['proposed_framework']:
        print(f"      - {item}")

def check_database():
    """Check the generated SQLite database"""
    print(f"\n🗄️ DATABASE ANALYSIS")
    print("=" * 50)
    
    if not os.path.exists('industry_analysis.db'):
        print("❌ Database not found. Run the analysis first.")
        return
    
    conn = sqlite3.connect('industry_analysis.db')
    cursor = conn.cursor()
    
    # Check companies table
    cursor.execute("SELECT COUNT(*) FROM companies")
    company_count = cursor.fetchone()[0]
    print(f"📊 Companies in database: {company_count}")
    
    # Show sample companies
    cursor.execute("""
        SELECT name, industry_classification, confidence_score, isic_code, hsic_code 
        FROM companies 
        ORDER BY confidence_score DESC 
        LIMIT 5
    """)
    
    companies = cursor.fetchall()
    print(f"\n🏢 Top Companies by Confidence Score:")
    for company in companies:
        name, industry, confidence, isic, hsic = company
        print(f"   • {name}")
        print(f"     Industry: {industry} | Confidence: {confidence:.1%}")
        print(f"     Codes: ISIC {isic} | HSIC {hsic}")
    
    conn.close()

def check_output_files():
    """Check all generated output files"""
    print(f"\n📁 OUTPUT FILES STATUS")
    print("=" * 50)
    
    # Find the latest files
    json_files = list(Path('.').glob('industry_analysis_results_*.json'))
    excel_files = list(Path('.').glob('industry_analysis_results_*.xlsx'))
    ppt_files = list(Path('.').glob('HK_Industry_Analysis_*.pptx'))
    
    # Sort by modification time (newest first)
    json_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    excel_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    ppt_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    print(f"📊 Generated Files:")
    
    if json_files:
        latest_json = json_files[0]
        size_kb = latest_json.stat().st_size / 1024
        print(f"   ✅ JSON Results: {latest_json.name} ({size_kb:.1f} KB)")
    
    if excel_files:
        latest_excel = excel_files[0]
        size_kb = latest_excel.stat().st_size / 1024
        print(f"   ✅ Excel Report: {latest_excel.name} ({size_kb:.1f} KB)")
    
    if ppt_files:
        latest_ppt = ppt_files[0]
        size_kb = latest_ppt.stat().st_size / 1024
        print(f"   ✅ PowerPoint: {latest_ppt.name} ({size_kb:.1f} KB)")
    
    # Check charts
    charts_dir = Path('charts')
    if charts_dir.exists():
        chart_files = list(charts_dir.glob('*.png'))
        print(f"   ✅ Charts: {len(chart_files)} files in charts/ directory")
        for chart in chart_files:
            size_kb = chart.stat().st_size / 1024
            print(f"      • {chart.name} ({size_kb:.1f} KB)")
    
    # Check database
    db_file = Path('industry_analysis.db')
    if db_file.exists():
        size_kb = db_file.stat().st_size / 1024
        print(f"   ✅ Database: {db_file.name} ({size_kb:.1f} KB)")
    
    # Check logs
    log_file = Path('industry_analysis.log')
    if log_file.exists():
        size_kb = log_file.stat().st_size / 1024
        print(f"   ✅ Logs: {log_file.name} ({size_kb:.1f} KB)")

def demonstrate_use_cases():
    """Demonstrate practical use cases"""
    print(f"\n🎯 PRACTICAL USE CASES")
    print("=" * 50)
    
    use_cases = [
        {
            "title": "🏛️ Government Policy Making",
            "description": "Identify industry gaps for new HSIC classification codes",
            "benefits": ["Evidence-based policy decisions", "Industry development planning", "Regulatory framework updates"]
        },
        {
            "title": "💼 Investment Analysis",
            "description": "Find emerging companies in high-growth sectors",
            "benefits": ["Deal sourcing for VCs", "Market entry strategies", "Competitive intelligence"]
        },
        {
            "title": "🎓 Academic Research",
            "description": "Study Hong Kong's innovation ecosystem evolution",
            "benefits": ["Industry trend analysis", "Academic publications", "Grant applications"]
        },
        {
            "title": "🏢 Corporate Strategy",
            "description": "Identify partnership and acquisition targets",
            "benefits": ["Strategic planning", "M&A target identification", "Market positioning"]
        },
        {
            "title": "🌏 Regional Comparison",
            "description": "Compare HK with Singapore and other regional hubs",
            "benefits": ["Benchmarking studies", "Competitiveness analysis", "Policy recommendations"]
        }
    ]
    
    for i, use_case in enumerate(use_cases, 1):
        print(f"{i}. {use_case['title']}")
        print(f"   {use_case['description']}")
        print(f"   Benefits:")
        for benefit in use_case['benefits']:
            print(f"     • {benefit}")
        print()

def show_technical_architecture():
    """Show the technical architecture"""
    print(f"\n🏗️ TECHNICAL ARCHITECTURE")
    print("=" * 50)
    
    architecture = """
    📊 Hong Kong Industry Analysis Framework
    ├── 🔍 Data Collection Layer
    │   ├── Companies Registry Scraper (BeautifulSoup + Requests)
    │   ├── HKTDC Directory API Integration
    │   └── IP Department Database Connector
    │
    ├── 🧠 Processing Layer
    │   ├── AI Industry Classifier (NLTK + scikit-learn)
    │   ├── ISIC/HSIC Code Mapper
    │   └── Data Validation & Cleaning Engine
    │
    ├── 📈 Analysis Layer
    │   ├── Market Gap Analyzer
    │   ├── Statistical Trend Engine
    │   └── Visualization Generator (Matplotlib + Seaborn)
    │
    ├── 🗄️ Storage Layer
    │   ├── SQLite Database
    │   ├── JSON Export
    │   └── Excel Workbooks
    │
    └── 📋 Presentation Layer
        ├── PowerPoint Generator (python-pptx)
        ├── Executive Dashboard
        └── Report Templates
    """
    
    print(architecture)
    
    print(f"\n🔧 KEY TECHNOLOGIES:")
    technologies = [
        "🐍 Python 3.8+ with modern libraries",
        "🔍 Web Scraping: Requests + BeautifulSoup + Selenium",
        "🧠 NLP: NLTK + scikit-learn for text classification",
        "📊 Data Analysis: Pandas + NumPy for data processing",
        "📈 Visualization: Matplotlib + Seaborn for charts",
        "🗄️ Database: SQLite for local storage",
        "📋 Reporting: python-pptx + openpyxl for output",
        "⚡ Performance: Concurrent processing & caching"
    ]
    
    for tech in technologies:
        print(f"   {tech}")

def main():
    """Main demo function"""
    print_banner()
    
    # Check if analysis has been run
    json_files = list(Path('.').glob('industry_analysis_results_*.json'))
    
    if not json_files:
        print("\n❗ No analysis results found. Please run the analysis first:")
        print("   python3 industry_analysis_framework.py")
        return
    
    # Use the latest results file
    latest_json = max(json_files, key=lambda x: x.stat().st_mtime)
    
    with open(latest_json, 'r') as f:
        results = json.load(f)
    
    # Run all demonstrations
    demonstrate_framework_capabilities()
    analyze_results(latest_json)
    display_classification_framework(results)
    check_database()
    check_output_files()
    demonstrate_use_cases()
    show_technical_architecture()
    
    print(f"\n🎉 DEMO COMPLETED SUCCESSFULLY!")
    print("=" * 50)
    print(f"📊 Your Hong Kong Industry Analysis Framework is ready for:")
    print(f"   • Real-world industry analysis")
    print(f"   • Government policy research")
    print(f"   • Investment decision support")
    print(f"   • Academic research projects")
    print(f"   • Corporate strategic planning")
    print(f"\n🚀 Next Steps:")
    print(f"   1. Customize keyword lists for your specific industries")
    print(f"   2. Integrate real API endpoints for live data")
    print(f"   3. Add more data sources and analysis modules")
    print(f"   4. Deploy as a web service or scheduled analysis")
    print("🌟" * 60)

if __name__ == "__main__":
    main()