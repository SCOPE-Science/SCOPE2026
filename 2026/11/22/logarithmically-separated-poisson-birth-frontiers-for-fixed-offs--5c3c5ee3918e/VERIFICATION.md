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

# Reproducible arithmetic checks

Run `python verify.py` with Python 3 and no external libraries. It compares the exact marked-degree distribution obtained from the independent-parent generating function with exhaustive recursive-tree enumeration for \(n\leq8\). It also checks all individual degree probabilities up to \(n=12\), exact leaf probabilities, and numerically evaluates bounded-interval expected counts at \(n=400000\) for degrees \(0,1,2\).

The code verifies finite identities and provides non-exhaustive scaling diagnostics. It does **not** prove Poisson point-process convergence, tail uniformity, or historical novelty; those claims require the mathematical proof and literature comparison in the accompanying documents. No independent audit has been performed.
