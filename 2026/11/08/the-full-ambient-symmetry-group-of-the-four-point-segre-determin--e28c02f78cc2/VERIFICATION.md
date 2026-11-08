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

Exact check: run `python verify_segre_symmetry.py` with Python 3 and SymPy. Expected output includes `LIE_STABILIZER_DIM 6`, `FINITE_COMPONENTS 192`, and `EXACT_CHECKS_PASS`. It enumerates all 24 signed determinant terms and all signed candidate permutations, computes the 256-by-24 rational infinitesimal-action matrix and its rank 18, and checks the projective augmented rank 19. The result requires the algebraic-group normalizer argument given in RESULT.md; no assertion about abstract automorphisms of the divisor or external independent validation is made.
