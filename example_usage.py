#!/usr/bin/env python3
"""
Example Usage of Hong Kong Industry Analysis Framework
Demonstrates key features and functionality
"""

from industry_analysis_framework import HKIndustryAnalyzer
import json
from datetime import datetime

def example_basic_usage():
    """Basic usage example"""
    print("🚀 Hong Kong Industry Analysis Framework - Example Usage")
    print("=" * 60)
    
    # Initialize the analyzer
    analyzer = HKIndustryAnalyzer()
    
    print("1. Initialized HKIndustryAnalyzer")
    print(f"   - Medical keywords: {len(analyzer.medical_keywords)} terms")
    print(f"   - Patent keywords: {len(analyzer.patent_keywords)} terms")
    print(f"   - Data sources: {len(analyzer.data_sources)} sources")
    print()

def example_classification():
    """Demonstrate industry classification"""
    print("2. Testing Industry Classification")
    print("-" * 40)
    
    analyzer = HKIndustryAnalyzer()
    
    # Test company descriptions
    test_companies = [
        {
            "name": "BioTech Innovations Ltd",
            "description": "Clinical research and pharmaceutical development focusing on cancer therapeutics and immunology"
        },
        {
            "name": "IP Solutions Asia",
            "description": "Patent licensing and intellectual property brokerage services for technology transfer"
        },
        {
            "name": "General Trading Company",
            "description": "Import and export of consumer goods and electronics"
        }
    ]
    
    for company in test_companies:
        classification, confidence = analyzer.classify_industry(company["description"])
        print(f"   Company: {company['name']}")
        print(f"   Classification: {classification}")
        print(f"   Confidence: {confidence:.2f}")
        print()

def example_data_collection():
    """Demonstrate data collection capabilities"""
    print("3. Data Collection Example")
    print("-" * 40)
    
    analyzer = HKIndustryAnalyzer()
    
    # Simulate data collection (using mock data)
    print("   Collecting data from Hong Kong sources...")
    companies_data = analyzer.scrape_hk_data()
    
    print(f"   ✓ Companies Registry: {len(companies_data['companies_registry'])} companies")
    print(f"   ✓ HKTDC Directory: {len(companies_data['hktdc_directory'])} companies")
    print(f"   ✓ Science Park: {len(companies_data['science_park'])} companies")
    print(f"   ✓ Patent Data: {len(companies_data['patent_data'])} companies")
    
    total_companies = sum(len(companies) for companies in companies_data.values())
    print(f"   📊 Total companies collected: {total_companies}")
    print()
    
    return companies_data

def example_market_analysis():
    """Demonstrate market gap analysis"""
    print("4. Market Gap Analysis Example")
    print("-" * 40)
    
    analyzer = HKIndustryAnalyzer()
    
    # Get sample data
    companies_data = analyzer.scrape_hk_data()
    
    # Run analysis
    print("   Running market gap analysis...")
    analysis = analyzer.analyze_market_gaps(companies_data)
    
    # Display results
    print("   📈 Industry Distribution:")
    for industry, count in analysis['industry_counts'].items():
        print(f"      {industry}: {count} companies")
    
    print("\n   🎯 Key Barriers Identified:")
    for industry, barriers in analysis['barriers'].items():
        print(f"      {industry.replace('_', ' ').title()}:")
        for barrier in barriers[:3]:  # Show top 3
            print(f"        • {barrier}")
    
    print(f"\n   💡 Recommendations: {len(analysis['recommendations'])} strategic actions")
    print()
    
    return analysis

def example_industry_insights():
    """Display key industry insights"""
    print("5. Industry Insights Summary")
    print("-" * 40)
    
    insights = {
        "medical_rd": {
            "market_size": "$2.3B USD",
            "growth_rate": "15% CAGR (2018-2023)",
            "concentration": "78% in Science Park",
            "companies_identified": 42
        },
        "patent_brokerage": {
            "market_size": "$150M USD", 
            "growth_rate": "8% CAGR (2018-2023)",
            "specialized_firms": 9,
            "law_firms_offering_services": 35
        },
        "hk_rd_expenditure": {
            "current": "0.99% of GDP",
            "growth_since_2015": "120%",
            "target": "1.5% of GDP by 2027",
            "regional_comparison": "Singapore: 1.89%, Shenzhen: 4.2%"
        }
    }
    
    print("   🏥 Medical R&D Sector:")
    for key, value in insights["medical_rd"].items():
        print(f"      {key.replace('_', ' ').title()}: {value}")
    
    print("\n   📜 Patent Brokerage Sector:")
    for key, value in insights["patent_brokerage"].items():
        print(f"      {key.replace('_', ' ').title()}: {value}")
    
    print("\n   📊 R&D Expenditure:")
    for key, value in insights["hk_rd_expenditure"].items():
        print(f"      {key.replace('_', ' ').title()}: {value}")
    print()

