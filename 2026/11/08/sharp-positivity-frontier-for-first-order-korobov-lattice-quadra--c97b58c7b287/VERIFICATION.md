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

# Reproducibility and proof boundary

Run `python3 verify.py` from this directory with Python 3.9 or newer. The code requires only the standard library and independently evaluates the quadrature kernel and kernel means by exact-form polynomial-times-sine primitives on explicit subintervals. It computes the weight vector by Gaussian elimination, separately evaluates the theorem's closed formulas, and compares the two for \(N=2,\ldots,12\) and \(\gamma/\Gamma_N\in\{0.5,0.9,1.1,2.0\}\). It also compares the exact bubble and endpoint-hat formulas against independently segmented integrals and numerically checks the asymptotic constant.

Executed result: `VERIFY_OK 44 direct linear-system comparisons; asymptotic checks passed`.

All numerical tolerances in the code apply to finite floating-point cross-checks; the infinitely many grid sizes, exact threshold boundary and asymptotic law are proved symbolically in `RESULT.md`. No external formal proof system or independent validation has been used. Any checks of novel claims beyond the stated one-dimensional setting remain unperformed.
