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

# Reproduction and scope

Run `python3 verify.py` with Python 3 and no external modules. The verifier constructs each \(D_m(X)\) directly from its defining binomial coefficients and performs polynomial multiplication modulo \(p^3\); it separately constructs the claimed comparison polynomial. It checks all coefficients for nine odd primes up to 29, checks the exact normalized fourth-power expansion at 49 integer inputs, checks Guo's convolution identity and its recurrence for 23 indices, and checks the central triple-to-double reduction coefficientwise modulo \(p^2\) for seven primes.

The observed complete output is:

```text
VERIFY_OK primes=9 coefficients=481 lemma_4_2=23 recurrence=21 lemma_4_1=49 intermediate_primes=7 intermediate_coefficients=143 all_exact=True
```

These are finite checks. The unrestricted proof is given in `RESULT.md` and uses two proved published binomial identities; the verifier neither claims to certify all primes nor constitutes independent mathematical audit. It does not test the excluded prime two or a hypothetical modulus \(p^4\).
