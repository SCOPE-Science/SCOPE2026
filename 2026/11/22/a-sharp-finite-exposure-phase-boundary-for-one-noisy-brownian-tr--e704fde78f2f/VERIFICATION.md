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

# Reproducible checks

Execute `python VERIFY.py` using Python 3 with `sympy` and `scipy` installed. The script constructs all covariance integrals independently, compares them symbolically with the cubic numerator, checks derivatives and endpoint identities exactly, isolates the unique critical-width root in \((0,1)\) using rational root intervals, and checks the vanishing-window expression. It also performs 75 independent numerical covariance-integral quadratures with piecewise exact integrands, and sampled bounded scalar optimization and threshold checks for several positive widths and noise values.

The exact global theorem is supported by the elementary sign proof in `RESULT.md`; finite sampling cannot certify uniqueness or a universal statement. No external proof assistant, independent reviewer, or independent mathematical audit is claimed. The floating-point critical width is descriptive; its exact definition is the cubic root in the stipulated interval.
