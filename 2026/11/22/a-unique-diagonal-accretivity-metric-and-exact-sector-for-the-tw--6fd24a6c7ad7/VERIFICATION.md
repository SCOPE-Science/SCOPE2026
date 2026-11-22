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

# Reproducibility and scope

The standalone `checker.py` was run after creation from its actual package path, using Python with NumPy and SymPy. It returned `PASS: symbolic matrix identities and 120 finite SPD matrix cases`. Symbolic tests verify the exact two-by-two Butcher inverse, square, weighted symmetric blocks, unweighted determinant, and exact differentiated sector factor; finite spatial matrix tests compare weighted Hermitian blocks, exact general-eigenvalue sector formulas, positive coercivity, and Euclidean negative directions for deterministic positive-definite spatial factors in dimensions 1, 2, 3, and 5. The proof in `RESULT.md`, not the 120 cases, establishes unrestricted dimension and all positive coefficients.

No computational exhaustive certification over all matrices is claimed. The literature search could miss an equivalent analysis, and neither the finite checks nor this review constitutes independent audit. The statement assumes exact positive-definite factors on the gauge-fixed pressure space.
