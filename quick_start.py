#!/usr/bin/env python3
"""
Hong Kong Industry Analysis Framework - Quick Start Script
One-command setup and execution
"""

import os
import sys
import subprocess
import platform
from pathlib import Path

def print_header():
    """Print welcome header"""
    print("🚀" * 60)
    print("🏢 HONG KONG INDUSTRY ANALYSIS FRAMEWORK")
    print("🚀 QUICK START SETUP & EXECUTION")
    print("🚀" * 60)

def check_python_version():
    """Check if Python version is compatible"""
    print("🔍 Checking Python version...")
    
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ required. Current version:", f"{version.major}.{version.minor}")
        print("   Please upgrade Python and try again.")
        return False
    
    print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
    return True

def install_dependencies():
    """Install required dependencies"""
    print("\n📦 Installing dependencies...")
    
    try:
        # Check if requirements.txt exists
        if not Path("requirements.txt").exists():
            print("❌ requirements.txt not found")
            return False
        
        # Install with pip
        result = subprocess.run([
            sys.executable, "-m", "pip", "install", "--break-system-packages", 
            "-r", "requirements.txt"
        ], capture_output=True, text=True)
        
        if result.returncode == 0:
            print("✅ Dependencies installed successfully")
            return True
        else:
            print("❌ Failed to install dependencies:")
            print(result.stderr)
            return False
            
    except Exception as e:
        print(f"❌ Error installing dependencies: {e}")
        return False

def download_nltk_data():
    """Download required NLTK data"""
    print("\n🧠 Setting up NLP data...")
    
    try:
        import nltk
        
        # Download required NLTK data
        nltk_packages = ['punkt_tab', 'punkt', 'stopwords', 'wordnet']
        
        for package in nltk_packages:
            try:
                nltk.download(package, quiet=True)
            except:
                pass  # Some packages might already exist
        
        print("✅ NLP data setup complete")
        return True
        
    except ImportError:
        print("❌ NLTK not installed. Please install dependencies first.")
        return False
    except Exception as e:
        print(f"❌ Error setting up NLP data: {e}")
        return False

def run_analysis():
    """Run the main analysis framework"""
    print("\n🏢 Running Industry Analysis Framework...")
    
    try:
        # Set matplotlib backend for headless environments
        env = os.environ.copy()
        env['MPLBACKEND'] = 'Agg'
        
        # Run the main analysis
        result = subprocess.run([
            sys.executable, "industry_analysis_framework.py"
        ], env=env, capture_output=False)
        
        if result.returncode == 0:
            print("\n✅ Analysis completed successfully!")
            return True
        else:
            print(f"\n❌ Analysis failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running analysis: {e}")
        return False

def run_demo():
    """Run the demo script"""
    print("\n🎭 Running Demo Presentation...")
    
    try:
        result = subprocess.run([sys.executable, "demo_analysis.py"], capture_output=False)
        
        if result.returncode == 0:
            print("\n✅ Demo completed successfully!")
            return True
        else:
            print(f"\n❌ Demo failed with return code: {result.returncode}")
            return False
            
    except Exception as e:
        print(f"❌ Error running demo: {e}")
        return False

def show_next_steps():
    """Show next steps for users"""
    print("\n🎉 SETUP COMPLETE!")
    print("=" * 50)
    print("📁 Generated Files:")
    print("   • JSON Results: industry_analysis_results_*.json")
    print("   • Excel Report: industry_analysis_results_*.xlsx") 
    print("   • PowerPoint: HK_Industry_Analysis_*.pptx")
    print("   • Charts: charts/ directory")
    print("   • Database: industry_analysis.db")
    
    print("\n🚀 What's Next:")
    print("1. 📊 Review the generated PowerPoint presentation")
    print("2. 📈 Analyze the Excel report and JSON data")
    print("3. 🎨 Check the charts in the charts/ directory")
    print("4. 🔧 Customize keywords in industry_analysis_framework.py")
    print("5. 🌐 Integrate real data sources for production use")
    
    print("\n📖 Documentation:")
    print("   • Setup Guide: setup_and_usage.md")
    print("   • Code Documentation: Comments in Python files")
    print("   • Demo Script: python3 demo_analysis.py")
    
    print("\n🆘 Need Help?")
    print("   • Check industry_analysis.log for detailed logs")
    print("   • Run: python3 demo_analysis.py for feature overview")
    print("   • Modify keyword lists in IndustryClassifier class")

def main():
    """Main execution function"""
    print_header()
    
    # Step 1: Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Step 2: Install dependencies
    if not install_dependencies():
        print("\n⚠️ Dependency installation failed. Trying to continue...")
    
    # Step 3: Setup NLTK data
    if not download_nltk_data():
        print("\n⚠️ NLTK setup failed. Trying to continue...")
    
    # Step 4: Run analysis
    if not run_analysis():
        print("\n❌ Analysis failed. Please check the logs.")
        sys.exit(1)
    
    # Step 5: Run demo (optional)
    print("\n🎭 Would you like to see the demo presentation? (y/n): ", end="")
    
    try:
        choice = input().strip().lower()
        if choice in ['y', 'yes']:
            run_demo()
    except KeyboardInterrupt:
        print("\n\n⏹️ Skipping demo...")
    
    # Step 6: Show next steps
    show_next_steps()
    
    print("\n🎉 Hong Kong Industry Analysis Framework is ready!")
    print("🚀" * 60)

if __name__ == "__main__":
    main()