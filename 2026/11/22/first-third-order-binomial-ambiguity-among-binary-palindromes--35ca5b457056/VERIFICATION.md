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

# Reproducibility

Execute `python3 verify_direct.py` and `python3 verify_dynamic.py` from this file's directory. Both use only Python standard-library packages. The direct checker enumerates all \(2^{\lceil n/2\rceil}\) binary palindromes at each \(1\le n\le14\) and sums all increasing-index embeddings for the fourteen target patterns. The independent checker uses simultaneous incremental subsequence-count recurrences and verifies the complete list of profile counts \((2,2,4,4,8,8,16,16,32,32,64,64,128,122)\) and the exact six size-two fibers at length fourteen. All assertions passed during this review. These are exhaustive checks over a finite, explicitly bounded domain. No claim about lengths above fourteen is verified or made. External independent audit has not been performed.
