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

The finite-exhaustion proof in RESULT.md is replayable from `verify_short_cycles.cpp` with a C++17 compiler. All periods \(1\) through \(22\), all residues of the delay modulo each period, and every binary nonzero-position mask are processed using exact integer operations. A proof of the mask reduction and of completeness is provided in RESULT.md. The program explicitly compares every valid primitive word against the table, counts its zero-anchored rotations and verifies the original modular-square recurrence.

The included independent direct-word cross-check `verify_small_direct.py` enumerates all ternary words for periods \(1\) through \(11\) and every delay residue without relying on the binary-mask reconstruction.

Observed direct test outputs:

```
VERIFY_OK periods=1..22,lag_residues=all,mask_candidates=176160517,valid_zero_anchored=36,exact_integer=yes
INDEPENDENT_DIRECT_OK periods=1..11 all_lags exact_enumeration=yes
```

The tests are exhaustive only in the stated finite domains. No inference about longer primitive cycles or entry from the distinguished seed is made. Independent mathematical audit has not been performed.
