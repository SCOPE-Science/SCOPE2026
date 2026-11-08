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

# Reproduction and limits

The proof in `RESULT.md` gives an exact ordered-side cone parameterization, a complete nonnegative polynomial remainder, and two sharpness and equality arguments. Run `python check.py` with `sympy>=1.12` to reproduce the algebraic certificates and diagnostic samples. The execution completed with `SYMBOLIC_IDENTITY_OK; NUMERIC_CHECKS= 30015`.

The symbolic checker reduces the square-root parameter by the exact defining relation \(r^2=1-\eta+\eta^2\). Positivity of the remainder is established mathematically for \(0<\eta<1\); the 30,015 numerical checks are not a substitute for universal quantification. Existence and global maximality at the equilateral container use [1, Theorem 1], inspected in its full primary text. No external independent mathematical audit was performed.
