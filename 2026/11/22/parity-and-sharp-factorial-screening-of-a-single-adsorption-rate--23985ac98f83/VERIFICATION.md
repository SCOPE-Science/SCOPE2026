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

# Verification scope

The analytic argument in `RESULT.md` proves a result on the infinite tree. The accompanying `verify.py` is a finite-depth numerical consistency check, not a proof of any infinite-volume statement. Its two routes are (i) direct integration of the exact infinite-tree Volterra kernel and (ii) an explicit finite regular subtree recursion with the same one-root defect but without a change of variables.

Run `python verify.py` in an environment with Python 3, `numpy`, `scipy` and `mpmath`. The code checks all fifteen triples with degrees 3 and 4, marked rates 2 and 3, and separations 1–5. The tolerance is \(1.5\times10^{-7}\) for each absolute difference. A separate symbolic calculation in `RESULT.md` gives the exact degree-three, rate-two first- and second-shell corrections and supplies a stringent normalization check. The source-based comparisons and limitations appear in `REVIEW.md` and `AUDIT.json`. No external independent validation has been performed.
