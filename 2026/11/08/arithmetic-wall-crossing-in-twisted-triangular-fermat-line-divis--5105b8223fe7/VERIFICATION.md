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

# Reproducibility

The sole standalone program is `verify.py`; execute it with `python3 verify.py`. It uses only Python 3's standard library. It enumerates all projective points for 11,994 parameter cases over six indicated prime fields and compares the zero set of the three-factor polynomial to the closed finite-étale counting expression. It constructs a cubic field extension by an explicit irreducible polynomial and separately enumerates the projective zero set over the extension. The observed output was:

`TWISTED_CEVA_EXACT_CHECK_OK prime_cases=11994 F7=3 F343=3072`

These are finite tests only. The all-field proof is the line-family intersection classification, finite-étale normalization, and the Grothendieck-ring scissors calculation in `RESULT.md`. No independent mathematical audit has been performed. A historical-priority risk for equivalent older arithmetic formulas remains.
