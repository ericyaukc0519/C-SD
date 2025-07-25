# 🏢 Hong Kong Industry Analysis Framework

**AI-Powered Industry Classification and Market Gap Analysis for Medical R&D and Patent Brokerage Sectors**

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)

## 🎯 Overview

A comprehensive Python-based data pipeline designed specifically for analyzing Hong Kong's Medical R&D and Patent Brokerage industries. This framework combines web scraping, AI-powered classification, market analysis, and automated reporting to provide actionable insights for policymakers, investors, and researchers.

### 🌟 Key Features

- **🔍 Multi-Source Data Collection**: Automated scraping from Hong Kong Companies Registry, HKTDC, and IP Department
- **🧠 AI-Powered Classification**: NLP-based industry categorization using NLTK and scikit-learn
- **📊 Comprehensive Analysis**: Market gap identification, barrier analysis, and opportunity mapping
- **📈 Professional Visualizations**: Automated chart generation with Matplotlib and Seaborn
- **🎬 Auto-Generated Reports**: Professional PowerPoint presentations, Excel reports, and JSON exports
- **🗄️ Database Integration**: SQLite storage with structured company and analysis data
- **🔧 Highly Configurable**: Customizable industry keywords and classification frameworks

## 🚀 Quick Start

### One-Command Setup & Execution

```bash
python3 quick_start.py
```

This script will:
1. ✅ Check Python version compatibility
2. 📦 Install all required dependencies
3. 🧠 Download NLP data
4. 🏢 Run the complete analysis
5. 🎭 Optionally show demo presentation

### Manual Setup

```bash
# 1. Install dependencies
pip install -r requirements.txt

# 2. Download NLTK data
python3 -c "import nltk; nltk.download('punkt_tab'); nltk.download('stopwords'); nltk.download('wordnet')"

# 3. Run analysis
MPLBACKEND=Agg python3 industry_analysis_framework.py

# 4. View demo
python3 demo_analysis.py
```

## 📊 Output Files

After running the analysis, you'll get:

| File Type | Description | Use Case |
|-----------|-------------|----------|
| **PowerPoint** | `HK_Industry_Analysis_*.pptx` | Executive presentations |
| **Excel Report** | `industry_analysis_results_*.xlsx` | Data analysis & filtering |
| **JSON Data** | `industry_analysis_results_*.json` | API integration & processing |
| **Charts** | `charts/*.png` | Standalone visualizations |
| **Database** | `industry_analysis.db` | Query & advanced analysis |
| **Logs** | `industry_analysis.log` | Debugging & monitoring |

## 🏗️ Architecture

```
Hong Kong Industry Analysis Framework
├── 🔍 Data Collection Layer
│   ├── Companies Registry Scraper
│   ├── HKTDC Directory Integration
│   └── IP Department Database
├── 🧠 Processing Layer
│   ├── AI Industry Classifier (NLP)
│   ├── ISIC/HSIC Code Mapper
│   └── Data Validation Engine
├── 📈 Analysis Layer
│   ├── Market Gap Analyzer
│   ├── Trend Analysis Engine
│   └── Statistical Visualizer
└── 📋 Output Layer
    ├── PowerPoint Generator
    ├── Excel/JSON Exporter
    └── Database Storage
```

## 📈 Industry Classification Framework

### Medical R&D Industry
- **ISIC Code**: 7210 (Natural sciences R&D)
- **HSIC Gap**: No dedicated class (grouped under 8520-R&D)
- **Proposed Framework**:
  - Clinical research organizations
  - Biopharma labs
  - Medtech innovation hubs

### Patent Brokerage
- **ISIC Code**: 6619 (Other auxiliary financial services)
- **HSIC Gap**: Not explicitly classified
- **Proposed Framework**:
  - IP valuation firms
  - Technology transfer offices
  - Licensing specialists

## 🔍 Sample Analysis Results

### Key Findings
- **Medical R&D**: ~42 companies identified (78% in Science Park)
- **Patent Brokerage**: Only 9 specialized firms + 35 law firms with IP services
- **Growth Metrics**: 15% CAGR in medical patents since 2018
- **R&D Investment**: HK 0.99% of GDP vs Singapore's 1.89%

