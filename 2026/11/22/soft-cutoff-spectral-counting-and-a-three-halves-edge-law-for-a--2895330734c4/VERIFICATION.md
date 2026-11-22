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

# Verification

The mathematical proof is in `RESULT.md`. Its nonstandard step is the uniform Hilbert–Schmidt discretization estimate, justified by summable squared derivatives and unit-cell Poincaré inequalities. The Hilbert–Schmidt comparison suffices for fixed trace powers of degree at least two; the degree-one trace is handled separately via the zeta-series diagonal. The limit spectral measure has no positive atoms, so fixed-threshold counting follows from weighted moment convergence without assuming uniformity as the threshold moves.

Run `python3 check.py` to check elementary integral constants, profile derivatives, edge coefficients, and finite matrix positivity. No software output establishes an infinite-dimensional theorem. The formulas for the profile near its two edges are sequential limits, with the exponent parameter tending to zero first.
