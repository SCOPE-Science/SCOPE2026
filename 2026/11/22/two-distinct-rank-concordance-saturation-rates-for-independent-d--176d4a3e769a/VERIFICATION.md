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

# Verification of a finite-horizon rank theorem

Run `python3 checker.py` using Python 3.9 or newer (standard library only). It checks the Sparre Andersen–Spitzer coefficient recursion through nine increments for an exact two-valued nonlattice step law, the no-tie rank algebra across every pair of permutations through size five, and deterministic random-seed path/rank identities. It also prints two fast-convergent Gaussian constants using the complementary error function.

The count printed is the number of finite assertions. None of the finite tests is an exhaustive verification of an infinite-time result. The analytically decisive steps are the exponential negative-sum bound, the stationary ergodic average, the occupation-count generating identity and the long-lag domination argument. Independent external audit has not been performed.
