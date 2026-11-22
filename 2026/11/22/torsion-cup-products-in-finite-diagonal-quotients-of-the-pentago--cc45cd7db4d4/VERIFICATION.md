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

The standalone `verify.py` runs using the Python standard library only and prints `PENTAGON_HOCHSTER_AND_GYSIN_INPUTS_OK` on success. It exhaustively lists all 32 subsets of the five-gon vertex set, computes induced-graph connectivity and cycle ranks, and obtains the integral Hochster ranks 1 in degrees 0 and 7 and 5 in degrees 3 and 4. It checks arithmetic groups for sample integers 2, 3, 4, 5, 7, 11 and 25.

These are **input and arithmetic cross-checks**, not an independent infinite-family proof. The mathematical argument uses the circle fibration, integrality of Euler classes, the Gysin long exact sequence, six-dimensional Poincaré duality and cup-product naturality as detailed in `RESULT.md`. The complete homotopy type of any quotient is not claimed.
