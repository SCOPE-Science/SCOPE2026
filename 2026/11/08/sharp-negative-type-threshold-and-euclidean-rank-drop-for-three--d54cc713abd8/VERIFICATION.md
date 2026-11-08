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

Run `python3 check.py` from the extracted package directory. It constructs field tables and evaluates the Fourier sums and rank-class frequencies over \(\mathbb F_4\) and \(\mathbb F_9\), then checks the symbolic formulas at several integer field orders and solves the monotone scalar root numerically. The exact-field calculations are independent finite checks, not a formal proof for every prime power; the all-field proof is given in RESULT.md. No external specialist audit has been performed.
