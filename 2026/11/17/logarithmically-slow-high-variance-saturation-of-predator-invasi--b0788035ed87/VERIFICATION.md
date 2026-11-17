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

# Verification of the high-variance invasion asymptotic

The proof is analytic and covers every fixed admissible positive parameter tuple. Its indispensable steps are: symmetry of the stationary Gaussian, the \(1/t\) tail of the even arctangent response, an integrable remainder after tail subtraction, dominated convergence, and the exact small-argument expansion of \(E_1\). In particular, finite numerical tests are not substituted for the infinite-variance proof.

The bundled `check.py` performs supplementary high-precision quadrature for one rational benchmark and compares \(\Lambda(s)-\Lambda_\infty\) with the proven two-term formula. Run `python check.py` with Python 3 and `mpmath` installed (tested with an available installation). The checker is not an independent validation and does not verify historical priority. The coefficient test uses the exact rational identity \(A=96/(1225\pi)\). The computed \(B\) is a truncated quadrature with a tail that is analytically \(O(1/T)\); no exact numerical value of \(B\) is claimed.

The scope is an infinite-time ergodic threshold, not a finite-time or sample-path extinction assertion. The supporting first-source result is arXiv:2611.11026v1, Section 8.2, Proposition 8.6.
