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

The explicit monomial matrix coefficients were independently reconstructed from radial integrals. The numerical checker `check_flat_toeplitz.py` passed 135 assertions using SciPy and NumPy, including normalized finite-commutator identities, the modified-Bessel maximizer, and convergence of finite Jacobi norms. Reproduce with `python check_flat_toeplitz.py` after installing `numpy` and `scipy`.

The analytic evidence is contained in `RESULT.md`: (i) finite-support quadratic-form congruence, (ii) saddle bounds and ratio-one property for the Jacobi bonds, (iii) a rank/block proof of the exact singular counting coefficient, and (iv) Bessel scaling with uniform tail control and long-block norm lower bounds. Computation does not establish the infinite claims and no independent audit is represented.
