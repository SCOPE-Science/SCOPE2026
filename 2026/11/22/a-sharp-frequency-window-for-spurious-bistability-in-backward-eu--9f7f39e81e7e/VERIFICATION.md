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

# Verification scope

The mathematical proof is self-contained in `RESULT.md`, based on explicit radial inversion, its Jacobian determinant, the two roots of a quadratic equation in squared radius, and a monotone radial comparison argument. Strict boundary cases are checked algebraically. The derivation proves infinitely many parameters; finite numerical tests do not.

Run `python3 check.py` under a Python 3 standard-library environment. This runs exact-rational checks for \((b,c,a)=(3/5,4/5,-9/10)\) and \((4/5,3/5,-1)\), including invariant radii, exact radial multipliers, strict determinant positivity, and the quadratic window threshold. It also computes radial inverse steps by bracketed bisection from representative interior, intermediate, and exterior starting radii. The actual run printed both case tuples followed by `PASS: rational radii, Jacobian, multipliers, phase window and radial iterates`.

The checker cannot independently establish the infinite-dimensional range of parameters or literary priority; those require the algebraic proof and literature comparison. Only the isochronous single-oscillator cubic equation and exact fully implicit step are treated. Independent mathematical validation has not been performed.
