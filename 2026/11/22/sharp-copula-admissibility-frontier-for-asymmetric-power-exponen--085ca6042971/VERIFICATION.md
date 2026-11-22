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

The theorem in `RESULT.md` is an analytic global result. The key deductions independently checked are: (i) exact mixed derivative and its sign factor; (ii) positive-coordinate substitution with inverse and factored global infimum; (iii) the boundary asymptotic when either exponent is less than one; (iv) limiting cases where an optimizer occurs only at infinity.

For reproducibility, run `python3 CHECK.py`. The checker uses only the Python standard library and exact rational arithmetic. It tests selected threshold values, exact zero and negative-density witnesses, and finite-grid sanity checks. In particular \(H(4/9,4/9)=0\) for \(a=b=2\), \(\phi=729/256\), and \(H(4/9,4/9)=-37232/4782969\) for \(a=b=2\), \(\phi=3\). Its finite grid is **not** a proof for arbitrary real parameters, arbitrary interior points, or an infinite continuum.

Limits: the result only establishes copula existence of the specified candidate, not estimation, model fit, or sampling theory. Source comparisons do not prove absolute historical priority; a relevant earlier generalization had only preview-level access. No independent mathematical audit has been performed.
