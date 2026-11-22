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

The exact proof is in `RESULT.md`. The executable `check_checkerboard.py` independently constructs generalized moment-Gram matrices for the full degree-at-most-\(q\) polynomial space on the unit sphere, using a quotient monomial basis with the last coordinate exponent at most one. For each tested pair it computes the full real symmetric generalized eigenvalue list of the compressed sign multiplication operator. The concentration spectrum is obtained from those eigenvalues by the affine map \(\lambda\mapsto(1+\lambda)/2\).

Executed as `python check_checkerboard.py` under Python 3 with NumPy and SciPy. All of \((q,d)=(1,2),(1,4),(2,4),(2,5),(3,6),(3,7)\) passed. The respective polynomial-space dimensions were 3, 5, 14, 20, 77, and 112. The maximum observed absolute eigenvalue error was \(2.3\times10^{-16}\). Each test uses the actual spherical even moments and checkerboard signed moments, and compares with the exact \((2/\pi)^q\) prediction.

The infinite-dimensional-parameter claim does not rest on numerical tests: it follows from parity-character selection and two exact Dirichlet moments in `RESULT.md`. This check does not establish literature priority, independent review, or higher-band behavior.
