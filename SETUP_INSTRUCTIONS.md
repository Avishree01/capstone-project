# Capstone Project Setup Instructions

## Prerequisites Check

✅ Python 3.11+ is available: Python 3.14.2
✅ Git is available
✅ Terminal is available

## What's Missing

The capstone requires access to four course project directories. According to the assignment description, these should be located in `/workspace/` with this structure:

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

## Instructions to Proceed

### Step 1: Access Course Materials

In your Vocareum/Udacity workspace:

1. Open the **Cloud Resources** tab
2. Look for access to the course project files
3. Copy the paths or download the course materials

Alternatively, if you have a download link or GitHub repository with these materials, please provide it.

### Step 2: Set Environment Variables

Once you have the materials available in your environment:

```bash
# For Claude API access (required for 3 of 4 systems)
export ANTHROPIC_API_KEY="your-api-key-here"

# If using Vocareum key (starts with 'voc-'), also set:
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"

# Verify they're set:
python -c "import os; print('Key:', bool(os.environ.get('ANTHROPIC_API_KEY')), 'Base URL:', os.environ.get('ANTHROPIC_BASE_URL'))"
```

### Step 3: Run Automated Setup Script

Once materials are in place and environment is configured, run:

```bash
cd /workspaces/capstone-project
python run_capstone.py
```

This will:
- Set up Python virtual environments for each of the 4 systems
- Install dependencies for each
- Run test suites (expecting 30 + 30 + 35 + 33 = 128 tests total)
- Capture evidence artifacts
- Generate a baseline for the reflection brief

## Expected Test Results

| System | Path | Tests |
|--------|------|-------|
| 1. Claims Intake Agent | System 1 | 30 ✓ |
| 2. Context Strategy | System 2 | 30 ✓ (28 pass, 2 skip initially) |
| 3. Claude Code Config | System 3 | 35 ✓ |
| 4. Quality Monitoring | System 4 | 33 ✓ |

## Deliverables

After running all systems:

1. **Evidence Artifacts** (in `/workspaces/capstone-project/evidence/`)
   - `system-1-tests.log` - Claims Intake Agent test output
   - `system-2-tests.log` - Context Strategy test output
   - `system-2-run.txt` - Context Strategy run output
   - `system-3-tests.log` - Claude Code Config test output
   - `system-4-tests.log` - Quality Monitoring test output

2. **Reflection Brief** (in `/workspaces/capstone-project/`)
   - `reflection-brief.md` - Completed brief with evidence citations

## Questions?

If you're stuck:
1. Verify Python version: `python --version`
2. Check API key is set: `python -c "import os; print('ANTHROPIC_API_KEY' in os.environ)"`
3. Verify materials location
4. Review the individual system README.md files in their solution/ directories

---

**Next Action:** Provide the path to the course materials or download link.
