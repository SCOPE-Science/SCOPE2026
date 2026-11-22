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

Run `python3 verify_prime_resonance.py` using Python 3 standard library only. It completed with:

```
EXAMPLE r=1 empirical=0.212290 prime_product=0.213633
EXAMPLE r=2 empirical=0.047700 prime_product=0.047846
EXAMPLE r=3 empirical=0.001780 prime_product=0.001664
EXAMPLE r=4 empirical=0.011310 prime_product=0.011283
VERIFY_OK finite_checks=166 prime_bound=100000 exact_CRT_moduli=6,30,210 polynomial_sample=100000
```

The script independently enumerates residue pairs to test all local prime factors through \(19\), verifies finite-modulus Chinese-remainder counts and endpoint run identities over \(6\), \(30\), and \(210\), checks positive finite prime-truncated second differences for \(r\le24\), and computes \(\lfloor\sqrt2 n^2\rfloor\) by exact integer square root for the deterministic sample. The example comparison has a specified finite tolerance and is not an analytic convergence certificate. The mathematical proof, rather than the test script, handles all unbounded quantifiers; it invokes Holdridge's large-prime theorem, Mertens' theorem, and the prime number theorem as published/classical inputs.

No independent scientific audit has been performed.
