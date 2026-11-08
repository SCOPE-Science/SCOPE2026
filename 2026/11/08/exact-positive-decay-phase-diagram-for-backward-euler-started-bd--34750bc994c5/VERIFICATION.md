---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducible verification

Run `python verify.py` with Python 3.10+ and SymPy 1.11 or later. The companion `requirements.txt` specifies the symbolic dependency. The script executes exact rational-function simplifications for the two-step monodromy trace, determinant, discriminant, starter relation and both step coefficients. It additionally verifies 234 rational admissible pairs over 60 updates each, four rational critical/contrast pairs over 120 updates each, and records explicit finite negative witnesses for six excluded pairs. Every predicted positive trajectory is checked for strict stepwise decrease.

The claimed **all-index if-and-only-if** result is established by the analytic eigenvalue, starter and oscillation arguments in `RESULT.md`; finite testing does not establish it by itself. Only the listed script and ordinary Python/SymPy are required. The arithmetic is exact for the symbolic identities and rational trajectories. No hidden data, external verification, or independent audit is asserted.
