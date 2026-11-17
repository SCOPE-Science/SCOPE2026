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

# Reproducible checks and limits

Use `python3 verify.py` from the same directory. Only Python standard-library modules are required. The script checks exactly, with rational arithmetic, component-averaging derivatives and their connected-boundary formulas on every labeled tree of orders two through six, covering 1,441 trees and 43,614 active-edge subsets. It checks the contractivity classification and universal envelope on these shapes and the integer-optimal candidate for orders two through 500. It additionally gives exact primal-dual stationary certificates for distinct nearby inputs of five broom examples: orders five, six, nine, sixteen and fifty.

The finite checker is not an exhaustive verification for arbitrary tree order. Its KKT certificates show real finite projection pairs for selected examples, not an unrestricted theorem by themselves. General correctness requires the analytic active-cell realization, cut-gradient basis, subtree-boundary counting, and extremal-tree construction in RESULT.md. The literature comparisons do not replace external priority review.
