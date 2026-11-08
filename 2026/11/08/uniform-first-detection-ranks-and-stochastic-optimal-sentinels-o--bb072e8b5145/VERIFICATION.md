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

# Computational verification

Run `python3 verify.py` with Python 3; it uses only the standard library. A successful replay prints `PASS: 50036 exact checks, including independent frontier enumeration and CTMC means`.

The exact-fraction tests independently enumerate all left/right frontier paths for arc lengths up to twelve; compute event-step survival by transition-probability propagation for every sentinel subset on cycles through nine vertices; compute first-passage means by a separate Markov recursion through eight vertices; enumerate all gap-placement optimality comparisons on cycles through ten vertices; and verify exact coefficient formulas and boundary cases. No sampling approximations or randomized simulations are used.

The finite checks are not an exhaustive verification for unbounded population size. The general theorem follows from the explicit fixed-direction rank count, independent exponential waiting times, the Poisson transform, and strict positive discrete curvature. Independent scientific audit has not been performed.
