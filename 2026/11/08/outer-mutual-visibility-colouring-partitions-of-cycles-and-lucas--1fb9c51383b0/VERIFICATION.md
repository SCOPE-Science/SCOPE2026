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

Run `python3 verify.py` with Python 3.10+; no third-party dependencies. The checker reconstructs each cycle's actual shortest paths in both directions, tests all two-vertex pairs through order eighteen and all larger candidate outer-visible subsets through order twelve, and enumerates all unordered vertex partitions for orders three through ten without assuming the matching reduction. It independently enumerates matchings of the auxiliary graph and compares its full cardinality distribution with the ladder occupancy transfer for even orders four through eighteen and the binomial formula for odd orders five through seventeen. The expected final output includes `VERIFY_OK`.

This finite exhaustive checking verifies instances and the transfer encoding; it is not an infinite proof, not an external proof certificate, and not independent validation. The unrestricted conclusions are established in `RESULT.md` using the exact combinatorial bijection and recurrence. Historical priority remains subject to further independent examination.
