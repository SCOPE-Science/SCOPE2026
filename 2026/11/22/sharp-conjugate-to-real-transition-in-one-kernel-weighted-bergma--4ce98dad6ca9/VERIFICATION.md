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

# Reproducibility and proof checks

The mathematical proof is self-contained in `RESULT.md`. The relevant identities have been independently verified in the included `checker.py`: the exact squared norm of the single-kernel projection, the quadratic angular reduction, numerical agreement of the claimed global maximizing sites with continuous one-dimensional optimization, and critical square-root/one-sided derivative laws.

Run `python checker.py` in a Python 3 environment with NumPy and SciPy. The checked package yielded `PASS 21896 finite assertions; theorem formulas checked numerically, not an infinite proof`. The numerical checks sample a finite list of parameters (including both sides of the transition and the critical parameter), and cannot establish uniqueness for all parameters; the analytic proof establishes the quantified conclusions.

Relevant source comparison: arXiv:2006.03290 (introduction and global existence theorem); DOI:10.1016/j.amc.2021.126749 (introduction, Section 5 one-kernel formula and Section 6 remarks); arXiv:2201.07228 (introduction, existence theorem, final remarks). No independent external mathematical validation was conducted.
