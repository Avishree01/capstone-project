# Capstone Project: Complete Setup & Execution

## 📋 Project Overview

This capstone requires you to:
1. **Set up and run** four AI/ML systems from completed course projects
2. **Verify** each system passes its full test suite (128 tests total)
3. **Gather evidence** from running all systems
4. **Write a reflection brief** that cites evidence to explain each system's design

## ✅ What's Ready (Already in This Repository)

You have everything you need to run the capstone **once you have the course materials**:

### Scripts & Tools
- `run_capstone.py` — Automation script to run all four systems
- `setup_helper.py` — Validates your environment

### Documentation
- `SETUP_INSTRUCTIONS.md` — First-time setup (read this first!)
- `EXECUTION_GUIDE.md` — Complete step-by-step walkthrough
- `REFERENCE_GUIDE.md` — Quick reference and troubleshooting
- `reflection-brief-template.md` — Template for your reflection brief (fill this in)

### Directory Structure
- `evidence/` — Where test outputs are saved (created automatically)

## 🚀 Quick Start (Once Materials Are Available)

```bash
# From /workspaces/capstone-project/

# 1. Check environment
python setup_helper.py

# 2. Ensure course materials are in /workspace/ (see below)

# 3. Set API key (if available)
export ANTHROPIC_API_KEY="your-key-here"
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"  # if Vocareum key

# 4. Run all systems
python run_capstone.py

# 5. Write reflection brief
cp reflection-brief-template.md reflection-brief.md
# Edit with your citations

# 6. Submit
git add evidence/ reflection-brief.md
git commit -m "Capstone: all four systems tested and reflection brief completed"
git push origin main
```

## 📦 What's Missing: Course Materials

The capstone requires **four course project directories** that should be in `/workspace/` (note: /workspace, NOT /workspaces).

Expected structure:
```
/workspace/
├── Build a Claims Intake Agent with a stop_reason-Driven Loop/
│   └── exercises/03-dynamic-decomposition/solution/
├── Engineer a Long-Conversation Context Strategy for a Retail Support Copilot/
│   └── 04-assemble-and-locate/solution/
├── Configure Claude Code for a Multi-Surface Monorepo Team/
│   └── 04-plan-mode-and-explore-decision-doc/solution/
├── Build a Multi-Shift Quality Monitoring System with Claude Orchestration/
│   └── 04-fork-scratchpad/solution/
└── Project-Harness Engineering with Claude and Claude Code/
    ├── README.md
    └── reflection-brief-template.md
```

### How to Get These Materials

**Option A: Vocareum** (if you're in a Udacity course)
- Go to Cloud Resources tab in Vocareum
- Access the workspace or download materials
- Copy them to `/workspace/`

**Option B: Downloaded Files**
- If provided by instructor, extract to `/workspace/`

**Option C: GitHub Repository**
- Ask instructor for repository URL
- Clone to `/workspace/`

## 📚 Documentation Index

| Document | Purpose | Read When |
|----------|---------|-----------|
| `SETUP_INSTRUCTIONS.md` | Initial setup and prerequisites | First time |
| `EXECUTION_GUIDE.md` | Complete walkthrough (8 phases) | Before running |
| `REFERENCE_GUIDE.md` | Command reference and troubleshooting | While running |
| `reflection-brief-template.md` | Template for your answers | After getting evidence |

## 🎯 The Four Systems

### System 1: Claims Intake Agent (30 tests)
- **Concept:** Agentic loop driven by `stop_reason` values
- **Key Learning:** Loop termination logic and control flow
- **Evidence Location:** `evidence/system-1-tests.log`

### System 2: Context Strategy (30 tests)
- **Concept:** Compress long conversations while keeping them answerable
- **Key Learning:** Token compression and position-aware strategies
- **Evidence Location:** `evidence/system-2-tests.log`
- **Special:** May show "28 passed, 2 skipped" on first run (expected!)

### System 3: Claude Code Config (35 tests)
- **Concept:** CLAUDE.md hierarchy with path-scoped rules and custom commands
- **Key Learning:** Configuration-driven AI behavior
- **Evidence Location:** `evidence/system-3-tests.log`
- **No API key needed for this one**

### System 4: Quality Monitoring (33 tests)
- **Concept:** Tiered storage, fresh sessions, crash recovery, fork support
- **Key Learning:** Stateless orchestration and recovery patterns
- **Evidence Location:** `evidence/system-4-tests.log`

## ⚙️ Prerequisites

Check these before starting:

```bash
# Python 3.11+
python --version

# Git
git --version

# Environment (check after setting):
python -c "import os; print('API Key:', bool(os.environ.get('ANTHROPIC_API_KEY'))); print('Base URL:', os.environ.get('ANTHROPIC_BASE_URL'))"
```

## 📊 Expected Results

When everything works:
- ✅ 30 tests pass (System 1)
- ✅ 28-30 tests pass (System 2, may have 2 skipped initially)
- ✅ 35 tests pass (System 3)
- ✅ 33 tests pass (System 4)
- ✅ **Total: 128 tests** ✅

Evidence files saved to `evidence/` directory.

## 📝 Reflection Brief

After running all systems, you fill in `reflection-brief.md` by:

1. **Reading each question** in the template
2. **Referencing your evidence files** (the test output logs)
3. **Citing specific tests or output** that answer the question
4. **Explaining the design** based on what the tests reveal

Each answer must cite evidence! Generic answers will not pass.

## 🐛 Troubleshooting

**Common Issues:**

| Problem | Solution |
|---------|----------|
| "Course materials not found" | Ensure they're in `/workspace/` (capital W) |
| "401 Unauthorized" from API | Set ANTHROPIC_API_KEY and ANTHROPIC_BASE_URL |
| "Module not found" | Run `pip install -e ".[dev]"` in the system directory |
| "2 tests skipped" in System 2 | Normal! Run system, then re-run tests |

See `REFERENCE_GUIDE.md` for more troubleshooting.

## 📋 Submission Checklist

Before submitting:

- [ ] Course materials obtained and placed in `/workspace/`
- [ ] Environment variables set (ANTHROPIC_API_KEY at least)
- [ ] All four systems run successfully
- [ ] Evidence files exist in `evidence/` directory
- [ ] Reflection brief completed with citations
- [ ] All files committed to git
- [ ] Repository pushed to GitHub

## 🎓 Learning Objectives

By completing this capstone, you'll understand:

✓ How to operate a `stop_reason`-driven agentic loop
✓ How to engineer position-aware context compression
✓ How to configure AI behavior via CLAUDE.md hierarchies
✓ How to orchestrate multi-shift systems with tiered state
✓ How to test and validate complex AI systems
✓ How to explain architectural trade-offs with evidence

## 📞 Support

- **Command reference:** See `REFERENCE_GUIDE.md`
- **Step-by-step guide:** See `EXECUTION_GUIDE.md`
- **Initial setup:** See `SETUP_INSTRUCTIONS.md`
- **System details:** Check individual system README.md files in their solution/ directories

## 🚢 Next Action

**Immediate:** Read `SETUP_INSTRUCTIONS.md`

**Then:** Obtain course materials in `/workspace/`

**Then:** Follow `EXECUTION_GUIDE.md` to run all systems

**Finally:** Complete `reflection-brief.md` with citations from `evidence/` directory

Good luck! 🚀

