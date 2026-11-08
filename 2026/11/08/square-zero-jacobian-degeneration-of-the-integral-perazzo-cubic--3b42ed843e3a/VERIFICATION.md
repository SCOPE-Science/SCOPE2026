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

# Verification of the relative singular scheme

The file `verify_perazzo.py` uses Python 3 and SymPy (version constraints in `requirements.txt`). Its execution is reproduced in `verification-output.txt`.

The script symbolically differentiates the defining integral cubic, checks the determinant of the presentation matrix, and verifies the characteristic-dependent Jacobian ideals using exact Gröbner bases over the prime fields of characteristics 2, 3, 5, 7 and 11. For each field, it exhaustively computes the Hilbert function in degrees 0 through 8 from the actual leading monomial ideal and checks the predicted values.

The proof in `RESULT.md`, not this finite test, establishes the universal quantifiers over all fields and all degrees. In particular, the matrix-cokernel calculation on the smooth conic, the characteristic-two direct-sum calculation, and flatness over the integers are mathematical arguments, not inferred from the finite executions.

The classical cubic equation and the reduced singular plane come from Gondim–Russo; no independent mathematical audit has yet been conducted.
