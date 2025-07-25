# 🏢 Hong Kong Industry Analysis & Text Comparison Suite

A comprehensive toolkit featuring:
1. **Industry Analysis Framework** - Advanced data pipeline for Hong Kong Medical R&D and Patent Brokerage industries
2. **Dual Text Areas Comparison Tool** - Web-based tool for comparing include/exclude sections

## 🔬 Industry Analysis Framework

### Key Features
- **Automated Data Collection** from Hong Kong sources (Companies Registry, HKTDC, Science Park, IP Department)
- **AI-Powered Classification** using NLP for Medical R&D and Patent Brokerage industries
- **Market Gap Analysis** with statistical insights and barrier identification
- **Automated Report Generation** (PowerPoint, Excel, JSON, visualizations)

### Quick Start
```bash
# Install dependencies
pip install -r requirements.txt

# Run complete analysis
python industry_analysis_framework.py

# Or test with minimal dependencies
python setup_and_test.py
```

### Industry Insights
- **Medical R&D**: 42+ companies identified, 15% CAGR, concentrated in Science Park
- **Patent Brokerage**: 9 specialized firms, growing sector with infrastructure gaps
- **R&D Expenditure**: 0.99% of GDP (target: 1.5%), 120% growth since 2015

## 📊 Text Comparison Features

### 🎯 **Dual Text Areas**
- **Left panel**: For Sheet1 content using "This class includes/excludes" format
- **Right panel**: For Sheet2 content using "Include/Exclude" format

### 🔍 **Comparison Features**
- Extracts include/exclude sections from both texts automatically
- Compares items using sequence similarity (JavaScript implementation of difflib's SequenceMatcher)
- Shows items unique to each sheet with configurable similarity threshold (80% by default)

### 🎮 **Interactive Elements**
- **"Compare Texts" button**: Run analysis on both text areas
- **"Clear All" button**: Reset all inputs and results
- Scrollable output area with formatted results

### 🎨 **Visual Output**
- Clearly shows items present in one sheet but not the other
- Groups results into "Includes" and "Excludes" sections
- Highlights differences with bullet points and color coding
- Beautiful, modern UI with responsive design

## How to Use

1. **Open the Tool**: Open `index.html` in your web browser
2. **Input Text**: 
   - Paste Sheet1 content in the left text area
   - Paste Sheet2 content in the right text area
3. **Compare**: Click "Compare Texts" to see:
   - Items only in Sheet1
   - Items only in Sheet2
4. **Clear**: Use "Clear All" to reset and start over

## Supported Formats

### Sheet1 Format (Left Panel)
```
This class includes:
- Item 1
- Item 2
- Item 3

This class excludes:
- Item 4
- Item 5
```

### Sheet2 Format (Right Panel)
```
Include:
- Item 1
- Item 6
- Item 7

Exclude:
- Item 4
- Item 8
```

## Technical Features

- **Sequence Similarity**: Uses edit distance algorithm for fuzzy matching
- **Smart Parsing**: Automatically removes bullet points, numbers, and formatting
- **Responsive Design**: Works on desktop and mobile devices
- **Modern UI**: Clean, professional interface with animations
- **No Dependencies**: Pure HTML, CSS, and JavaScript - no external libraries required

## Getting Started

### Text Comparison Tool
Simply open `index.html` in any modern web browser. No installation or setup required!

### Industry Analysis Framework
1. **Review Documentation**: See `INDUSTRY_ANALYSIS_GUIDE.md` for comprehensive usage guide
2. **Run Test**: Execute `python setup_and_test.py` to test with minimal dependencies
3. **Full Analysis**: Install requirements and run `python industry_analysis_framework.py`
4. **Example Usage**: Check `example_usage.py` for detailed examples

## Files Overview

| File | Purpose |
|------|---------|
| `index.html` | Text comparison web tool |
| `industry_analysis_framework.py` | Main industry analysis pipeline |
| `setup_and_test.py` | Framework test with minimal dependencies |
| `example_usage.py` | Usage examples and demonstrations |
| `INDUSTRY_ANALYSIS_GUIDE.md` | Comprehensive documentation |
| `requirements.txt` | Python dependencies |

## Browser Compatibility (Text Tool)

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Any modern browser with ES6 support