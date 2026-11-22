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

# Verification and reproducibility

The mathematical proof in `RESULT.md` establishes the universal upper bound and matching family of couplings for every real tolerance \(\varepsilon\ge0\). The only nonstandard construction is a randomly permuted, randomly signed affine triple built from a uniform \([1,3/2]\) variable. Its exact six-interval marginal partition and pair-sum range are given explicitly in the proof.

Execute `python3 checker.py` with Python 3 and no third-party packages. The program checks exact rational endpoints, interval partition and density weights, pair-sum bounds under all signs and permutations, scaling for several rational tolerances, and the critical upper-bound identity. Expected output: `PASS: 1891 exact rational assertions/groups; analytic proof remains essential`.

The program checks finitely many sample tolerances; its assertions are reproducibility diagnostics, not an infinite certificate. The analytic proof handles every admissible real tolerance and every Borel coupling. The exact capacity is specific to three continuous standard-uniform marginals, common target sum and common tolerance. No independent audit has been performed.
