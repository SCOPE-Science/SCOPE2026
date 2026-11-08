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

Execute `python3 verify.py` in an empty directory containing the attached file. A successful run prints `VERIFY_OK` and asserts the exact fixed-point coefficient identity for every order-preserving transformation on chains of degrees one through ten. It also verifies the total rational recurrence through degree sixteen and the independent side/basin count. The program does not need external files or packages, the internet, or a random seed.

Analytic verification is mathematical: there is a unique positive dominant solution \(\rho\in(0,1/2)\) of \(B(\rho)=1\), the idempotent pole is farther from the origin, and the basin-size law has positive variance. Exhaustive finite tests alone do not prove the generating function or its limit theorem, and an independent mathematical audit has not been performed.
