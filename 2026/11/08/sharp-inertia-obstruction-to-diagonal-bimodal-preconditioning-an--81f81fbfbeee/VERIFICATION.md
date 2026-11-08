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

# Verification and limits

The complete proof is in `RESULT.md`. The included `verify.py` is standalone Python 3 source with NumPy as its sole nonstandard dependency. Running `python verify.py` on the delivered source returned `PASS 900 finite checks; analytic universal proof is in RESULT.md`.

The checks cover dimensions three through seventeen, multiple positive weighting patterns, arbitrary positive diagonal comparison factors, and randomly generated invertible symmetric hollow matrices. Assertions use eigenvalue tolerances of at most \(5\times10^{-11}\). The analytic proof covers *all* stated dimensions and matrices, not just finite diagnostics. No claim is made about the source paper's smoothed/logarithmic bimodal penalty, finite precision, or iterative convergence. Independent audit is not performed.
