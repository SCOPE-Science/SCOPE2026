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

# Reproducibility and verification

The standalone `artifacts/verify.py` uses Python's standard library and is run as `python3 artifacts/verify.py`. In a direct execution it returned:

```
VERIFY_OK local_cases=44 base_seeds=323 prime_cube_fibers=24 exception_checks=10 both_overlap_types=PASS
```

The script exhaustively checks the simultaneous primitive-root counts for every seed for each of the 22 listed primes \(7\le p\le97\), with both reciprocal signs, compares predicted and directly counted total prime-square lifts, and checks 24 complete prime-cube seed fibers at five primes. It checks that both possible values of the forbidden-lift coincidence indicator are attained. Additional direct modular evaluation verifies the excluded primes \(3,5,7,13,61\) against the sign-specific exception lists. The full unbounded correctness argument, including the finite-field seed theorem used from the literature, is in `RESULT.md`; these bounded tests alone do not prove it.

No independent audit has been performed. There are unresolved historical-priority risks described in `REVIEW.md` and `AUDIT.json`.
