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

# Verification and boundaries

The enclosed `verify_threepoint.py` uses standard-library exact integer and rational arithmetic. Run `python3 verify_threepoint.py` from this directory. Successful execution checks the following against independent finite matrix-rank or direct enumeration methods:

- The exact unrounded three-site clock versus mod-two Pascal/Hasse rank for 560 triples within 16 sites.
- The full triple-set distribution, mean and second moment at interval lengths 4, 8, 16, 32 and 64, including all 41,664 three-subsets at length 64.
- General sparse-mask dyadic exactness against independently evaluated Pascal/Hasse ranks for 43,255 mask-and-time cases.
- Complete uniform random-mask dyadic occupancy counts at interval lengths 8, 16 and 32, for mask sizes two through five.

These finite computations test implementation and algebraic consistency; they do **not** constitute infinite-case proof or independent mathematical audit. The infinite theorems are proved by the bilateral linear recurrence, Frobenius identity, finite-field duality, finite occupancy counting and falling-factorial asymptotics documented in RESULT.md. Non-dyadic unrounded clocks for four or more sites are outside the asserted complete classification.
