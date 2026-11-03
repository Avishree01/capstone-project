#!/usr/bin/env python3
"""
Interactive Capstone Setup Helper

This script helps you:
1. Locate or download the four course projects
2. Set up environment variables
3. Run the capstone automation
"""

import os
import sys
import subprocess
from pathlib import Path


def print_header(text):
    """Print a section header"""
    print("\n" + "=" * 80)
    print(f"  {text}")
    print("=" * 80)


def check_materials_location():
    """Check if course materials exist"""
    print_header("Checking for Course Materials")
    
    workspace_path = Path("/workspace")
    capstone_path = Path("/workspaces/capstone-project")
    
    print(f"\nPrimary location: {workspace_path}")
    print(f"Fallback location: {capstone_path}")
    
    systems = [
        "Build a Claims Intake Agent with a stop_reason-Driven Loop",
        "Engineer a Long-Conversation Context Strategy for a Retail Support Copilot",
        "Configure Claude Code for a Multi-Surface Monorepo Team",
        "Build a Multi-Shift Quality Monitoring System with Claude Orchestration",
    ]
    
    found = {
        "primary": [],
        "fallback": [],
        "missing": []
    }
    
    for system in systems:
        primary_exists = (workspace_path / system).exists()
        fallback_exists = (capstone_path / system).exists()
        
        if primary_exists:
            found["primary"].append(system)
        elif fallback_exists:
            found["fallback"].append(system)
        else:
            found["missing"].append(system)
    
    if found["primary"]:
        print(f"\n✅ Found {len(found['primary'])} in /workspace/:")
        for s in found["primary"]:
            print(f"   - {s}")
    
    if found["fallback"]:
        print(f"\n✅ Found {len(found['fallback'])} in capstone-project/:")
        for s in found["fallback"]:
            print(f"   - {s}")
    
    if found["missing"]:
        print(f"\n❌ Missing {len(found['missing'])} systems:")
        for s in found["missing"]:
            print(f"   - {s}")
        return False
    
    return True


def check_api_key():
    """Check if API key is configured"""
    print_header("Checking API Configuration")
    
    has_key = bool(os.environ.get("ANTHROPIC_API_KEY"))
    base_url = os.environ.get("ANTHROPIC_BASE_URL")
    
    print(f"\nANTHROPIC_API_KEY: {'✅ SET' if has_key else '❌ NOT SET'}")
    
    if has_key:
        key_start = os.environ.get("ANTHROPIC_API_KEY", "")[:10]
        key_type = "Vocareum (voc-)" if key_start.startswith("voc-") else "Standard Anthropic"
        print(f"  Type: {key_type}")
        print(f"  Value: {key_start}...")
        
        if key_start.startswith("voc-") and not base_url:
            print("\n⚠️  WARNING: Vocareum key detected but ANTHROPIC_BASE_URL not set!")
            print("   Set it to: https://claude.vocareum.com")
            return False
    
    print(f"\nANTHROPIC_BASE_URL: {'✅ SET' if base_url else '⚠️  not set'}")
    if base_url:
        print(f"  Value: {base_url}")
    
    return True  # Optional for some systems


def check_python():
    """Check Python version"""
    print_header("Checking Python Environment")
    
    version = sys.version_info
    print(f"\nPython version: {version.major}.{version.minor}.{version.micro}")
    
    if version.major < 3 or version.minor < 11:
        print("❌ ERROR: Python 3.11+ required")
        return False
    
    print("✅ Python version OK")
    
    # Check venv availability
    try:
        import venv
        print("✅ venv module available")
        return True
    except ImportError:
        print("❌ ERROR: venv module not available")
        return False


def print_next_steps():
    """Print instructions for next steps"""
    print_header("Next Steps")
    
    print("""
1. DOWNLOAD COURSE MATERIALS
   If not found, download or clone the course projects to /workspace/
   
   Expected structure:
   /workspace/
   ├── Build a Claims Intake Agent with a stop_reason-Driven Loop/
   ├── Engineer a Long-Conversation Context Strategy for a Retail Support Copilot/
   ├── Configure Claude Code for a Multi-Surface Monorepo Team/
   ├── Build a Multi-Shift Quality Monitoring System with Claude Orchestration/
   └── Project-Harness Engineering with Claude and Claude Code/

2. SET API KEY (if needed)
   export ANTHROPIC_API_KEY="your-key-here"
   
   If using Vocareum key:
   export ANTHROPIC_BASE_URL="https://claude.vocareum.com"

3. RUN AUTOMATION
   python run_capstone.py
   
   This will:
   - Create virtual environments for each system
   - Install dependencies (may take several minutes)
   - Run test suites (~128 tests total)
   - Capture evidence artifacts
   - Show results summary

4. WRITE REFLECTION BRIEF
   After automation completes, fill in:
   reflection-brief-template.md
   
   Cite the captured evidence from each system run.
""")


def main():
    """Main setup flow"""
    print("\n" + "=" * 80)
    print("  CAPSTONE PROJECT - INTERACTIVE SETUP")
    print("=" * 80)
    
    # Check each component
    checks = {
        "Python Environment": check_python(),
        "API Configuration": check_api_key(),
        "Course Materials": check_materials_location(),
    }
    
    # Summary
    print_header("Setup Summary")
    all_ok = True
    
    for check_name, result in checks.items():
        status = "✅ PASS" if result else "⚠️  REVIEW"
        print(f"{status} - {check_name}")
        if not result:
            all_ok = False
    
    # Next steps
    print_next_steps()
    
    if all_ok:
        print("\n" + "=" * 80)
        print("  ✅ ALL CHECKS PASSED - Ready to run!")
        print("=" * 80)
        print("\nRun: python run_capstone.py")
    else:
        print("\n" + "=" * 80)
        print("  ⚠️  SOME CHECKS REQUIRE ATTENTION")
        print("=" * 80)
    
    return 0 if all_ok else 1


if __name__ == "__main__":
    sys.exit(main())
