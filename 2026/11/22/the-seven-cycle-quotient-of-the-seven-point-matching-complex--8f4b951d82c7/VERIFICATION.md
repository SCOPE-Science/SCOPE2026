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

# Reproducibility and limitations

Execute the embedded Python 3 standard-library verifier `VERIFY_M7_C7.py`: it regenerates the original face list, quotient cell orbits, oriented attaching loops, twelve homotopy-preserving cancellations, and the final three attaching degrees. Actual check outcome: `M7_C7_HOMOTOPY_OK`, with quotient cells (3,15,15), initial thirteen circle generators and final exponent magnitudes (0,21,42).

The independently implemented barycentric subdivision check `CHECK_BARYCENTRIC.py` requires the version of SymPy specified by `requirements.txt`. Actual run found quotient flag-cell counts (33,120,90), first boundary rank 32, remaining cycle matrix 88 by 90 of rank 88, Smith nonunit invariant factor 21, and second-homology rank two. Outcome: `BARYCENTRIC_INDEPENDENT_CHECK_OK`.

The homotopy equivalence depends on topological validity of generator–two-cell cancellations, not on Smith normal form alone. All finite cells are exhaustively enumerated. No infinite statement or external independent validation follows from these finite tests.
