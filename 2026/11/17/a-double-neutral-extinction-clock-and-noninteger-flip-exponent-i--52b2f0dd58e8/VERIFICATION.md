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

The attached `check.py` is a standalone symbolic and numerical diagnostic that imports SymPy and uses only the model parameters explicitly stated in the result. It checks the quadratic coefficients and cancellations of the exact map by symbolic differentiation and polynomial composition, then checks three parameter instances with strictly positive initial conditions for 400,000 generations each.

Run `python check.py`. All symbolic identities and finite diagnostics passed in the delivered copy. The proof of the infinite-time limits requires the analytically derived invariant wedge and variation-of-constants estimates in \(`RESULT.md`\); finite numerical convergence alone is not a certificate of a limit.

The claim is local, restricted to \(1<p<2\). No independent audit has been performed.
