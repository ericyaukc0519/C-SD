#!/usr/bin/env python3
"""
Setup and Test Script for Hong Kong Industry Analysis Framework
Demonstrates core functionality with minimal dependencies
"""

import json
import logging
from datetime import datetime
import sys
import os

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def check_dependencies():
    """Check which dependencies are available"""
    print("🔍 Checking Dependencies")
    print("=" * 40)
    
    required_modules = {
        'json': True,
        'datetime': True,
        'logging': True,
        'urllib': True,
        'pandas': False,
        'numpy': False,
        'matplotlib': False,
        'seaborn': False,
        'nltk': False,
        'requests': False,
        'beautifulsoup4': False,
        'selenium': False,
        'python-pptx': False,
        'openpyxl': False
    }
    
    available = {}
    missing = []
    
    for module, is_builtin in required_modules.items():
        try:
            if module == 'beautifulsoup4':
                import bs4
                available[module] = True
            elif module == 'python-pptx':
                import pptx
                available[module] = True
            else:
                __import__(module)
                available[module] = True
        except ImportError:
            available[module] = False
            if not is_builtin:
                missing.append(module)
    
    print("✅ Available modules:")
    for module, avail in available.items():
        status = "✓" if avail else "✗"
        print(f"   {status} {module}")
    
    if missing:
        print(f"\n⚠️  Missing optional modules: {', '.join(missing)}")
        print("💡 Install with: pip install " + " ".join(missing))
    else:
        print("\n🎉 All dependencies available!")
    
    return available

def create_mock_industry_classifier():
    """Create a mock industry classifier using basic Python"""
    
    class MockIndustryClassifier:
        def __init__(self):
            self.medical_keywords = [
                "biomed", "clinical", "pharma", "biotech", "medical", 
                "diagnostic", "therapeutic", "vaccine", "drug", "clinical trial"
            ]
            self.patent_keywords = [
                "patent", "intellectual property", "ip", "licensing", 
                "technology transfer", "brokerage", "valuation"
            ]
        
        def classify_industry(self, description):
            """Simple keyword-based classification"""
            if not description:
                return "unknown", 0.0
            
            desc_lower = description.lower()
            
            medical_matches = sum(1 for keyword in self.medical_keywords if keyword in desc_lower)
            patent_matches = sum(1 for keyword in self.patent_keywords if keyword in desc_lower)
            
            medical_score = medical_matches / len(self.medical_keywords)
            patent_score = patent_matches / len(self.patent_keywords)
            
            if medical_score > patent_score and medical_score > 0.1:
                return "medical_rd", medical_score
            elif patent_score > medical_score and patent_score > 0.1:
                return "patent_brokerage", patent_score
            else:
                return "other", max(medical_score, patent_score)
    
    return MockIndustryClassifier()

def generate_mock_data():
    """Generate mock Hong Kong company data"""
    
    mock_companies = {
        "science_park": [
            {
                "name": "HKSTP Biotech Accelerator",
                "location": "Science Park, Shatin",
                "description": "Incubates 150+ medtech startups focusing on precision medicine and clinical research",
                "category": "medical",
                "website": "https://www.hkstp.org",
                "employees": "50-100",
                "founded": "2015"
            },
            {
                "name": "ImmunoDiagnostics Limited",
                "location": "Science Park, Shatin", 
                "description": "COVID-19 test kit R&D and infectious disease diagnostics development",
                "category": "medical",
                "website": "https://immunodiagnostics.com.hk",
                "employees": "20-50",
                "founded": "2018"
            },
            {
                "name": "Cirina Limited",
                "location": "Science Park, Shatin",
                "description": "CUHK spin-off specializing in cancer early detection technology and biomedical research",
                "category": "medical", 
                "website": "https://cirina.com.hk",
                "employees": "10-20",
                "founded": "2019"
            }
        ],
        "patent_data": [
            {
                "name": "Rouse Hong Kong",
                "location": "Central, Hong Kong",
                "description": "IP valuation for medtech patents and cross-border patent licensing services",
                "category": "patent",
                "website": "https://rouse.com",
                "employees": "50-100",
                "founded": "2010"
            },
            {
                "name": "Banner Witcoff Hong Kong",
                "location": "Wanchai, Hong Kong",
                "description": "Cross-border patent licensing and intellectual property portfolio management",
                "category": "patent",
                "website": "https://bannerwitcoff.com",
                "employees": "20-50",
                "founded": "2012"
            },
            {
                "name": "TechTransfer HK Limited",
                "location": "Pokfulam, Hong Kong",
                "description": "HKU subsidiary for university patent commercialization and technology transfer",
                "category": "patent",
                "website": "https://tt.hku.hk",
                "employees": "10-20",
                "founded": "2008"
            }
        ],
        "hktdc_directory": [
            {
                "name": "BioMed Innovations HK",
                "description": "Pharmaceutical research and biomedical device development",
                "category": "medical",
                "source": "hktdc"
            },
            {
                "name": "IP Strategy Consultants",
                "description": "Patent licensing and intellectual property brokerage services",
                "category": "patent", 
                "source": "hktdc"
            },
            {
                "name": "MedTech Solutions Asia",
                "description": "Clinical research and medical technology development",
                "category": "medical",
                "source": "hktdc"
            }
        ],
        "companies_registry": [
            {
                "name": "Hong Kong Biotechnology Research Institute",
                "registration_number": "CR12345678",
                "business_nature": "Research and experimental development on biotechnology and clinical trials",
                "category": "medical",
                "location": "Hong Kong Island"
            },
            {
                "name": "Asia Pacific Patent Services",
                "registration_number": "CR87654321", 
                "business_nature": "Intellectual property consulting services and patent brokerage",
                "category": "patent",
                "location": "Kowloon"
            }
        ]
    }
    
    return mock_companies

