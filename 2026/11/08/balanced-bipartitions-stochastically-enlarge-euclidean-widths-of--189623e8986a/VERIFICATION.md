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

Execute `python3 verify.py` from the directory containing this document and the standalone checker. The expected successful output begins with `BALANCED_BIPARTITE_WIDTH_CHECKS_PASSED`. The checker enumerates all \(p\)-subsets in 20 deterministic profiles of sizes \(3\) through \(7\), compares their exact crossing-gap CDFs to the stated binomial probability at six thresholds, and verifies monotonicity. It also tests the positive-length one-long-edge strictness mechanism for sizes \(4\) through \(14\). No stochastic sampling or external package is required.

These bounded verifications are not exhaustive for arbitrary dimension. The proof in `RESULT.md` establishes the stated theorem by exact support-function identities, a deterministic one-component lemma, finite binomial counting, and an integral equality argument. The external priority comparison examines relevant literature but does not constitute independent mathematical certification.
