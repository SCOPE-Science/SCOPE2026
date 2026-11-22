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

# Verification record

The proof derives an exact moment-weighted Jacobi representation and checks the signed quadratic-form identity. The coefficient expansions yield the attractive \(1/j\) tail precisely when \(0<|a|<1\). The min–max argument with separated Dirichlet sine vectors proves the infinite and quantitative assertions without relying on finite truncation. For \(|a|\ge1\), pointwise multiplier bounds and the essential interval prove equality of full and essential spectra.

The supplementary checker `check_binomial_bergman.py` runs with the standard Python library and performs exact rational tests on finite vectors. Its expected output is `BERGMAN_BINOMIAL_EXACT_CHECK_OK 351`. This is not a proof of infinite dimensional conclusions and does not cover arbitrary real \(\alpha>-1\); those conclusions rest on the analytic argument.

A published novelty guarantee, independent audit, sharp counting asymptotic, and full point spectrum are not provided.