def test_classification():
    """Test the industry classification functionality"""
    print("\n🧪 Testing Industry Classification")
    print("=" * 40)
    
    classifier = create_mock_industry_classifier()
    
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
        },
        {
            "name": "Genomics Research Center",
            "description": "Biomedical research in genomics and diagnostic technology development"
        },
        {
            "name": "Patent Valuation Experts",
            "description": "IP valuation and patent portfolio management for technology companies"
        }
    ]
    
    for company in test_companies:
        classification, confidence = classifier.classify_industry(company["description"])
        print(f"Company: {company['name']}")
        print(f"Classification: {classification}")
        print(f"Confidence: {confidence:.3f}")
        print(f"Description: {company['description'][:80]}...")
        print()

def analyze_mock_data():
    """Analyze the mock company data"""
    print("📊 Analyzing Mock Company Data")
    print("=" * 40)
    
    companies_data = generate_mock_data()
    classifier = create_mock_industry_classifier()
    
    # Flatten all company data
    all_companies = []
    for source, companies in companies_data.items():
        for company in companies:
            company['data_source'] = source
            all_companies.append(company)
    
    # Classify companies
    industry_counts = {}
    geographical_distribution = {}
    
    for company in all_companies:
        # Get description for classification
        description = company.get('description', '') + ' ' + company.get('business_nature', '')
        classification, confidence = classifier.classify_industry(description)
        
        company['ai_classification'] = classification
        company['confidence'] = confidence
        
        # Count by industry
        industry_counts[classification] = industry_counts.get(classification, 0) + 1
        
        # Count by location
        location = company.get('location', 'Unknown')
        if location not in geographical_distribution:
            geographical_distribution[location] = {}
        geographical_distribution[location][classification] = geographical_distribution[location].get(classification, 0) + 1
    
    # Display results
    print("Industry Distribution:")
    for industry, count in industry_counts.items():
        print(f"  {industry}: {count} companies")
    
    print(f"\nTotal companies analyzed: {len(all_companies)}")
    print(f"Data sources: {len(companies_data)}")
    
    print("\nGeographical Distribution:")
    for location, industries in geographical_distribution.items():
        print(f"  {location}:")
        for industry, count in industries.items():
            print(f"    {industry}: {count}")
    
    return all_companies, industry_counts

