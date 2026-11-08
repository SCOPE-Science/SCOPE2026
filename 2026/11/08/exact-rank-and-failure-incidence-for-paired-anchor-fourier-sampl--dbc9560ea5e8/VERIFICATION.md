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

# Reproducibility checks

Run `python3 checker.py` from this directory using only the Python standard library. The checker expands the reduced determinant as an integer polynomial in a primitive prime root of unity, checks exact cancellation in the group ring, and compares every configuration to the theorem's midpoint conditions for primes 3, 5, 7, 11. It also recomputes the exact incidence totals. Fixed-seed exact tests cover primes 13, 17, 19 and 23.

The tested exhaustive counts (total, rank-three) are: (54,18) for prime 3; (6000,800) for prime 5; (92610,6174) for prime 7; (2994750,78650) for prime 11. The script terminates with `PAIR_ANCHOR_FOURIER_RANK_CENSUS_PASS`.

These checks test the formula over finite ranges only. The all-prime claim is proved by the independent cyclotomic and finite-field fourth-moment argument in RESULT.md. The check does not provide an independent audit, does not establish priority and does not certify arbitrary four-by-four Fourier minors.
