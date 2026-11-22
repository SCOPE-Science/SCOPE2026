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

# Verification details

The general theorem is established by the four analytic steps in RESULT.md, not by finite samples. For \(f(x)=1+x^2\), both untransformed integrals have exact elementary antiderivatives; the transformed Gaussian formulas and cancellation-free residual identities are implemented in `verify.py`. The script uses only Python's standard library to compute Gauss–Legendre nodes and weights, checks rules of orders 1, 2, 3, 4, 8, and 12, and tests multiple distances. The second polynomial \(f(x)=1+x^2+x^4\) checks the different limiting constant \(C_f=4/3\).

Run `python verify.py` in the directory containing `verify.py`. On the checked environment the output was `PASS 208 positive, error-identity and asymptotic diagnostics`. Some direct differences involving terms of size \(d^{-2}\) suffer catastrophic floating-point cancellation; the script uses cancellation-free formulas when testing small-distance limits and deliberately permits appropriate direct-subtraction roundoff in other comparisons. No interval arithmetic or machine-checked universal proof is claimed. An independent audit has not been performed.
