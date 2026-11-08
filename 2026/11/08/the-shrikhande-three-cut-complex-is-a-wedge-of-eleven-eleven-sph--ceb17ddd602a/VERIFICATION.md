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

Run both programs using Python 3 without dependencies: `python3 verify_shrikhande_cut.py` and `python3 verify_dual_compare.py`. Their captured outputs are included separately. The first exhaustively verifies 65,162 nonempty cut faces, 32,573 matching pairs, and all 519,328 incidence arrows; checks that no directed cycles remain; and calculates the exact integral 13-by-2 Morse boundary and its unit 2-by-2 minor. The second builds the Alexander dual independently and computes its exact finite-field boundary ranks in four characteristics, including the previously studied rook comparator. Finite-field agreement alone would not prove the integral homotopy claim; its proof uses the exact signed Morse differential and the high-dimensional Hurewicz theorem. These computations pertain only to the described finite graph.
