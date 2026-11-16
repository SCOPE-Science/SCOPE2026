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

# Reproduction and proof limits

The sole program is `CHECK.py` (Python standard library only): run `python CHECK.py` in a directory containing the embedded file. A recorded execution passed 457 finite assertions. It verifies rational product-remainder inequalities for sample indices, the exact power-series Bessel equation for finite coefficients, finite Laguerre identities, high-precision numerical values of the covariance correction, and rational charged-intensity identities.

The mathematical proof independently establishes the expansion for all positive integer orders by summing an infinite absolutely convergent majorant after the Bonferroni inequality. Convergence of smooth Gaussian fields additionally uses a standard compact Gaussian tightness argument. Convergence of zero measures relies on regularity via the vector Bulinskaya lemma and deterministic inverse-function stability. No finite checker could establish those universal statements by exhaustive enumeration; their assumptions and limitations are stated in `RESULT.md`.

For source verification, compare the exact covariance with arXiv:2012.12298v1, Section 5.4, or arXiv:2610.13531v1, Section 2.3. The fixed-order intensities appear in arXiv:2605.17296v1 and arXiv:2610.13531v1, while the new analysis supplies the spatial scaling, second-order covariance remainder, and charged zero-process convergence. No independent external mathematical review has been carried out.