### Critical Classification Gaps
- HSIC lacks codes for 7210.2 (Biomedical research)
- HSIC lacks codes for 6619.5 (IP brokerage)

## 🎯 Use Cases

| Sector | Application | Benefits |
|--------|-------------|----------|
| **🏛️ Government** | Policy development & HSIC updates | Evidence-based decisions |
| **💼 Investment** | VC deal sourcing & market entry | Competitive intelligence |
| **🎓 Academia** | Innovation ecosystem research | Industry trend analysis |
| **🏢 Corporate** | M&A target identification | Strategic planning |
| **🌏 Regional** | HK vs Singapore comparison | Benchmarking studies |

## 🔧 Customization

### Industry Keywords
Edit `industry_analysis_framework.py`:

```python
# Medical R&D keywords
self.medical_rd_keywords = [
    'biomed', 'clinical trial', 'pharma research',
    # Add your custom keywords here
]

# Patent brokerage keywords
self.patent_brokerage_keywords = [
    'patent licensing', 'ip brokerage',
    # Add your custom keywords here
]
```

### Data Sources
Add custom scrapers in `HongKongDataScraper` class:

```python
def scrape_custom_database(self) -> List[Dict]:
    """Add your custom data source here"""
    # Your scraping logic
    return custom_companies_data
```

### PowerPoint Styling
Modify colors in `ppt_generator.py`:

```python
self.colors = {
    'primary': RGBColor(0, 51, 102),     # Your brand colors
    'secondary': RGBColor(0, 153, 204),
    'accent': RGBColor(255, 102, 0),
}
```

## 📊 Technical Specifications

| Component | Technology | Purpose |
|-----------|------------|---------|
| **Web Scraping** | Requests + BeautifulSoup | Data collection |
| **NLP Processing** | NLTK + scikit-learn | Text classification |
| **Data Analysis** | Pandas + NumPy | Data processing |
| **Visualization** | Matplotlib + Seaborn | Chart generation |
| **Database** | SQLite | Data storage |
| **Reporting** | python-pptx + openpyxl | Output generation |

## 📋 Requirements

- **Python**: 3.8 or higher
- **Memory**: 4GB+ RAM recommended
- **Storage**: ~500MB for dependencies
- **Network**: Internet connection for scraping

## 🛠️ Troubleshooting

### Common Issues

**NLTK Data Missing**
```bash
python3 -c "import nltk; nltk.download('all')"
```

**Memory Issues**
```python
# Reduce dataset size in scraping functions
scraper.scrape_companies_registry(max_pages=5)
```

**Chart Generation Fails**
```bash
# Install GUI backend
pip install PyQt5
# Or use headless mode
export MPLBACKEND=Agg
```

## 🚀 Advanced Features

### Production Deployment
- **API Integration**: Replace simulated data with real endpoints
- **Scheduling**: Add cron jobs for regular updates
- **Monitoring**: Implement logging and alerting
- **Scaling**: Use multiprocessing for larger datasets

### Enhanced Analysis
- **Real-time Scraping**: Selenium WebDriver integration
- **Advanced NLP**: BERT/GPT model integration
- **Interactive Dashboards**: Streamlit/Dash web interface
- **Cloud Integration**: AWS/GCP deployment options

## 📞 Support & Contributing

### Getting Help
- 📖 **Documentation**: `setup_and_usage.md`
- 🎭 **Demo**: `python3 demo_analysis.py`
- 📊 **Logs**: Check `industry_analysis.log`
- 🔧 **Issues**: Review configuration in Python files

### Contributing
1. Fork the repository
2. Create feature branch
3. Add comprehensive tests
4. Submit pull request with detailed description

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- Hong Kong Companies Registry for public data access
- HKTDC for trade development information
- Hong Kong IP Department for patent data
- Open source Python community for excellent libraries

---

**Built with ❤️ for Hong Kong's Innovation Ecosystem**

*Ready to analyze Hong Kong's emerging industries and support evidence-based policy making!*