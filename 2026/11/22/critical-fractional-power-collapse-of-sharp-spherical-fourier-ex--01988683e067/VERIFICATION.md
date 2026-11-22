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

# Verification and limits
The exact leading exponents were checked algebraically: \(q_c=2d/(d-1)\), \(\beta=(d-1)/2\), \(d-1-\beta q_c=-1\), \(2/q_c=(d-1)/d\), and hence \(2/q_c-1=-1/d\). The gamma expression for the periodic mean agrees with \(m(3)=4/(3\pi)\). The proof establishes the uniform mean-zero oscillatory tail via a bounded periodic primitive and does not infer an infinite result from numerical quadrature.

The optional script `numeric_probe.py` evaluates six successive critical Bessel-cell integrals in each dimension \(d=3,4,5\), using `requirements.txt`; all computed cell increments were positive and the cumulative values increased. Finite floating-point quadrature is explicitly supplementary and cannot prove the all-dimension positivity or a tail estimate. The latter follows analytically from fixed-order Hankel asymptotics, while positive cells use Xu's Theorem 3.9.

Relevant primary-source comparisons: https://arxiv.org/abs/2610.19648 (Theorems 1.2, 1.3, 3.9 and §4); https://arxiv.org/abs/1710.10365 (Theorem 1); https://doi.org/10.1007/s00041-024-10120-z (different ordinary \(L^4\) setting). No independent external audit has been performed.
