# Complete Step-by-Step Capstone Execution Guide

This guide will help you run all four systems from start to finish and generate the evidence needed for your reflection brief.

## Prerequisites Checklist

Before starting, verify:

```bash
# Check Python version (need 3.11+)
python --version

# Check git
git --version

# Later: Set API key (if you have one)
export ANTHROPIC_API_KEY="your-key-or-voc-key"

# If using Vocareum key, also set:
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"

# Verify they're set:
python -c "import os; print('Key:', bool(os.environ.get('ANTHROPIC_API_KEY'))); print('Base URL:', os.environ.get('ANTHROPIC_BASE_URL'))"
```

## Phase 1: Set Up Your Workspace

### 1.1 Navigate to Capstone Project

```bash
cd /workspaces/capstone-project
```

### 1.2 Verify Setup Tools Are In Place

```bash
# You should have these files:
ls -la setup_helper.py run_capstone.py SETUP_INSTRUCTIONS.md reflection-brief-template.md
```

### 1.3 Run Setup Helper to Verify Everything

```bash
python setup_helper.py
```

Expected output should show:
- ✅ Python 3.11+ available
- ✅ API key detected (or ⚠️ if not set yet)
- ❌ Course materials not found (until you get them)

## Phase 2: Get Course Materials

The four systems should be in `/workspace/` (capital W, not /workspaces/) as a parallel directory.

### Option A: Materials Already Downloaded
If your instructor provided the materials, verify they're here:

```bash
ls /workspace/
```

You should see:
```
/workspace/
├── Build a Claims Intake Agent with a stop_reason-Driven Loop/
├── Engineer a Long-Conversation Context Strategy for a Retail Support Copilot/
├── Configure Claude Code for a Multi-Surface Monorepo Team/
├── Build a Multi-Shift Quality Monitoring System with Claude Orchestration/
└── Project-Harness Engineering with Claude and Claude Code/
```

### Option B: Download or Clone from Vocareum
1. Open Vocareum in your browser (Cloud Resources tab)
2. Download or copy the course project files
3. Place them in `/workspace/`

### Option C: Clone from GitHub (if available)
```bash
# If your instructor has shared a GitHub repository:
git clone <repo-url> /workspace/capstone-materials
```

## Phase 3: Run All Four Systems

### 3.1 Run the Automation Script

Once materials are in place:

```bash
cd /workspaces/capstone-project
python run_capstone.py
```

This script will:
1. **For each system:**
   - Create a Python virtual environment (`.venv/`)
   - Install dependencies (may take 3-5 minutes per system)
   - Run pytest with all tests
   - Capture test output to `evidence/`

2. **Total runtime:** ~15-20 minutes depending on API calls

3. **Output:** Summary of all 128 tests and their status

### 3.2 Monitor Progress

While the script runs, you can open another terminal and check:

```bash
# Check evidence directory
ls -la evidence/

# Watch for generated log files
tail -f evidence/system-*.log
```

### 3.3 Expected Results

The script should report:

```
System 1: Claims Intake Agent
  Expected: 30 tests passing
  Result: ✅ PASS

System 2: Context Strategy  
  Expected: 30 tests (28 pass, 2 skip on first run)
  Result: ✅ PASS (with note about skipped tests)

System 3: Claude Code Config
  Expected: 35 tests passing
  Result: ✅ PASS

System 4: Quality Monitoring
  Expected: 33 tests passing
  Result: ✅ PASS

Total: 128 tests across all systems
```

## Phase 4: Handle System 2's Special Case

System 2 has a two-part test suite:

### 4.1 First Run

```bash
# Run normally (like other systems):
cd /workspace/Engineer\ a\ Long-Conversation\ Context\ Strategy\ for\ a\ Retail\ Support\ Copilot/04-assemble-and-locate/solution
source .venv/bin/activate
pytest tests/ -v
```

Expected output: **28 passed, 2 skipped**

This is normal! The last 2 tests read output from an actual compression run.

### 4.2 Run the System

```bash
# Execute the compression demonstration
python -m system_name  # (or check README for the actual command)

# This generates the output that tests 29-30 will read
```

### 4.3 Re-run Tests

```bash
# Now the last 2 tests will pass
pytest tests/ -v
```

Expected output: **30 passed** (all tests now pass)

The automation script attempts to handle this automatically. If it doesn't, you may need to run tests twice manually.

## Phase 5: Gather Evidence Artifacts

After all systems complete, verify you have evidence files:

```bash
ls -la evidence/

# Expected:
# system-1-tests.log      (Claims Intake Agent, ~30 tests)
# system-2-tests.log      (Context Strategy, ~30 tests, may show initial 28/2 split)
# system-2-run.txt        (Output from running the compression)
# system-3-tests.log      (Claude Code Config, ~35 tests)
# system-4-tests.log      (Quality Monitoring, ~33 tests)
```

### Inspect a Log File

```bash
# See test counts for System 1:
grep -E "(passed|failed|error)" evidence/system-1-tests.log | tail -5

# Check System 3 for configuration details:
head -100 evidence/system-3-tests.log

# Look for token compression metrics in System 2:
grep -i "token\|compress" evidence/system-2-tests.log
```

## Phase 6: Write the Reflection Brief

### 6.1 Start from Template

```bash
cp reflection-brief-template.md reflection-brief.md
```

### 6.2 Fill in Each Question