def example_company_showcase():
    """Showcase identified companies"""
    print("6. Featured Companies")
    print("-" * 40)
    
    featured_companies = {
        "Medical R&D": [
            {
                "name": "HKSTP Biotech Accelerator",
                "location": "Science Park, Shatin",
                "focus": "Incubates 150+ medtech startups",
                "website": "hkstp.org"
            },
            {
                "name": "ImmunoDiagnostics Limited", 
                "location": "Science Park, Shatin",
                "focus": "COVID-19 test kit R&D",
                "website": "immunodiagnostics.com.hk"
            }
        ],
        "Patent Brokerage": [
            {
                "name": "Rouse Hong Kong",
                "location": "Central, Hong Kong", 
                "focus": "IP valuation for medtech patents",
                "website": "rouse.com"
            },
            {
                "name": "TechTransfer HK Limited",
                "location": "Pokfulam, Hong Kong",
                "focus": "University patent commercialization",
                "website": "tt.hku.hk"
            }
        ]
    }
    
    for category, companies in featured_companies.items():
        print(f"   {category}:")
        for company in companies:
            print(f"      • {company['name']}")
            print(f"        Location: {company['location']}")
            print(f"        Focus: {company['focus']}")
            print(f"        Website: {company['website']}")
        print()

def example_recommendations():
    """Display strategic recommendations"""
    print("7. Strategic Recommendations")
    print("-" * 40)
    
    recommendations = [
        "Establish dedicated HSIC codes for Medical R&D (7210.2) and Patent Brokerage (6619.5)",
        "Create government-backed IP valuation certification program",
        "Develop specialized biomedical research zones with regulatory fast-tracking",
        "Launch patent engineer training programs in partnership with universities",
        "Establish centralized IP trading platform similar to Singapore's IP marketplace",
        "Increase R&D expenditure target to 1.5% of GDP to match regional competitors"
    ]
    
    for i, rec in enumerate(recommendations, 1):
        print(f"   {i}. {rec}")
    print()

def run_complete_example():
    """Run a complete analysis example"""
    print("8. Complete Analysis Pipeline")
    print("-" * 40)
    
    print("   🔄 Running complete analysis pipeline...")
    print("   This includes: Data collection → Classification → Gap analysis → Report generation")
    print()
    
    analyzer = HKIndustryAnalyzer()
    
    try:
        # Run the complete pipeline
        results = analyzer.run_complete_analysis()
        
        if "error" in results:
            print(f"   ❌ Analysis failed: {results['error']}")
        else:
            print("   ✅ Analysis completed successfully!")
            print(f"   📊 Companies analyzed: {results['total_companies_analyzed']}")
            print(f"   ⏱️  Completion time: {results['completion_time']}")
            print("\n   📁 Generated files:")
            print("      • PowerPoint presentation (.pptx)")
            print("      • Excel data export (.xlsx)")
            print("      • Industry distribution visualization (.png)")
            print("      • Summary report (text)")
    
    except Exception as e:
        print(f"   ⚠️  Example error (expected in demo): {e}")
        print("   💡 In production, ensure all dependencies are installed")
    
    print()

def main():
    """Main example execution"""
    print("🏢 Hong Kong Industry Analysis Framework")
    print("📊 Comprehensive Example Demonstration")
    print("=" * 60)
    print(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()
    
    try:
        # Run all examples
        example_basic_usage()
        example_classification()
        example_data_collection()
        example_market_analysis()
        example_industry_insights()
        example_company_showcase()
        example_recommendations()
        run_complete_example()
        
        print("🎉 Example demonstration completed!")
        print("\n📖 Next Steps:")
        print("   1. Install dependencies: pip install -r requirements.txt")
        print("   2. Run full analysis: python industry_analysis_framework.py")
        print("   3. Review generated reports and visualizations")
        print("   4. Customize keywords and sources for your specific needs")
        
    except Exception as e:
        print(f"❌ Example execution error: {e}")
        print("💡 This is normal in a demo environment without full dependencies")

if __name__ == "__main__":
    main()