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

# Reproducibility and limits

Run `python3 check.py` with Python 3 and no third-party packages. The checker independently evaluates the state recursion and the literal labelled-subset edge-choice recursion for \(2\le n\le6\), then checks the overlap-state martingale identity using exact rational arithmetic. It also checks base values and reports diagnostics for selected larger orders. These finite checks agree with the claimed formulas but are not a proof of their asymptotic expansion. The proof of the logarithmic coefficient is given in RESULT.md and depends on uniform two-tag survival bounds.

The literature comparison relies on identified public sources, with an unresolved full-text access limitation for the original randomized-greedy-matching article. No independent validation has been performed.
