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

# Reproduction and evidence

Run `python3 verify_kneser_lambda3.py` (Python 3 standard library only). The verifier constructs exact adjacency sets for two small Kneser graphs, checks all size-three and size-four vertex subsets, verifies the extremal three-vertex complement remains connected, directly tests the incidence-function adjacency identity, and checks 264 exact-integer parameter inequalities.

Expected lines include:

```
DIRECT_INCIDENCE_EIGENSPACE_IDENTITY_PASS 8 3
EXHAUSTIVE_THREE_AND_FOUR_SETS_PASS 8 3 N= 56 lambda3= 26 optimal_cut_count= 2520
EXHAUSTIVE_THREE_AND_FOUR_SETS_PASS 9 3 N= 84 lambda3= 54 optimal_cut_count= 280
EXACT_INTEGER_SPECTRAL_THRESHOLDS_PASS 264
VERIFY_OK
```

The exhaustive checks are limited to the named small graphs. The parameter checks cover the ranges explicitly programmed and are not an exhaustive proof of infinitely many parameters. The unrestricted proof is in `RESULT.md`, including the exact graph definition, spectral calculation, comparison of all component sizes and count of minimizers.

No independent audit, formal proof assistant certification or external human validation is claimed.
