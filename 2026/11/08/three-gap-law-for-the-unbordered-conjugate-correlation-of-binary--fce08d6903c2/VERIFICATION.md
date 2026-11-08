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

## Reproducible checks

Run `python3 verify_gap_border.py` from the directory containing this file. The source is standalone Python 3 and requires only its standard library.

The command was executed against the included source. The checked finite range was every three-one binary word of length \(3\le n\le29\), totaling \(27{,}405\) indexed words. For each, independent literal cyclic rotations were checked for proper borders by the prefix-function algorithm and matched against the strict gap-cut prediction. On lengths through \(17\), a separate direct prefix-versus-suffix comparison independently checked the border predicate. The code also checked three exact histogram formulas and the expectation/variance identities using rational arithmetic.

Observed terminal signatures:

```
DIRECT_KMP_BORDER_AND_FULL_POPULATION_OK 27405
EXACT_MOMENT_FORMULAS_OK 3..29
```

This verification is finite corroboration. The infinite cut characterization and all-length formulas rely on the combinatorial proof in RESULT.md, not on extrapolation from the code. The source literature comparison is not a certification of historical priority. Independent mathematical audit has not been performed.
