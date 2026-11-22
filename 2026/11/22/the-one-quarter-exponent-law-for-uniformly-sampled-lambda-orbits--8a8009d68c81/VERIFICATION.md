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

# Verification notes

A self-contained exact-integer checker, `verify_orbit_sampling.py`, is provided. It independently creates all left-unitriangular action orbits and checks their matrix ranks and sizes in the seven cases enumerated in `RESULT.md`. A separately implemented rank recurrence agrees with the subset formula for field sizes 2, 3, 4, 5 and 7 through dimension 15. The program concludes with `EQUAL_ORBIT_LAMBDA_BIAS_CHECKS_PASSED` when all checks pass.

The infinite-dimensional \(L^1\) theorem rests on the written partition-product estimates, not on an extrapolation from finite data. In particular finite enumeration does not certify all prime-power fields or all dimensions. The only reviewed mathematical assertion is the equal-orbit sampling theorem, including the bounded defect and leading exponent. Independent audit has not been performed.
