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

Run `python3 verify.py` with Python 3 standard library. The independent finite enumeration includes 40 labeled complete-multipartite host configurations up to eight vertices. It counts 102778 valid labeled trees, compares 6834 full multivariate degree-law coefficients with the independent categorical polynomial, and compares 646 distinct-pair degree covariances with the exact theoretical expression. All comparisons passed. The separate all-size proof in RESULT.md establishes the sharp inequality; finite enumeration is **not** an infinite certificate.

## Scientific limits

The weighted tree enumerator is classical. The original 1994 multipartite-tree paper was not available in full, leaving an unresolved priority comparison. Results are specific to connected complete multipartite hosts and uniform tree sampling. The sharp bound and equality are derived by convexity; no independent review is claimed.
