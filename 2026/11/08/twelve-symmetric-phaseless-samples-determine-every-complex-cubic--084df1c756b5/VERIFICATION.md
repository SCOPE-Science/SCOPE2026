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

# Verification of the mathematical assertion

The standalone `check_cubic_squares.py` reconstructs twelve exact algebraic sample locations, a twelve-by-sixteen real Hermitian lifting matrix, the kernel family, the four principal three-by-three determinant identities, and the exact coefficient determinant 6064128. It verifies the residual quartic determinant after setting the diagonal parameter to zero. The sign argument in `RESULT.md` then proves the rank obstruction without numerical approximations.

To replay, run `python check_cubic_squares.py` in a Python 3 installation with SymPy. Successful execution prints `CUBIC_THREE_SQUARES_CHECKS_PASS`. The program checks finite symbolic identities; phase retrieval and qualitative stability follow from the written general proof. This file records no independent external audit or validation.
