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

# Verification

Extract the standalone `verify.py` from the same package and run `python3 verify.py` with Python 3 and only its standard library. The run actually performed returned:

```
VERIFY_OK structured_cases=236 direct_full_cases=6 sieve_cases=741 max_length=12 example_base41_sums=[19, 23, 27, 31] exponent=991
```

The checker validates exact low-digit arithmetic, modular Fermat congruences at every digit-sum prime, the separate coprimality claims, 236 structured base instances, 741 independently enumerated admissible instances, six fully constructed large-integer examples, and the \(b=41\), \(d=4\), \(p=5\) witness. It checks finite instances only. The infinite result requires the complete argument in `RESULT.md` (in particular, Fermat's little theorem, CRT and the prime obstruction). The file is self-contained, requires no network or other artifacts, and makes no independent audit claim.
