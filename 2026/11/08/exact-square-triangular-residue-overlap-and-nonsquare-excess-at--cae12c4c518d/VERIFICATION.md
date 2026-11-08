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

# Reproducibility and exact limits

Run `python3 verify.py` with Python 3; no nonstandard packages or network connectivity are required. The program enumerates squares and triangular images and independently counts their intersection for every modulus from 2 through 2000. It checks the three-branch exact prime nonsquare-excess identities for every odd prime below 151. It also checks separate prime powers up to 30000 for the seven primes listed in the program and tests dyadic triangular surjectivity and odd-modulus equality of the separate image cardinalities.

Observed output:

```
VERIFY_OK moduli=1999 prime_nonsquare_excess=34 prime_powers=34 exact_intersections=PASS dyadic_surjectivity=PASS CRT=PASS
```

All computations use exact modular integer arithmetic. They are finite tests; the generic-character, exceptional-valuation, dyadic-bijection and Chinese-remainder proof steps establish the unrestricted theorem. The arithmetic implementation is ordinary reproducibility software, not a formally verified proof or an independent audit.
