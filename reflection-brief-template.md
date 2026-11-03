# Capstone Reflection Brief

> **Instructions:** Answer each question below, citing evidence from your own test runs. Generic answers without evidence will not pass. Each evidence artifact should be saved from running the system (test output, run logs, etc.).

## System 1: Claims Intake Agent (Stop-Reason-Driven Loop)

**What it is:** An agentic loop that processes intake conversations, calls tools to gather and classify information, and routes or escalates cases. Control flow is driven by `stop_reason`.

### 1.1 Termination Logic and Anti-Patterns
**Question:** Explain the loop's termination logic: how does it know when to stop, what `stop_reason` values trigger stops, and which anti-patterns does it avoid?

**Evidence Sources:**
- Test output: `evidence/system-1-tests.log`
- Key test files to cite: `tests/test_*.py`

**Answer:** (Citation required from your test output)

```
[Paste relevant test output showing stop_reason handling here]
```

### 1.2 Tool Integration
**Question:** What tools does the intake agent call? Why are they chosen for this workflow?

**Evidence Sources:**
- Test runs showing tool usage
- System 1 README: solution directory

**Answer:** (Citation required)

### 1.3 Design Rationale
**Question:** Why use `stop_reason`-driven control instead of explicit state machines? What trade-offs are being made?

**Evidence Sources:**
- Test patterns demonstrating control flow
- Code structure in the solution

**Answer:** (Citation required)

---

## System 2: Context Strategy (Token Compression for Long Conversations)

**What it is:** Compresses a long, multi-issue conversation to under half its tokens while preserving answerability. Uses position-aware strategy for retail support copilot.

### 2.1 Compression Mechanism
**Question:** How does the system compress tokens? What position-aware strategy is used, and how does it decide what to keep vs. discard?

**Evidence Sources:**
- Test output: `evidence/system-2-tests.log` (run twice: first with 2 skips, second after run completes)
- System 2 README

**Answer:** (Citation required from test output)

### 2.2 Answerability Preservation
**Question:** How does the system verify that compressed context still answers evaluation questions? What would fail if compression was too aggressive?

**Evidence Sources:**
- Test names and results
- Test run artifacts

**Answer:** (Citation required)

### 2.3 Token Measurement
**Question:** What metric proves compression worked? Show the before/after token count from your run.

**Evidence Sources:**
- Run output showing token counts
- Test results

**Answer:** (Citation with numbers required)

---

## System 3: Claude Code Config (CLAUDE.md Hierarchy)

**What it is:** A CLAUDE.md hierarchy with path-scoped rules, custom slash command, and a forked-context skill. Checked by a validator.

### 3.1 CLAUDE.md Structure
**Question:** Describe the CLAUDE.md hierarchy: what is in the root file? What are the path-scoped overrides? How does precedence work?

**Evidence Sources:**
- Test output: `evidence/system-3-tests.log` (35 tests expected)
- The actual CLAUDE.md files in the solution directory

**Answer:** (Citation required with example file paths)

### 3.2 Path-Scoped Rules
**Question:** Give an example of a path-scoped rule and explain why scoping it to that path makes sense for the monorepo.

**Evidence Sources:**
- CLAUDE.md files
- Test cases validating path scoping

**Answer:** (Citation required)

### 3.3 Custom Slash Command
**Question:** What does the custom slash command do? How is it invoked and what does it produce?

**Evidence Sources:**
- Test output showing command behavior
- CLAUDE.md defining the command

**Answer:** (Citation required)

### 3.4 Forked-Context Skill
**Question:** What is the forked-context skill? When and why would you fork context instead of running in the current session?

**Evidence Sources:**
- Test results
- Skill definition in CLAUDE.md or related files

**Answer:** (Citation required)

### 3.5 Validator
**Question:** What does the validator check? How does it prevent misconfiguration?

**Evidence Sources:**
- Test output showing validation checks
- Validator code or test assertions

**Answer:** (Citation required)

---

## System 4: Layer 3 Orchestrator (Multi-Shift Quality Monitoring)

**What it is:** Runs as a fresh session per shift, keeps state tiny through tiered storage and SQL pre-filtering, recovers from crashes, supports forked investigations.

### 4.1 Tiered Storage Architecture
**Question:** Describe the three tiers of storage in this system and why each tier is needed. How does SQL pre-filtering reduce work?

**Evidence Sources:**
- Test output: `evidence/system-4-tests.log` (33 tests expected)
- System 4 README and code structure

**Answer:** (Citation required with tier definitions)

### 4.2 Fresh Session per Shift
**Question:** Why start a fresh session per shift instead of maintaining one long session? What state must persist across shifts, and what is discarded?

**Evidence Sources:**
- Test cases demonstrating session lifecycle
- Session management code

**Answer:** (Citation required)

### 4.3 Crash Recovery
**Question:** How does the system recover from crashes? What is the recovery checkpoint, and what would be lost vs. preserved?

**Evidence Sources:**
- Test output showing crash/recovery scenarios
- Recovery logic in code

**Answer:** (Citation required)

### 4.4 Forked Investigations
**Question:** How can the orchestrator fork an investigation? What context is forked, and why would you fork instead of continuing in the main session?

**Evidence Sources:**
- Test output showing fork behavior
- Fork implementation details

**Answer:** (Citation required)

### 4.5 Design Trade-offs
**Question:** What is the trade-off between keeping state "tiny" and supporting forked investigations? Why not just keep everything in memory?

**Evidence Sources:**
- Test scenarios demonstrating the trade-off
- Code showing state management choices

**Answer:** (Citation required)

---

## Cross-System Synthesis

### 5.1 Commonalities
**Question:** What patterns appear across all four systems? What are they each solving for?

**Answer:** (Synthesis from all four systems)

### 5.2 Integration Points
**Question:** Could any of these systems be composed together? If you built a larger system, where would System 1, 2, 3, and 4 fit?

**Answer:** (Design reasoning)

---

## Evidence Artifacts Checklist

Before submission, verify you have:

- [ ] `evidence/system-1-tests.log` — Claims Intake Agent, 30 tests passing
- [ ] `evidence/system-2-tests.log` — Context Strategy, 28 passed + 2 skipped (from first run), then second run re-checking last 2 tests
- [ ] `evidence/system-2-run.txt` — Output from actually running the compression (if applicable)
- [ ] `evidence/system-3-tests.log` — Claude Code Config, 35 tests passing
- [ ] `evidence/system-4-tests.log` — Quality Monitoring, 33 tests passing
- [ ] `reflection-brief.md` — This file completed with citations

---

## Submission

1. **Fill in all answers** with citations to your evidence artifacts
2. **Save as** `reflection-brief.md` in `/workspaces/capstone-project/`
3. **Commit** to your repository:
   ```bash
   git add evidence/ reflection-brief.md
   git commit -m "Capstone project: evidence and reflection brief"
   git push origin main
   ```

