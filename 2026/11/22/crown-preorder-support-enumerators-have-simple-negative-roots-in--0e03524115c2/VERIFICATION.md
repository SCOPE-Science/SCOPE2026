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

The exact theorem is proved in `RESULT.md`. Run the included standard-library-only `verify.py` with `python3 verify.py` on Python 3.9 or newer. The program independently enumerates disjoint upward-matchable endpoint pairs on crown posets for orders \(6,8,10,12,14,16\); checks integer points of the preorder polytope from *all* order ideals for orders \(6,8,10\); and compares the cycle matching transfer matrix to the asserted formula through crown order \(100\). All comparisons use integer arithmetic. Success prints `VERIFY_OK`.

The underlying Hall/Oh/Zhong disjoint pair theorem is an external cited input. The cycle-to-matching uniqueness lemma, full-cycle correction, transfer matrix and Chebyshev zero analysis form the unrestricted proof. Finite enumeration is not an infinite proof and does not determine whether the theorem has appeared elsewhere in unindexed prior literature. The manuscript underlying the cited contemporary specialist release was not independently read in full. No independent verification has been performed.
