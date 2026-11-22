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

# Reproducibility and scientific limits

Run `python verify_peano.py` using Python 3 and SymPy. The program recalculates both quadrature rules and the exact Peano-kernel polynomials rather than consuming precomputed output; it does not access any network resources. A successful execution prints **PASS**, exactly 39 strictly positive algebraic rational-interval certificates, twelve exact polynomial-moment identities, the sharp ratio \(c_*\), and the minimax Lobatto weight \(c_*/2\).

The sign proof uses Bernstein coefficients over the *entire* polynomial subintervals, not values sampled on a grid. The square roots \(\sqrt3\), \(\sqrt5\), and \(\sqrt{15}\) are bracketed by exact integer-square-root fractions with denominator \(10^{70}\); the lower endpoint of each required exact rational interval is strictly positive. Piecewise identities, symmetry, the Peano integral formula, and the smooth-bump sharpness argument in `RESULT.md` complete the infinite-dimensional theorem. The script checks finite algebraic obligations; it is not a substitute for the stated functional-analytic proof.

This is a one-sign sixth-derivative result, with no claim for mixed signs, noisy function values, or floating-point certified interval arithmetic. The only assessment performed is the self-review. Independent audit: not yet performed.
