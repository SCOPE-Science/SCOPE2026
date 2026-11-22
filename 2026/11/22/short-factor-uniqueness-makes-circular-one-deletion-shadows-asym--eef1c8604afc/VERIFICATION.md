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

Verification was conducted against `verify.py` in this package using Python 3. It performs direct circular-word deletion and canonical rotation, independently enumerates the exact cyclic-transition distribution, and checks collision probabilities by exhaustive letter assignments. Passing finite checks corroborate the deterministic and probabilistic arguments but do not establish statements for all lengths.

Manual proof checks: the two intact-factor index sets must intersect because each omits at most \(\ell-1\) of \(n-1\) output factor starts; the factor's source origin is uniquely pinned; linear deletion equality forces a constant interval; a proper subset of edges of each cyclic shift orbit has no graph cycle; and the chromatic polynomial of a cycle gives the transition count. The expectation, variance and Gaussian limit use the declared birthday coupling and standard binomial facts.

The exact source model is independent uniform indexed symbols before quotienting by rotation. No independent mathematical audit has been performed.
