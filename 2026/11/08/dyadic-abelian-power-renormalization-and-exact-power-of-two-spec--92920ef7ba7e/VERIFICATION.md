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

The accompanying `verify.py` is self-contained and uses only Python's standard library.

Execute `python3 verify.py` from a directory containing that file. The observed outcome for the distributed checker is:

```
VERIFY_OK moduli=8 shifts=7 checks=318792
```

The checker uses two independent definitions of the generalized period-doubling fixed point, direct valuations and iterated substitution. It tests the sliding Parikh identity, Abelian power existence at dyadic periods, and finite exact-rational valuations against the claimed density limits.

The exhaustive quantifiers over all alphabet sizes, exponents, lengths and positions are justified by the written proof, not by these bounded checks. No third-party proof assistant or independent scientific audit is claimed.
