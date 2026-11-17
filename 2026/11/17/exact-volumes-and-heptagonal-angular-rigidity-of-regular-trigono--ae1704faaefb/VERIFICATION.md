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
# Reproducibility and limits

Run the embedded standalone program with `python VERIFY.py` using Python 3.9 or later. It depends only on the standard library. The executed program returned success and printed eleven complete ordered-facet determinant sweeps at orders \(5,6,7,8,9,10,11,12,15,20,32\), an exact integer cyclotomic computation of the seven-vertex Hessian coefficient arrays, verification of all 49 Hessian symmetries and circulant relations, exact matching of the four Fourier eigenpolynomials, and seven independent finite-difference comparisons of the Hessian first row. It also reconstructed the seven-vertex volume as \(0.389054556345294\ldots\), and its nonzero Fourier eigenvalues as approximately \(-0.2345350103\), \(-0.6794676280\), and \(-1.0312701434\).

The proof of the all-order statement is the determinant identity and finite trigonometric-sum calculation in RESULT.md. The negative-eigenvalue assertion is proved by exact cyclotomic algebra and rational sign bounds; numerical checks do not establish global maximality or certify any independent review. The source article's global upper bound of \(2/5\) is not improved by this work, and historical originality remains subject to independent literature review.
