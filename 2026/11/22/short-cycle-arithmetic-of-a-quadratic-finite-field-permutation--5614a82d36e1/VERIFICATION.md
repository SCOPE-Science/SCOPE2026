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

The included `verify.py` requires only Python 3 and no additional package. Its independent exact calculations use fraction-free determinant elimination for all twelve cyclotomic resultants and polynomial Euclidean division modulo primes for the four exceptional gcds. It checks 132 prime-power root-count cases and directly iterates 224 nonzero fibers over twelve odd prime fields. It also confirms the local determinant product equals four.

Expected successful output:

```
PASS: 16 exact resultants/characteristic certificates, 224 prime-field nonzero fibers, 132 prime-power spectral checks
```

The finite-field tests are not used in place of the infinite proof. The formal argument reduces all possible short periods to the three moduli and the explicitly certified resultant and gcd identities. A separate independent mathematical audit has not been performed.
