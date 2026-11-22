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

The infinite theorem is proved by the rational root test, exact cubic discriminant factorization, an exhaustive divisor-of-eight argument, an explicit cyclotomic field identification, Chebotarev's density theorem, and Hensel's lemma.

The independent-of-proof finite checker is `check_prime_spectrum.py` and runs with `python3 check_prime_spectrum.py` without additional packages. It passed 2001 integer-parameter discriminant comparisons, two field identities, and 4153 good-prime root spectra with unique lifts through the third prime power. No finite experiment is used as evidence that every integer parameter has been searched.

The prime-density limits are fixed-parameter statements. For each fixed parameter, finitely many ramified primes are excluded from the cycle-type and Hensel formulas. No effective convergence rate or independence from the classical Chebotarev theorem is claimed.
