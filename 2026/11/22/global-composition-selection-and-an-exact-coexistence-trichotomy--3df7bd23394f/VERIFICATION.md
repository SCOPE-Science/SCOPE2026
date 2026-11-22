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

# Mathematical reproducibility

Run `python checker.py` from this directory with Python 3 and SymPy. The program independently constructs the original population dynamics, checks the matched-feeding coordinate change, differentiates the scalar composition response, verifies the exact full Jacobian characteristic polynomials of both rational positive equilibria, and checks the continuous neutral family. Its output for the supplied sources is:

`PASS: exact transformation, frequency law, eigenvalue factorization, two hyperbolic witnesses and neutral continuum`

The theorem for all strictly positive rates satisfying the hypotheses follows from the algebraic steps and scalar differential-equation argument in `RESULT.md`, not from the finite witnesses alone. In particular, no claim is made about global convergence of the three absolute abundances, stochastic simulations, or independent verification.
