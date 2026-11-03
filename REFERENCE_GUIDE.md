# Capstone Project Reference Guide

Quick reference for running and understanding the four systems.

## System Overview

| System | Focus | Tests | Key Tool | State |
|--------|-------|-------|----------|-------|
| 1: Claims Intake Agent | Control flow via `stop_reason` | 30 | Loop termination | In memory |
| 2: Context Strategy | Token compression | 30 | Position-aware pruning | Converted state |
| 3: Claude Code Config | CLAUDE.md hierarchy | 35 | Path-scoped rules | Configuration |
| 4: Quality Monitoring | Tiered storage & recovery | 33 | SQL pre-filtering | Persistent |

## Quick Setup

```bash
# From /workspaces/capstone-project/

# 1. Verify environment
python setup_helper.py

# 2. Get materials to /workspace/
# (See SETUP_INSTRUCTIONS.md for details)

# 3. Set API key (optional, needed for Systems 1, 2, 4)
export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"  # if using Vocareum key

# 4. Run all systems
python run_capstone.py

# 5. Verify evidence captured
ls evidence/

# 6. Start writing reflection brief
cp reflection-brief-template.md reflection-brief.md
# Edit reflection-brief.md with citations
```

## File Locations & Purposes

### In `/workspaces/capstone-project/` (Your Work)
- `run_capstone.py` — Automation script that runs all four systems
- `setup_helper.py` — Validates environment prerequisites
- `SETUP_INSTRUCTIONS.md` — First-time setup guide
- `EXECUTION_GUIDE.md` — Step-by-step walkthrough
- `reflection-brief-template.md` — Template for reflection brief
- `evidence/` — Directory where test outputs are saved
  - `system-1-tests.log` — Claims Intake Agent output
  - `system-2-tests.log` — Context Strategy output
  - `system-3-tests.log` — Claude Code Config output
  - `system-4-tests.log` — Quality Monitoring output

### In `/workspace/` (Course Materials - Need to Obtain)
```
/workspace/
├── Build a Claims Intake Agent with a stop_reason-Driven Loop/
│   └── exercises/03-dynamic-decomposition/solution/
│       ├── .venv/
│       ├── src/
│       ├── tests/
│       ├── README.md
│       └── pyproject.toml
├── Engineer a Long-Conversation Context Strategy for a Retail Support Copilot/
│   └── 04-assemble-and-locate/solution/
│       └── (similar structure)
├── Configure Claude Code for a Multi-Surface Monorepo Team/
│   └── 04-plan-mode-and-explore-decision-doc/solution/
│       └── (similar structure)
├── Build a Multi-Shift Quality Monitoring System with Claude Orchestration/
│   └── 04-fork-scratchpad/solution/
│       └── (similar structure)
└── Project-Harness Engineering with Claude and Claude Code/
    ├── README.md
    └── reflection-brief-template.md (template reference)
```

## System-Specific Commands

### System 1: Claims Intake Agent

```bash
cd /workspace/Build\ a\ Claims\ Intake\ Agent\ with\ a\ stop_reason-Driven\ Loop/exercises/03-dynamic-decomposition/solution
source .venv/bin/activate
pytest tests/ -v

# What to look for in evidence:
# - "test_stop_reason_*" test names indicate control flow tests
# - Look for assertions on stop_reason values
# - Tool call sequences show loop progression
```

### System 2: Context Strategy

```bash
cd /workspace/Engineer\ a\ Long-Conversation\ Context\ Strategy\ for\ a\ Retail\ Support\ Copilot/04-assemble-and-locate/solution
source .venv/bin/activate

# First run - some tests skip
pytest tests/ -v

# Run the system to generate output
python -m src.main  # or check README for exact command

# Second run - all tests pass
pytest tests/ -v

# What to look for in evidence:
# - Token count comparisons (before/after compression)
# - Test names like "test_compression_ratio", "test_evaluation_questions"
# - Skipped test explanation in first run
```

### System 3: Claude Code Config

```bash
cd /workspace/Configure\ Claude\ Code\ for\ a\ Multi-Surface\ Monorepo\ Team/04-plan-mode-and-explore-decision-doc/solution
source .venv/bin/activate
pytest tests/ -v

# What to look for in evidence:
# - Test names showing CLAUDE.md validation
# - Path-scoping tests
# - Custom command tests
# - Forked context skill tests
# - Validator checks
```

### System 4: Quality Monitoring

```bash
cd /workspace/Build\ a\ Multi-Shift\ Quality\ Monitoring\ System\ with\ Claude\ Orchestration/04-fork-scratchpad/solution
source .venv/bin/activate
pytest tests/ -v

# What to look for in evidence:
# - Session lifecycle tests
# - Tiered storage tests (in-memory, session, persistent)
# - SQL pre-filtering tests
# - Crash recovery tests
# - Fork/investigation tests
```

## Understanding Test Output

### Test Summary Line

```
40 passed, 2 skipped, 1 failed, 3 errors in 12.34s
```

Breakdown:
- `passed` — Tests that succeeded
- `skipped` — Tests intentionally skipped (often expected for System 2)
- `failed` — Tests that ran but assertions failed
- `errors` — Tests that couldn't run (import, setup errors)

