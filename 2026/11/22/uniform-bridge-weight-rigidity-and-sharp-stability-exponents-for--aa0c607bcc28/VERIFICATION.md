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

# Reproducibility and mathematical checks
Run `python verify.py` from the same directory with Python 3, NumPy and SymPy. The program prints `VERIFY_OK 1072` on success. Actual checks include exact SymPy identities for the inverse resistance envelope, its maximizer and near-optimal exponent derivatives; complete transition-matrix row-sum, symmetry, nonnegativity, spectrum and upper/lower bound comparisons for 121 integer order pairs; 225 randomized feasible non-orbit-invariant edge-weight assignments; and finite-dimensional convergence checks for perturbed bridge or gateway holding.

The proof in RESULT.md establishes all quantifiers and inequalities analytically; floating-point eigenvalue checks cannot certify an infinite family. Checkable external inputs are the cited published papers, and no external training data or private infrastructure is needed.

**Unproved limits:** No exact optimizer-face enumeration is supplied. The literature comparison is not an independent novelty certificate. No external independent mathematical audit has been performed.
