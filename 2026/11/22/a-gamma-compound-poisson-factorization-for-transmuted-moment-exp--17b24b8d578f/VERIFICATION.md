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

Run `python verify.py` from the same directory as this file with Python 3 and SymPy available. It checks exactly the rational Laplace-transform identity, cubic discriminant and root brackets, boundary factorizations, normalization, first moment, and a six-index exact-rational Poisson-count jump example at \((\alpha,\beta)=(1/9,1)\). Numerical evaluations across eight other parameter points are only illustrative.

For full quantified correctness, independently inspect the analytical inequalities in RESULT.md: for positive transmutation the root bounds \(A>2,B>1\) give two nonnegative terms, and for negative transmutation \(A>1,B>2\) yield \(E(t)\ge e^{-t}-e^{-2t}>0\); these cover every \(t>0\) and every admissible interior parameter. The endpoint kernel is checked separately. Integrability follows from the small-argument and exponential-tail bounds. The factorization gives all count Lévy intensities, not merely those computed by the checker.

Independent mathematical audit and exhaustive historical priority verification have not been performed. There is no assertion that a numerical grid proves global positivity.
