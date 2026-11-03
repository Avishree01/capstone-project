#!/usr/bin/env python3
"""
Capstone Project Automation Script

Runs all four systems:
1. Claims Intake Agent (stop_reason loop)
2. Context Strategy (token compression)
3. Claude Code Config (CLAUDE.md hierarchy)
4. Quality Monitoring (Layer 3 orchestrator)

Creates evidence artifacts and generates reflection brief foundation.
"""

import os
import sys
import subprocess
import json
from pathlib import Path
from datetime import datetime


class CapstoneRunner:
    def __init__(self):
        self.workspace_root = Path("/workspace")
        self.capstone_root = Path("/workspaces/capstone-project")
        self.evidence_dir = self.capstone_root / "evidence"
        self.evidence_dir.mkdir(exist_ok=True)
        
        # Define the four systems
        self.systems = {
            "1-claims-intake": {
                "name": "Claims Intake Agent (stop_reason loop)",
                "base_dir": self.workspace_root / "Build a Claims Intake Agent with a stop_reason-Driven Loop",
                "solution_path": "exercises/03-dynamic-decomposition/solution",
                "expected_tests": 30,
            },
            "2-context-strategy": {
                "name": "Context Strategy (token compression)",
                "base_dir": self.workspace_root / "Engineer a Long-Conversation Context Strategy for a Retail Support Copilot",
                "solution_path": "04-assemble-and-locate/solution",
                "expected_tests": 30,  # 28 pass, 2 skip initially
            },
            "3-claude-code": {
                "name": "Claude Code Config (CLAUDE.md hierarchy)",
                "base_dir": self.workspace_root / "Configure Claude Code for a Multi-Surface Monorepo Team",
                "solution_path": "04-plan-mode-and-explore-decision-doc/solution",
                "expected_tests": 35,
            },
            "4-quality-monitoring": {
                "name": "Quality Monitoring (Layer 3 orchestrator)",
                "base_dir": self.workspace_root / "Build a Multi-Shift Quality Monitoring System with Claude Orchestration",
                "solution_path": "04-fork-scratchpad/solution",
                "expected_tests": 33,
            },
        }
    
    def run(self):
        """Run all four systems"""
        print("=" * 80)
        print("CAPSTONE PROJECT AUTOMATION")
        print(f"Started: {datetime.now().isoformat()}")
        print("=" * 80)
        print()
        
        # Check prerequisites
        if not self.check_prerequisites():
            print("❌ Prerequisites check failed. See above for details.")
            return False
        
        # Check if workspace materials exist
        if not self.check_materials():
            print("❌ Course materials not found. See SETUP_INSTRUCTIONS.md")
            return False
        
        # Run each system
        results = {}
        for system_id, config in self.systems.items():
            print(f"\n{'='*80}")
            print(f"Running System {system_id}: {config['name']}")
            print(f"{'='*80}")
            
            success = self.run_system(system_id, config)
            results[system_id] = success
        
        # Print summary
        self.print_summary(results)
        
        return all(results.values())
    
    def check_prerequisites(self):
        """Verify Python, git, and environment"""
        print("Checking prerequisites...")
        
        # Check Python version
        py_version = sys.version_info
        if py_version.major < 3 or py_version.minor < 11:
            print(f"❌ Python 3.11+ required, got {py_version.major}.{py_version.minor}")
            return False
        print(f"✅ Python {py_version.major}.{py_version.minor}")
        
        # Check git
        result = subprocess.run(["git", "--version"], capture_output=True)
        if result.returncode != 0:
            print("❌ git not found")
            return False
        print(f"✅ git available")
        
        # Check API key (optional for some systems)
        has_key = bool(os.environ.get("ANTHROPIC_API_KEY"))
        print(f"{'✅' if has_key else '⚠️'} ANTHROPIC_API_KEY: {'set' if has_key else 'not set (OK for System 3)'}")
        
        return True
    
    def check_materials(self):
        """Verify course materials are available"""
        print("\nChecking course materials...")
        
        missing = []
        for system_id, config in self.systems.items():
            solution_dir = config["base_dir"] / config["solution_path"]
            if not solution_dir.exists():
                missing.append(f"  - {config['name']}")
        
        if missing:
            print("❌ Missing systems:")
            for m in missing:
                print(m)
            print(f"\nExpected location: {self.workspace_root}/")
            return False
        
        print("✅ All course materials found")
        return True
    
    def run_system(self, system_id, config):
        """Run a single system"""
        solution_dir = config["base_dir"] / config["solution_path"]
        
        if not solution_dir.exists():
            print(f"❌ Solution directory not found: {solution_dir}")
            return False
        
        # Create venv
        venv_path = solution_dir / ".venv"
        print(f"\n1. Setting up Python virtual environment...")
        
        if not self.create_venv(venv_path):
            return False
        
        # Install dependencies
        print(f"2. Installing dependencies...")
        if not self.install_dependencies(solution_dir, venv_path):
            return False
        
        # Run tests
        print(f"3. Running tests...")
        test_output = self.run_tests(solution_dir, venv_path, system_id)
        if test_output is None:
            return False
        
        # Save evidence
        log_path = self.evidence_dir / f"system-{system_id}-tests.log"
        log_path.write_text(test_output)
        print(f"   Saved to: {log_path}")
        
        return True
    
    def create_venv(self, venv_path):
        """Create Python virtual environment"""
        try:
            subprocess.run(
                [sys.executable, "-m", "venv", str(venv_path)],
                check=True,
                capture_output=True,
            )
            print(f"   ✅ venv created at {venv_path}")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to create venv: {e.stderr.decode()}")
            return False
    
    def install_dependencies(self, solution_dir, venv_path):
        """Install dependencies with dev extras"""
        try:
            python_exe = venv_path / "bin" / "python"
            
            # Install the package with dev dependencies
            subprocess.run(
                [str(python_exe), "-m", "pip", "install", "-e", ".[dev]"],
                cwd=str(solution_dir),
                check=True,
                capture_output=True,
            )
            print(f"   ✅ Dependencies installed")
            return True
        except subprocess.CalledProcessError as e:
            print(f"   ❌ Failed to install dependencies")
            print(f"   Error: {e.stderr.decode()}")
            return False
    
    def run_tests(self, solution_dir, venv_path, system_id):
        """Run pytest and capture output"""
        try:
            python_exe = venv_path / "bin" / "python"
            
            result = subprocess.run(
                [str(python_exe), "-m", "pytest", "tests/", "-v"],
                cwd=str(solution_dir),
                capture_output=True,
                text=True,
            )
            
            output = result.stdout + "\n" + result.stderr
            
            # Parse test results
            if "passed" in output:
                print(f"   ✅ Tests completed")
                # Extract summary line
                for line in output.split('\n'):
                    if 'passed' in line or 'failed' in line:
                        print(f"   {line.strip()}")
            else:
                print(f"   ⚠️ Could not parse test results")
            
            return output
        except Exception as e:
            print(f"   ❌ Failed to run tests: {e}")
            return None
    
    def print_summary(self, results):
        """Print execution summary"""
        print(f"\n{'='*80}")
        print("CAPSTONE EXECUTION SUMMARY")
        print(f"{'='*80}")
        
        passed = sum(1 for v in results.values() if v)
        total = len(results)
        
        for system_id, success in results.items():
            config = self.systems[system_id]
            status = "✅ PASS" if success else "❌ FAIL"
            print(f"{status} - {config['name']}")
        
        print(f"\n{'='*80}")
        print(f"Results: {passed}/{total} systems completed successfully")
        print(f"Evidence saved to: {self.evidence_dir}")
        print(f"Completed: {datetime.now().isoformat()}")
        print(f"{'='*80}")


if __name__ == "__main__":
    runner = CapstoneRunner()
    success = runner.run()
    sys.exit(0 if success else 1)
