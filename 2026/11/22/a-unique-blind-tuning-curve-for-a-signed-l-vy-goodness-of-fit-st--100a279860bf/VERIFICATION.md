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

The attached `verify.py` (Python with SciPy) executes numerical quadrature and bracketing for three shape parameters. A successful run showed 33 assertions, including each integrand's sign at six scaled arguments, opposite-sign endpoint values, a root residual below \(5\cdot10^{-8}\), correct signs around each root, and a strictly negative derivative. Its output for \(k=2.25\) was \(a_k=0.03754904932048\ldots\). These are numerical checks only; the analytic one-crossing inequality, fixed-alternative stochastic expansion, moment condition \(k>2\), and nondegenerate CLT are established in RESULT.md.

Source inspection used the available full public preprint https://arxiv.org/pdf/2308.00460 with attention to original equations (3)–(5), the null asymptotic theorem, alternative-distribution section, Gamma simulation tables, and the main proof appendix. The separate estimator-ratio paper was checked only at abstract level and is not presented as fully excluded. A historical-priority search cannot guarantee novelty. No independent audit is claimed.
