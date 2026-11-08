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

# Computational and mathematical verification

Run `python CHECKER.py` with Python 3 and NumPy installed. The checker assembles the actual unit-indexed Fourier matrices, their proposed exact projector/Gram identities, and their expected complex-eigenvalue multisets. It tests levels 2 through 128 at several odd twists, traces through 2048, exact CRT congruences, and 27 even composite moduli through 120, comparing matrix eigenvalues numerically to predicted complex phases. Finite eigenvalue calculations are corroborative only; the all-modulus proof is the arithmetic Ramanujan/block/trace argument in `RESULT.md`.

The projector and Gram relations are exact symbolic consequences of Ramanujan sums; floating-point eigenvalue checks do not certify universality. The public independent-audit status remains `not_performed` with null evidence. The limitations include reliance on the standard quadratic Gauss-sum sign for odd prime factors and historical priority risk for an inaccessible earlier report.
