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

# Reproducibility checks and limitations

The complete analytical argument appears in `RESULT.md`. Run `python3 check.py` using Python 3 with no external packages. The program verifies (i) exact integer signed-block identities for several integer block ratios, (ii) finite normalized Lyapunov exponent bounds with an independent stable logarithmic-norm evaluation, (iii) rational inversions of the universal CDF and the exact mid-block CDF difference, and (iv) numerical time-histogram values for both kinds of cutoff in a large finite block. These tests do not substitute for the limit proof, do not test the full planar map numerically, and do not constitute independent review. The source map's differentiability, boundary exclusions and parameter range are those established in arXiv:2206.09508v1.

The empirical measure concerns time indices and normalized finite-time rates, not the trajectory's spatial empirical measure. Independent mathematical audit: not performed.
