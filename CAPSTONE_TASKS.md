# Capstone Project - Specific Tasks

Based on the official task list, here are the exact steps you need to complete:

## ✅ Task 1: Build and Verify All Four Environments (30 points)

**What to do:**
- Create a venv for each system
- Run `pip install -e ".[dev]"` in each repo
- Run `pytest tests/ -v` in each repo
- Save passing output (30 + 30 + 35 + 33 = 128 tests total)
- Note: System 2 shows 28 passed, 2 skipped initially (until Task 3)
- Document any environment failures you hit and fix them

**Evidence to capture:**
- `system-1-tests.log` — 30 tests passing
- `system-2-tests.log` — 30 tests (28 pass, 2 skip initially)
- `system-3-tests.log` — 35 tests passing
- `system-4-tests.log` — 33 tests passing

---

## ✅ Task 2: Run the Agentic Loop (30 points)

**System 1: Claims Intake Agent**

Commands to run:
```bash
cd /path/to/claims-intake-agent
python -m claims_intake.run --all
```

**Evidence to capture:**
1. Save `summary.md` (or similar output from run)
2. Get one trace from `runs/<timestamp>/`
3. Verify each claim routes or escalates correctly
4. Verify trace shows:
   - `stop_reason` = `tool_use` (continues looping)
   - `stop_reason` = `end_turn` (stops)

**For your brief:** Understand how `stop_reason` values control the loop termination and tool call sequences.

---

## ✅ Task 3: Run the Context Strategy (30 points)

**System 2: Context Strategy**

Commands to run:
```bash
cd /path/to/context-strategy
python -m retail_context.run --all
```

**Evidence to capture:**
From `runs/<run_id>/`:
1. `budget.json` — Shows compression ratio (≥50% reduction)
2. `eval.json` — Evaluation question scores
3. `eval_control.json` — Control baseline

**Key metric:** Look for the budget reduction (should be ≥50%).

**Then re-run tests:**
```bash
pytest tests/ -v
```

Save output as System 2's final test evidence (all 30 should now pass).

**For your brief:** Understand which evaluation questions regressed and why compression works.

---

## ✅ Task 4: Validate the Claude Code Config (35 points)

**System 3: Claude Code Config**

Commands to run:
```bash
cd /path/to/claude-code-config
python -m ecommerce_team_config .
```

Expected output: `ok`

**Evidence to capture:**
1. Validator output (should say `ok`)
2. The `.claude/` directory structure:
   - Show glob patterns in rule files
   - Show `/review` command definition
   - Show forked context skill with `allowed-tools` and `context: fork`

**For your brief:** Explain the CLAUDE.md hierarchy, path-scoped rules, custom commands, and the forked-context skill.

---

## ✅ Task 5: Run the Orchestrator (33 points)

**System 4: Quality Monitoring Orchestrator**

**Step 1: Seed the warm tier (one-time):**
```bash
python -c "import json; from pathlib import Path; from shift_monitor.warm import WarmStore; w=WarmStore(Path('data/warm.sqlite')); w.initialize(); w.insert_many(json.load(open('fixtures/defects.json')))"
```

**Step 2: Run the orchestrator:**
```bash
python -m shift_monitor run-shift \
  --shift C \
  --warm-db data/warm.sqlite \
  --since 2026-04-01T00:00:00Z \
  --recorded-response fixtures/recorded_responses/shift_C_2026-04-30.json
```

**Evidence to capture:**
1. Shift output (console output from running orchestrator)
2. Byte size of `data/hot_state.json` (shows state size)
3. Count of defects returned vs warm-tier total (should be 17 of 40)

**For your brief:** Explain the tiered storage (warm, hot, transient), SQL pre-filtering, session freshness per shift, and recovery via warm-tier.

---

## ✅ Task 6: Organize Evidence (organized, ready for citation)

**Create one folder per system:**
```
evidence/
├── system-1-agentic-loop/
│   ├── test-results.log (30 tests passing)
│   ├── summary.md (from python -m claims_intake.run)
│   └── trace-example.json (one run trace showing stop_reason)
│
├── system-2-context-strategy/
│   ├── test-results-initial.log (28 pass, 2 skip)
│   ├── budget.json (compression ≥50%)
│   ├── eval.json
│   ├── eval_control.json
│   └── test-results-final.log (30 pass)
│
├── system-3-claude-code/
│   ├── test-results.log (35 tests passing)
│   ├── validator-output.txt (expect "ok")
│   └── .claude-structure.txt (show hierarchy)
│
└── system-4-orchestrator/
    ├── test-results.log (33 tests passing)
    ├── shift-output.txt (orchestrator run output)
    ├── hot-state-size.txt (byte size of data/hot_state.json)
    └── defects-summary.txt (17 of 40)
```

