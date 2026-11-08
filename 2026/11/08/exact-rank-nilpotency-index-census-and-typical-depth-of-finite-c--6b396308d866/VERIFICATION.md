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

# Verification of the finite-chain partial-isometry census

Run `python3 verify.py` from the directory containing this document and its companion script. The script has no nonstandard dependencies. It enumerates literal partial maps induced by every allowable signed isometry, deduplicates them, and computes powers by partial composition. Independently, it computes forbidden-run polynomials by enumerating binary words and forms the proposed cumulative rank-index coefficients. It checks all chain lengths from one to nine and every index threshold through one beyond the maximal possible index.

Successful execution prints `EXHAUSTIVE_OK` for each chain length and ends with:

```
JOINT_RANK_INDEX_OK n=1..9
CLOSED_RANK_AND_TOTAL_OK n=1..9
VERIFY_OK
```

The independent direct enumeration gives nilpotent totals \(1,3,9,27,65,151,317,663,1317\) for chain sizes one through nine. The script also checks the closed per-rank expression and the established total cardinality of the ambient monoid. The verification tests small finite cases; it does not prove a statement for arbitrary \(n\), nor does it establish novelty or replace the written asymptotic probability argument. Independent mathematical validation has not been performed.
