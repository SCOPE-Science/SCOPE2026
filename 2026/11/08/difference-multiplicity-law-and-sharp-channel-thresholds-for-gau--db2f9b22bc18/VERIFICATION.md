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

# Reproduction
Run `python -m pip install -r requirements.txt` and `python CHECK.py`. The checker reports 2656 checks for this package. It rebuilds complete sample-domain Hermitian matrices, uses independent block singular-value predictions, checks generalized Vandermonde ranks and kernel dimensions with symbolic exact arithmetic, and checks a symmetric trace-one exception. The analytic all-parameter proof, including positive generalized Vandermonde nonsingularity and trace-one genericity, is in `RESULT.md`; a finite checker alone cannot certify infinitely many frequencies, bins or widths. No independent audit was performed.
