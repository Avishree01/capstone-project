# Capstone Integration Guide

This document ties together all the documentation with the official task list.

## 📋 How This Package Relates to Official Tasks

### Your Harness (What I Built)
- **Automation:** `run_capstone.py` — Handles venv + dependencies + pytest
- **Validation:** `setup_helper.py` — Checks environment
- **Guides:** 8 documents explaining everything
- **Template:** `reflection-brief-template.md` — 19 questions to answer

### Official Tasks (What You Must Do)
1. Build environments & verify tests (30 pts)
2. Run agentic loop (30 pts)
3. Run context strategy (30 pts)
4. Validate Claude Code config (35 pts)
5. Run orchestrator (33 pts)
6. Organize evidence (automatic)
7. Complete brief (automatic once evidence is gathered)

### How They Connect

| Task | My Harness Helps How | Your Evidence |
|------|---------------------|-----------------|
| 1. Environments | `run_capstone.py` runs tests automatically | system-*-tests.log files |
| 2. Agentic loop | `CAPSTONE_TASKS.md` shows exact commands | traces with stop_reason |
| 3. Context strategy | `CAPSTONE_TASKS.md` shows compression run | budget.json, eval.json |
| 4. Claude Code | `CAPSTONE_TASKS.md` shows validator command | config output, .claude/ |
| 5. Orchestrator | `CAPSTONE_TASKS.md` shows run command | shift output, state size |
| 6. Organization | `CAPSTONE_TASKS.md` shows folder structure | evidence/ folder |
| 7. Brief | `reflection-brief-template.md` + examples | reflection-brief.md |

---

## 🚀 Your Complete Workflow

### Step 0: Orient Yourself (10 min)
```bash
cat 00-START-HERE.md              # Entry point
cat README_CAPSTONE.md            # Full overview
cat CAPSTONE_TASKS.md             # Exact tasks
```

### Step 1: Environment Setup (5 min)
```bash
python setup_helper.py            # Validate environment
export ANTHROPIC_API_KEY="..."    # Set if you have it
```

### Step 2: Build & Verify (30 min, Task 1 = 30 pts)
```bash
# For EACH system:
cd /workspace/<system>/solution
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -v > ~/system-X-tests.log
```

**Save logs as:**
- `evidence/system-1-agentic-loop/test-results.log`
- `evidence/system-2-context-strategy/test-results-initial.log`
- `evidence/system-3-claude-code/test-results.log`
- `evidence/system-4-orchestrator/test-results.log`

### Step 3: Run Agentic Loop (15 min, Task 2 = 30 pts)
```bash
cd system-1
python -m claims_intake.run --all
# Capture:
# - summary.md
# - One trace showing stop_reason values
```

**Save to:**
- `evidence/system-1-agentic-loop/summary.md`
- `evidence/system-1-agentic-loop/trace-example.json`

### Step 4: Run Context Strategy (20 min, Task 3 = 30 pts)
```bash
cd system-2
python -m retail_context.run --all
# Capture:
# - budget.json (check ≥50% reduction)
# - eval.json
# - eval_control.json

pytest tests/ -v > system-2-tests-final.log
```

**Save to:**
- `evidence/system-2-context-strategy/budget.json`
- `evidence/system-2-context-strategy/eval.json`
- `evidence/system-2-context-strategy/eval_control.json`
- `evidence/system-2-context-strategy/test-results-final.log`

### Step 5: Validate Claude Code Config (5 min, Task 4 = 35 pts)
```bash
cd system-3
python -m ecommerce_team_config . > output.txt
# Shows "ok" if validator passes
# Capture the .claude/ directory structure
```

**Save to:**
- `evidence/system-3-claude-code/test-results.log`
- `evidence/system-3-claude-code/validator-output.txt`
- `evidence/system-3-claude-code/.claude-structure.txt`

### Step 6: Run Orchestrator (20 min, Task 5 = 33 pts)
```bash
cd system-4
# First: seed warm tier
python -c "import json; from pathlib import Path; from shift_monitor.warm import WarmStore; w=WarmStore(Path('data/warm.sqlite')); w.initialize(); w.insert_many(json.load(open('fixtures/defects.json')))"

# Then: run shift
python -m shift_monitor run-shift \
  --shift C \
  --warm-db data/warm.sqlite \
  --since 2026-04-01T00:00:00Z \
  --recorded-response fixtures/recorded_responses/shift_C_2026-04-30.json \
  > shift-output.txt

# Capture:
# - shift-output.txt
# - du -b data/hot_state.json → byte size
# - grep "defects: \d\+ of \d\+" shift-output.txt
```

**Save to:**
- `evidence/system-4-orchestrator/test-results.log`
- `evidence/system-4-orchestrator/shift-output.txt`
- `evidence/system-4-orchestrator/hot-state-size.txt`
- `evidence/system-4-orchestrator/defects-summary.txt`

### Step 7: Write Brief (45 min, Task 7 = Depends on evidence)
```bash
cp reflection-brief-template.md reflection-brief.md
# Edit: Answer each question citing your evidence artifacts
```

**Key rule:** Every answer must cite at least one file from evidence/

**Example citation format:**
```markdown
**Answer:** The system uses stop_reason because...

From evidence/system-1-agentic-loop/trace-example.json:
- When stop_reason="tool_use" (line 42), the loop calls more tools
- When stop_reason="end_turn" (line 85), the loop terminates
- This proves that stop_reason directly controls termination
```

