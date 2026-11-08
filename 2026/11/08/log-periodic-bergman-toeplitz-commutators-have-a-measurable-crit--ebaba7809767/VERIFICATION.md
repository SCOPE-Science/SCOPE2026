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

# Reproducibility and verification

Run `python -m pip install -r requirements.txt` followed by `python CHECK.py`. The checker numerically evaluates beta integrals, complex gamma quotients, their exact recurrence, the monomial multiplicities and the simplified critical residue. The extracted checker passed 448 finite assertions with high-precision arithmetic. The analytic proof in RESULT.md, rather than any finite experiment, supplies the all-dimension and all-degree assertions, the sharp Schatten cutoff, and the sorted logarithmic asymptotic. No independent validation has been performed.
