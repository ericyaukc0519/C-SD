# 📊 Dual Text Areas Comparison Tool

A web-based tool for comparing include/exclude sections between two different text formats (Sheet1 and Sheet2 content).

## Features

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

Simply open `index.html` in any modern web browser. No installation or setup required!

## Browser Compatibility

- Chrome/Chromium (recommended)
- Firefox
- Safari
- Edge
- Any modern browser with ES6 support