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

# Scientific verification

The included `verification.py` uses only Python 3 standard-library modules. Its `test()` function independently enumerates each permutation of orders 3 through 9, forms circular descent-position histograms, then applies a hand-implemented integer Walsh–Hadamard transform. It checks all characters against the factorized Eulerian formula, separately enumerates all cycle matchings to check the nonzero-frequency support, verifies the Lucas rank and the six-periodic signed inertia, and checks the sign of each surviving character. Eulerian signed evaluations are additionally checked through degree 40.

Executed command: `python verification.py`.
Observed output: `PASS: 2081 exact assertions, full permutation/FWHT for n=3..9`.

This finite checker is not a substitute for the manuscript's uniform proof. The all-order result uses disjoint relative-order blocks, the cyclic Eulerian identity for the full character, and the exact cycle matching polynomial. This package does not include an independent external correctness or novelty certification.
