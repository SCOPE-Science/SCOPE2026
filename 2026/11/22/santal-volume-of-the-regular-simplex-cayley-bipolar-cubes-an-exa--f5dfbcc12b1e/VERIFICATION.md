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

# Verification and reproducibility

The exact all-dimensional claim is established in RESULT.md by: a sign-orthant decomposition and beta integration for the Cayley volume; an ordered-gap integral for the polar volume; a strict convexity proof of the Santaló minimizer; and a uniform asymptotic expansion. The crucial Euclidean gap Jacobian, regular-simplex dual identity, and axial-fiber bounds are explicitly reconstructed there.

Execute `python verify_cayley.py` with Python 3, NumPy and SciPy in the same directory. The checker obtains the polytope's primal volume from its vertices and the translated polar from direct halfspace intersection, independently of the sorting-chamber derivation. For dimensions two through six, three distinct axial centers are tested; the 35 volume comparisons all pass at numerical relative tolerance no larger than \(5\cdot10^{-8}\). The script also uses exact fractions for the first nontrivial denominator coefficients, checks the exact planar Santaló root, and prints larger-dimensional asymptotic diagnostics.

The finite calculations do not certify an infinite-dimensional theorem on their own. The limiting constant and uniqueness are analytic consequences of the displayed proof, and historical-priority review has not been independently completed.