For each question in the brief:
1. Read the question
2. Look at your evidence files (the .log files)
3. Find specific test output or results that answer the question
4. **Cite the evidence** in your answer (reference file and line/section)

### 6.3 Citation Format

When citing evidence, use this format:

```markdown
**Question:** Why use stop_reason-driven control?

**Evidence:** From `evidence/system-1-tests.log`, tests demonstrate:
- `test_stop_reason_end_of_escalation` (line 42): Shows escalation ends when stop_reason='end_turn'
- `test_end_of_function_tool_execution` (line 58): Shows tool calls continue until tool ends
- These patterns prove the system terminates on explicit stop signals, not state tracking

**Answer:** The system uses stop_reason because...
```

### 6.4 Complete All Five Sections

1. **System 1: Claims Intake Agent** (4 subsections)
2. **System 2: Context Strategy** (3 subsections)
3. **System 3: Claude Code Config** (5 subsections)
4. **System 4: Layer 3 Orchestrator** (5 subsections)
5. **Cross-System Synthesis** (2 subsections)

Each answer must cite your evidence!

## Phase 7: Commit and Submit

### 7.1 Stage Your Work

```bash
cd /workspaces/capstone-project
git add evidence/ reflection-brief.md
git status  # Verify what will be committed
```

### 7.2 Create a Meaningful Commit

```bash
git commit -m "Capstone project: all four systems tested, evidence gathered, reflection brief completed

- System 1: Claims Intake Agent - 30 tests passing
- System 2: Context Strategy - 30 tests passing (with token compression evidence)
- System 3: Claude Code Config - 35 tests passing
- System 4: Quality Monitoring - 33 tests passing
- Total: 128 tests passing
- Reflection brief completed with evidence citations"
```

### 7.3 Push to GitHub

```bash
git push origin main
```

Verify it's on GitHub:
```bash
# Check your repository online at:
https://github.com/Avishree01/capstone-project
```

## Phase 8: Self-Check Before Submission

Before considering the project complete:

### Checklist

- [ ] All four systems' tests pass (128 total)
- [ ] Evidence artifacts exist in `evidence/` directory:
  - [ ] system-1-tests.log
  - [ ] system-2-tests.log (showing 28+2 or all 30)
  - [ ] system-3-tests.log
  - [ ] system-4-tests.log
- [ ] `reflection-brief.md` exists and is filled out
- [ ] Every answer in the brief cites evidence
- [ ] Evidence citations reference the artifact files
- [ ] No generic/placeholder answers (all cite specific test output)
- [ ] All files are committed to git
- [ ] Repository is pushed to GitHub

### Validation Script (Optional)

```bash
# Create a quick validation:
python -c "
import os
from pathlib import Path

evidence_dir = Path('evidence')
brief = Path('reflection-brief.md')

# Check evidence files exist
required = ['system-1-tests.log', 'system-2-tests.log', 'system-3-tests.log', 'system-4-tests.log']
for f in required:
    if (evidence_dir / f).exists():
        print(f'✅ {f}')
    else:
        print(f'❌ {f} missing')

# Check brief exists and has content
if brief.exists():
    content = brief.read_text()
    if len(content) > 2000:  # Should be substantial
        print(f'✅ reflection-brief.md exists ({len(content)} chars)')
    else:
        print(f'⚠️ reflection-brief.md seems short ({len(content)} chars)')
else:
    print(f'❌ reflection-brief.md missing')
"
```

## Troubleshooting

### Problem: "Module not found" or import errors

**Solution:** Verify virtual environment is activated and dependencies installed:

```bash
cd <system-directory>
source .venv/bin/activate
pip install -e ".[dev]"
python -m pytest tests/ -v
```

### Problem: API key errors or 401 Unauthorized

**Solution:** Check key is set and format is correct:

```bash
python -c "import os; print(os.environ.get('ANTHROPIC_API_KEY', 'NOT SET')[:20])"

# If using Vocareum key (starts with 'voc-'), must also set:
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"
```

### Problem: "2 tests skipped" in System 2

**This is expected on first run!**

Solution: Run the system once to generate output, then re-run tests:

```bash
cd /workspace/Engineer*/04-assemble-and-locate/solution
source .venv/bin/activate

# First run - some tests will skip (need run output)
pytest tests/ -v

# Generate the output that tests need
python <whatever-command-the-readme-says>

# Second run - all tests should pass now
pytest tests/ -v
```

### Problem: Virtual environment location/path issues

**Solution:** Use full paths:

```bash
python -m venv /full/path/to/solution/.venv
/full/path/to/solution/.venv/bin/python -m pip install -e ".[dev]"
/full/path/to/solution/.venv/bin/python -m pytest tests/ -v
```

### Problem: Tests take too long / timeout

**Solution:** Some tests call the Claude API. This is normal and expected. Let them run. If timeout is an issue:

```bash
# Run with extended timeout:
pytest tests/ -v --timeout=300  # 5 minutes per test

# Or run specific test:
pytest tests/test_specific.py -v
```

## Next Steps After Completion

1. **Submit:** Make sure your repository is pushed to GitHub
2. **Verify:** Have your instructor or peer review check the evidence citations
3. **Reflect:** Review the reflection brief - does it tell a coherent story about why each system is designed the way it is?
4. **Archive:** Keep the evidence/ directory - these are your proof of completion

---

**Good luck! You've got this! 🚀**

Questions? Review the individual system README.md files in their solution/ directories for details about each system.
