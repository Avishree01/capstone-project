# Quick Start Guide

## The 30-Second Version

```bash
# 1. Get course materials in /workspace/
# 2. Set API key (optional but recommended)
export ANTHROPIC_API_KEY="your-key"
export ANTHROPIC_BASE_URL="https://claude.vocareum.com"  # if voc- key

# 3. Verify everything
python setup_helper.py

# 4. Run all systems
python run_capstone.py

# 5. Write brief
cp reflection-brief-template.md reflection-brief.md
# Edit reflection-brief.md with citations

# 6. Submit
git add evidence/ reflection-brief.md
git commit -m "Capstone complete"
git push origin main
```

## Files You Need to Read (In Order)

1. **GETTING_STARTED.txt** (5 min)
2. **README_CAPSTONE.md** (5 min)
3. **SETUP_INSTRUCTIONS.md** (5 min)
4. **EXECUTION_GUIDE.md** (10-30 min)
5. **reflection-brief-template.md** (5 min + 30-45 min to fill in)

## Key Facts

| Item | Value |
|------|-------|
| Python | 3.14.2 ✓ |
| Git | Configured ✓ |
| Tests Expected | 128 total |
| Test Files | 4 systems |
| Documentation | 7 guides |
| Automation | 2 scripts |
| Time Estimate | ~100 minutes |

## The 4 Systems

| System | Tests | Focus |
|--------|-------|-------|
| 1. Claims Intake | 30 | stop_reason loop |
| 2. Context Strategy | 30 | Token compression |
| 3. Claude Code | 35 | CLAUDE.md config |
| 4. Quality Monitor | 33 | Tiered storage |

## Common Issues

| Problem | Solution |
|---------|----------|
| Materials not found | Place in `/workspace/` (capital W!) |
| API 401 error | Check ANTHROPIC_API_KEY and _BASE_URL |
| Tests skip | System 2 normal on first run |
| Module not found | Run `pip install -e ".[dev]"` |

## Commands Quick Ref

```bash
# Validate environment
python setup_helper.py

# Run all systems (takes ~20 min)
python run_capstone.py

# Check evidence
ls evidence/

# View test output
grep PASSED evidence/system-*.log
```

## Files You'll Create

- `reflection-brief.md` (copy of template, filled in with evidence)
- `evidence/system-1-tests.log` (auto-generated)
- `evidence/system-2-tests.log` (auto-generated)
- `evidence/system-3-tests.log` (auto-generated)
- `evidence/system-4-tests.log` (auto-generated)

## Success Criteria

✅ All 128 tests pass
✅ Evidence files exist in `evidence/`
✅ Reflection brief completed with citations
✅ All files committed to git
✅ Repository pushed to GitHub

---

**Start Here:** `cat GETTING_STARTED.txt`