### Step 8: Submit (5 min)
```bash
git add evidence/ reflection-brief.md
git commit -m "Capstone submission: all systems tested, brief completed"
git push origin main
```

---

## 📊 Points Breakdown

| Task | Points | My Harness Role |
|------|--------|-----------------|
| 1. Build environments | 30 | Automates with run_capstone.py |
| 2. Agentic loop run | 30 | CAPSTONE_TASKS.md shows commands |
| 3. Context strategy run | 30 | CAPSTONE_TASKS.md shows commands |
| 4. Claude Code validation | 35 | CAPSTONE_TASKS.md shows commands |
| 5. Orchestrator run | 33 | CAPSTONE_TASKS.md shows commands |
| 6. Evidence organization | — | Folder structure in CAPSTONE_TASKS.md |
| 7. Brief completion | — | Template + citation guide |
| **TOTAL** | **158** | |

---

## 📁 Final Evidence Structure

```
evidence/
├── system-1-agentic-loop/
│   ├── test-results.log ........................ 30 tests passing
│   ├── summary.md ............................. From python -m claims_intake.run
│   └── trace-example.json ..................... Shows stop_reason values
│
├── system-2-context-strategy/
│   ├── test-results-initial.log .............. 28 pass, 2 skip
│   ├── budget.json ............................ Compression ≥50%
│   ├── eval.json .............................. Evaluation scores
│   ├── eval_control.json ...................... Control baseline
│   └── test-results-final.log ................. All 30 pass (after run)
│
├── system-3-claude-code/
│   ├── test-results.log ....................... 35 tests passing
│   ├── validator-output.txt ................... Should show "ok"
│   └── .claude-structure.txt .................. CLAUDE.md hierarchy
│
└── system-4-orchestrator/
    ├── test-results.log ....................... 33 tests passing
    ├── shift-output.txt ....................... Orchestrator run output
    ├── hot-state-size.txt ..................... Byte size of data/hot_state.json
    └── defects-summary.txt .................... 17 of 40 defects
```

---

## 🎯 Key Metrics to Track

### System 1: Claims Intake Agent
- ✅ 30 tests passing
- ✅ Each claim routed or escalated
- ✅ Trace shows `stop_reason` values (tool_use, end_turn)

### System 2: Context Strategy
- ✅ 30 tests passing (after run)
- ✅ Compression ≥ 50% (from budget.json)
- ✅ Name which evaluation question regressed

### System 3: Claude Code Config
- ✅ 35 tests passing
- ✅ Validator returns "ok"
- ✅ CLAUDE.md structure documented

### System 4: Quality Monitoring
- ✅ 33 tests passing
- ✅ Shift returns 17 defects (of 40 in warm tier)
- ✅ hot_state.json size < 50KB (tiny state)

---

## 📚 Reading Guide by Role

### If you're new to the project:
1. 00-START-HERE.md (3 min)
2. README_CAPSTONE.md (5 min)
3. CAPSTONE_TASKS.md (10 min) ← **Most important**
4. Dive into each task

### If you've done similar work:
1. QUICK_START.md (2 min)
2. CAPSTONE_TASKS.md (10 min) ← **Most important**
3. REFERENCE_GUIDE.md (as needed)

### If you need detailed walkthrough:
1. EXECUTION_GUIDE.md (start to finish)
2. CAPSTONE_TASKS.md (for specific commands)
3. reflection-brief-template.md (for brief writing)

---

## ⚡ Command Cheat Sheet

```bash
# Validate environment
python setup_helper.py

# Build & test all systems
python run_capstone.py

# Run individual tasks (from CAPSTONE_TASKS.md):
python -m claims_intake.run --all          # Task 2
python -m retail_context.run --all         # Task 3
python -m ecommerce_team_config .          # Task 4
python -m shift_monitor run-shift ...      # Task 5

# Write brief
cp reflection-brief-template.md reflection-brief.md
# Edit with your citations

# Submit
git add evidence/ reflection-brief.md
git commit -m "Capstone complete"
git push origin main
```

---

## ✅ Pre-Submission Checklist

- [ ] All 128 tests pass (30+30+35+33)
- [ ] evidence/ folder has all 4 system subdirectories
- [ ] System 1: summary.md + trace showing stop_reason
- [ ] System 2: budget.json ≥50%, eval.json, all tests pass on rerun
- [ ] System 3: validator output "ok", .claude/ structure documented
- [ ] System 4: shift output + state size + defect count
- [ ] reflection-brief.md completed
- [ ] Every brief answer cites at least one evidence file
- [ ] All files committed and ready to push

---

## 🎓 What You'll Learn

By following this workflow, you'll understand:

✓ How `stop_reason` controls agentic loop termination
✓ How to measure and achieve token compression
✓ How CLAUDE.md hierarchies configure AI behavior
✓ How tiered storage enables lightweight orchestration
✓ How to test complex systems and gather evidence
✓ How to defend architectural decisions with data

---

## 🚀 Get Started Now

1. Read CAPSTONE_TASKS.md completely
2. Follow the commands in Step 2 (Build & Verify)
3. Run one task at a time
4. Capture evidence in the structure shown
5. Write your brief citing that evidence

**Total time: ~2 hours**

Good luck! You've got this! 🎓