---

## ✅ Task 7: Complete the Brief (19 questions, cite evidence)

**Copy the template:**
```bash
cp reflection-brief-template.md reflection-brief.md
```

**Answer each question using YOUR OWN RUN EVIDENCE:**

### Section 1: System 1 - Claims Intake Agent (4 questions)

Example citation:
```
From evidence/system-1-agentic-loop/trace-example.json:
The loop continues when stop_reason="tool_use" (line 42) because...
The loop terminates when stop_reason="end_turn" (line 58) because...
```

### Section 2: System 2 - Context Strategy (3 questions)

Example citation:
```
From evidence/system-2-context-strategy/budget.json:
Original tokens: 5,432
Compressed tokens: 2,480
Reduction: 54.3% (exceeds 50% target)

Control regression: Question 7 dropped from 0.92 to 0.87...
```

### Section 3: System 3 - Claude Code Config (5 questions)

Example citation:
```
From evidence/system-3-claude-code/.claude-structure.txt:
CLAUDE.md hierarchy shows:
- Root: global rules
- /apps/web/: path-scoped overrides
- /apps/mobile/: different path-scoped rules

The /review command is defined at root level and...
The forked-context skill allows...
```

### Section 4: System 4 - Quality Monitoring (5 questions)

Example citation:
```
From evidence/system-4-orchestrator/shift-output.txt:
Warm tier pre-filter returned 17 defects of 40 total (42.5% reduction).
Hot state file (data/hot_state.json) is 8,456 bytes.
Session ran fresh for shift C, recovered from warm tier in 234ms...
```

### Section 5: Cross-System (2 synthesis questions)

Synthesize patterns across all four systems.

---

## 📋 Checklist Before Submission

- [ ] All 4 venvs created and tested (128 tests passing)
- [ ] Task 2 evidence captured: agentic loop traces with stop_reason values
- [ ] Task 3 evidence captured: compression metrics ≥50%, eval scores, re-run tests all pass
- [ ] Task 4 evidence captured: validator output "ok", .claude/ structure documented
- [ ] Task 5 evidence captured: orchestrator shift output, state size, defects count
- [ ] Evidence organized in `evidence/` folder (one per system)
- [ ] reflection-brief.md completed with citations to YOUR evidence
- [ ] Every answer cites at least one artifact from evidence/
- [ ] All files committed to git
- [ ] Ready to push to GitHub

---

## Key Points for Your Brief

**System 1 (Agentic Loop):**
- Cite specific `stop_reason` values from your trace
- Show how tool calls sequence based on stop_reason
- Explain why this is better than state machines

**System 2 (Context Strategy):**
- Cite your actual compression percentage from budget.json
- Name which evaluation questions regressed
- Explain the position-aware strategy

**System 3 (Claude Code Config):**
- Show the CLAUDE.md file hierarchy from your validator run
- Cite glob patterns and path scoping from rules
- Explain the forked-context skill

**System 4 (Orchestrator):**
- Cite defect counts (17 of 40)
- Show state file size from your run
- Explain tiered storage tiers and session freshness

---

## Commands Quick Reference

```bash
# Task 1: Build and verify
cd system-1
python -m venv .venv
source .venv/bin/activate
pip install -e ".[dev]"
pytest tests/ -v > system-1-tests.log

# Task 2: Run agentic loop
python -m claims_intake.run --all
cp summary.md evidence/system-1-agentic-loop/
cp runs/*/trace.json evidence/system-1-agentic-loop/

# Task 3: Run context strategy
python -m retail_context.run --all
cp runs/*/budget.json evidence/system-2-context-strategy/
pytest tests/ -v > system-2-tests-final.log

# Task 4: Validate Claude Code config
python -m ecommerce_team_config . > config-output.txt

# Task 5: Run orchestrator (seed first)
python -c "..."  # seed command
python -m shift_monitor run-shift ... > shift-output.txt

# Task 6: Organize
mkdir -p evidence/{system-1-agentic-loop,system-2-context-strategy,...}
# Copy artifacts to respective folders

# Task 7: Write brief
cp reflection-brief-template.md reflection-brief.md
# Edit with citations
```

---

**Your evidence is your proof. Cite it liberally in your brief!**
