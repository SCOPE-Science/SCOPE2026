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

The proof is self-contained apart from the standard definition of a quasi-kernel and the cited contextual sources. Its critical steps are the directed two-step gap classification, the cyclic-composition counting, the cubic Newton-sum identity, the sign-change proof that all auxiliary roots are simple and negative, and the sharp factor root count. No external theorem is needed for the root classification beyond elementary algebra and continuity.

The standalone `verify.py`, extracted from this package, checks fourteen \((n,k)\) cases by enumerating every initial vertex subset and independently checking independence and directed reachability in two steps. It additionally tests the exact integer coefficients for \(3\le n\le150\) and the first cubic discriminant. Executing `python3 verify.py` returned:

```
INDEPENDENT_EXHAUSTIVE_QK_CENSUS_PASS 14 cases 1767232 subsets_scanned
EXACT_CYCLIC_COMPOSITION_AND_COEFFICIENT_CHECK_PASS n=3..150
NEGATIVE_CUBIC_DISCRIMINANT_PASS -876
VERIFY_OK
```

The numerical tests are finite and are not represented as proof for arbitrary graph orders. Historical priority is provisional. Independent mathematical audit has not been performed.
