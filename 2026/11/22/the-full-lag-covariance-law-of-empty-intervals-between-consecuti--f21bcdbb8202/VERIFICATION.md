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

# Reproducibility and scope

The analytic proof uses: (i) the disjoint representation of non-perfect-power \(k\)-full integers as \((a\lambda)^k\); (ii) rational independence of \(1\) and any finite set of reciprocals \(1/\lambda\), as established in the cited 2025 source; (iii) Kronecker–Weyl equidistribution; (iv) the inequality \(\sum_\lambda 1/\lambda<\infty\); and (v) direct circular-overlap integration. All steps are displayed in `RESULT.md`.

Run `python3 verify_autocorrelation.py` beside this file. The code checks **eight** precisely specified squarefree bases \(m=2,3,5,6,7,10,11,13\), with \(\lambda=m\sqrt m\), over **500,000** base windows for lags \(1,2,3,4,7,13,29\). The checker marks each occurrence using Python's exact-integer `math.isqrt`, then compares its empirical frequencies against the finite-parameter theoretical products to tolerance 0.003. It also checks local first and second overlap moments by midpoint quadrature, and endpoint, strict positivity, and normalization identities.

Computational corroboration of finitely many rays cannot establish infinite products, irrational equidistribution, absolute continuity, or scientific originality. The proof provides those analytic steps, subject to the cited rational-independence theorem. No independent mathematical audit has been performed.
