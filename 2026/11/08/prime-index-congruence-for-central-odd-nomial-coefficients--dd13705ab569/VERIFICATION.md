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

Run `python3 verify.py` with Python 3 standard library. The program implements two *exact integer* formulas for the central \((2d+1)\)-nomial coefficient at exponent \(p\): a direct repeated convolution algorithm and inclusion-exclusion from the geometric series. It asserts agreement and verifies the predicted prime-square residue for all \(0\le d\le28\) and eleven odd primes through \(37\); this includes both exceptional and ordinary branches.

Expected output: `VERIFY_OK exact_cases=319 exceptional_cases=33 primes=[3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37] d=0..28`.

The infinite-parameter theorem is established by algebraic coefficient extraction and a finite-field harmonic identity in RESULT.md. The finite checker tests cases but does not certify originality or replace the proof; independent mathematical audit has not been performed.
