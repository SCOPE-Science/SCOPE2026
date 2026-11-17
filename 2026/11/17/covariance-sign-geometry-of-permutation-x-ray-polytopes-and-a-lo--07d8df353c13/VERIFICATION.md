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

The finite checker `verify.py` independently enumerates all permutation X-rays for orders 2 through 8, obtains exact rational second moments, and compares every covariance entry with the theorem. It also checks all coordinate-pair sign cases through order 100 and evaluates the exact positive-pair sum. Running `python verify.py` gives 662674 exact assertions, all passing. These checks are finite tests; the theorem for arbitrary order follows from the permutation-indicator covariance identity, interval overlap calculation and Riemann-sum proof in `RESULT.md`.

The classification is limited to the pushforward of the uniform distribution on source permutation matrices, including repeated images with their multiplicity. The published-source priority check is provisional and is not an independent mathematical audit.