### If All Tests Pass

```
======================== 30 passed in 8.42s =========================
```

This is what we want! All four systems should show similar "all passed" output.

### If Tests Fail

1. Check error message for what failed
2. Look at the test name to understand what it was testing
3. Read the assertion that failed
4. For API issues: verify ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL
5. For import issues: run pip install again in that system's venv

## Citation Examples for Reflection Brief

### Citation Format

```markdown
**Evidence:** From `evidence/system-1-tests.log`, line 42:
```test_stop_reason_escalation_routes PASSED```
This shows that...

**Answer:** The system uses stop_reason because it allows...
```

### Strong Citations

❌ **Bad:** "The system uses stop_reason for control flow."

✅ **Good:** "The system uses stop_reason for control flow. Evidence: 
`evidence/system-1-tests.log` shows `test_stop_reason_end_turn PASSED` 
(line 52), demonstrating that the loop terminates when `stop_reason='end_turn'`. 
This is more reliable than state tracking because..."

### Finding Evidence in Logs

```bash
# Search for test names
grep "test_" evidence/system-1-tests.log

# Find specific test output
grep -A 5 "test_stop_reason_escalation" evidence/system-1-tests.log

# Count passing tests
grep -c "PASSED" evidence/system-1-tests.log

# Look for token counts (System 2)
grep -i "token" evidence/system-2-tests.log

# Find configuration examples (System 3)
grep -i "claude.md\|path-scoped" evidence/system-3-tests.log

# Find session/storage info (System 4)
grep -i "session\|tier\|storage" evidence/system-4-tests.log
```

## API Key Troubleshooting

### Check Key is Set

```bash
echo $ANTHROPIC_API_KEY
# Should output your key (or nothing if not set)

# Or programmatically
python -c "import os; print(bool(os.environ.get('ANTHROPIC_API_KEY')))"
# Should print: True
```

### Vocareum Key Format

```bash
# Vocareum keys start with "voc-"
echo $ANTHROPIC_API_KEY | grep "^voc-"
# If nothing prints, it's not a Vocareum key

# If it IS a Vocareum key, MUST set base URL
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"
```

### Standard Anthropic Key

```bash
# Standard keys start with "sk-"
echo $ANTHROPIC_API_KEY | grep "^sk-"

# Base URL is default (not needed)
# But you can set it to be explicit:
export ANTHROPIC_BASE_URL="https://api.anthropic.com"
```

## Virtual Environment Management

### Create a Single venv for All Systems (Alternative)

```bash
# Create one venv for manual testing
python -m venv /workspaces/capstone-project/.venv
source /workspaces/capstone-project/.venv/bin/activate

# Then install each system's dependencies as needed
cd /workspace/System1/...
pip install -e ".[dev]"
pytest tests/

# Switch to another system
cd /workspace/System2/...
pip install -e ".[dev]"
# (Note: may conflict with different versions - see note below)
```

### Python Version Conflicts

Two systems use different `anthropic` package versions:
- System 1 & 2: `anthropic==0.39.0`
- System 3: May use different version
- System 4: May use different version

**Recommendation:** Use separate venv for each (as the automation script does).

If you get version conflicts:
```bash
# Use the automation script (handles this automatically)
python run_capstone.py

# Or manually use per-system venvs
cd /workspace/System1/solution
source .venv/bin/activate
# work with System 1

deactivate

cd /workspace/System2/solution
source .venv/bin/activate
# work with System 2

deactivate
```

## Common Issues and Solutions

| Issue | Solution |
|-------|----------|
| `ModuleNotFoundError: No module named anthropic` | Run `pip install -e ".[dev]"` in the system's directory |
| `401 Unauthorized` from API | Check ANTHROPIC_API_KEY is set and correct. If Vocareum key, also set ANTHROPIC_BASE_URL |
| Tests import wrong module | Verify venv is activated for that system |
| `pytest not found` | Run `pip install pytest` in the venv |
| System 2 tests skipped | Normal on first run! Run the system, then re-run tests |
| Tests timeout | Some make API calls. Use `pytest --timeout=300` for longer timeouts |

## Evidence Quality Checklist

Before writing your reflection brief:

- [ ] All evidence files exist (`evidence/system-*.log`)
- [ ] Each file is non-empty (not just headers)
- [ ] Files contain "PASSED" indicators
- [ ] Test counts match expected:
  - System 1: ~30 passed
  - System 2: ~30 passed (or 28 passed + 2 skipped initially)
  - System 3: ~35 passed
  - System 4: ~33 passed
- [ ] Files contain enough detail to answer reflection questions
- [ ] You can cite specific line numbers or test names

## Next Steps Checklist

1. ✅ Understand the four systems (read this guide)
2. ✅ Get access to course materials
3. ⏳ Run all four systems (automatically or manually)
4. ⏳ Verify evidence artifacts are captured
5. ⏳ Read reflection brief template
6. ⏳ Write reflection brief with citations
7. ⏳ Commit and push to GitHub
8. ⏳ Submit for grading

---

**Need help?** Check:
1. This reference guide for command syntax
2. EXECUTION_GUIDE.md for step-by-step walkthrough
3. Individual system README.md files in their solution/ directories
4. Test output files in evidence/ directory