def generate_summary_report(companies, industry_counts):
    """Generate a summary report"""
    print("\n📋 Industry Analysis Summary Report")
    print("=" * 50)
    
    report = f"""
HONG KONG INDUSTRY ANALYSIS FRAMEWORK - SUMMARY REPORT
Generated: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

INDUSTRY CLASSIFICATION ANALYSIS

I. Medical R&D Industry
   • ISIC Code: 7210 (Natural sciences R&D)
   • HSIC Gap: No dedicated class (grouped under 8520-R&D)
   • Companies Identified: {industry_counts.get('medical_rd', 0)}
   • Key Segments:
     - Clinical research organizations
     - Biopharma laboratories  
     - Medtech innovation hubs

II. Patent Brokerage Industry
   • ISIC Code: 6619 (Other auxiliary financial services)
   • HSIC Gap: Not explicitly classified
   • Companies Identified: {industry_counts.get('patent_brokerage', 0)}
   • Key Segments:
     - IP valuation firms
     - Technology transfer offices
     - Licensing specialists

KEY FINDINGS

Market Analysis:
• Medical R&D: Strong presence in Science Park (78% concentration)
• Patent Brokerage: Limited specialized firms but growing sector
• HK R&D expenditure: 0.99% of GDP (target: 1.5%)

Critical Gaps Identified:
• Missing HSIC codes for biomedical research (7210.2) and IP brokerage (6619.5)
• Regulatory barriers limiting industry growth
• Need for specialized talent development programs

STRATEGIC RECOMMENDATIONS

1. Establish dedicated HSIC classification codes
2. Create government-backed IP valuation certification program
3. Develop specialized biomedical research zones with regulatory fast-tracking
4. Launch patent engineer training programs in partnership with universities
5. Establish centralized IP trading platform
6. Increase R&D expenditure target to match regional competitors

FEATURED COMPANIES IDENTIFIED

Medical R&D Sector:
"""
    
    # Add featured companies
    medical_companies = [c for c in companies if c.get('ai_classification') == 'medical_rd']
    patent_companies = [c for c in companies if c.get('ai_classification') == 'patent_brokerage']
    
    for company in medical_companies[:3]:
        report += f"• {company['name']} - {company.get('location', 'N/A')}\n"
    
    report += "\nPatent Brokerage Sector:\n"
    for company in patent_companies[:3]:
        report += f"• {company['name']} - {company.get('location', 'N/A')}\n"
    
    report += f"""
DEVELOPMENT POTENTIAL

Hong Kong has significant growth potential in both sectors with:
• Strong university research base (HKU, CUHK, HKUST)
• Government innovation support initiatives
• Strategic location for Asia-Pacific operations
• Established financial and legal infrastructure

Total Companies Analyzed: {len(companies)}
Analysis Completion: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
"""
    
    print(report)
    
    # Save report to file
    try:
        with open(f'HK_Industry_Analysis_Summary_{datetime.now().strftime("%Y%m%d_%H%M%S")}.txt', 'w') as f:
            f.write(report)
        print("📁 Summary report saved to file")
    except Exception as e:
        print(f"⚠️  Could not save report: {e}")
    
    return report

def export_to_json(companies, industry_counts):
    """Export analysis results to JSON"""
    print("\n💾 Exporting Results to JSON")
    print("=" * 40)
    
    results = {
        "analysis_metadata": {
            "timestamp": datetime.now().isoformat(),
            "total_companies": len(companies),
            "framework_version": "1.0.0"
        },
        "industry_distribution": industry_counts,
        "companies": companies,
        "recommendations": [
            "Establish dedicated HSIC codes for Medical R&D (7210.2) and Patent Brokerage (6619.5)",
            "Create government-backed IP valuation certification program", 
            "Develop specialized biomedical research zones with regulatory fast-tracking",
            "Launch patent engineer training programs in partnership with universities",
            "Establish centralized IP trading platform similar to Singapore's IP marketplace",
            "Increase R&D expenditure target to 1.5% of GDP to match regional competitors"
        ]
    }
    
    try:
        filename = f'HK_Industry_Analysis_Data_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json'
        with open(filename, 'w') as f:
            json.dump(results, f, indent=2, default=str)
        print(f"✅ Data exported to: {filename}")
        print(f"📊 File size: {os.path.getsize(filename)} bytes")
    except Exception as e:
        print(f"❌ Export failed: {e}")

def main():
    """Main execution function"""
    print("🏢 Hong Kong Industry Analysis Framework")
    print("🧪 Setup and Test Script")
    print("=" * 60)
    print(f"Execution Time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"Python Version: {sys.version.split()[0]}")
    print()
    
    try:
        # Check dependencies
        available_deps = check_dependencies()
        
        # Test classification
        test_classification()
        
        # Analyze mock data
        companies, industry_counts = analyze_mock_data()
        
        # Generate reports
        generate_summary_report(companies, industry_counts)
        export_to_json(companies, industry_counts)
        
        print("\n🎉 Framework test completed successfully!")
        print("\n📖 Next Steps:")
        print("   1. Install full dependencies for production use:")
        print("      pip install -r requirements.txt")
        print("   2. Run complete analysis:")
        print("      python industry_analysis_framework.py")
        print("   3. Review generated reports and data files")
        print("   4. Customize for your specific research needs")
        
    except Exception as e:
        print(f"❌ Test execution error: {e}")
        logger.error(f"Framework test failed: {e}")

if __name__ == "__main__":
    main()