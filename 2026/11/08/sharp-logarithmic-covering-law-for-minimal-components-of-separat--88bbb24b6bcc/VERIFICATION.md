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

# Reproducible verification and boundaries

The central proof is analytic and consists of: (i) inductive affine atom separation \(g\lambda^{n-1}\); (ii) the active-atom word bijection on a minimal basic component; (iii) the established eventually affine complexity theorem [2]; (iv) matching integer-level lower and upper covering estimates. The eventual-affinity input is a published theorem, not a numerical guess. Intervals of diameter exactly \(\varepsilon\) are allowed; strict inequality at the lower packing scale is ensured by the chosen floor function.

Run the included `verify.py` with Python 3 to reproduce a finite exact-rational example (16 atom generations) in the separated two-branch map with common slope \(1/2\) and closed image gap \(1/2\). All operations use rational arithmetic. The checker tests branch geometry, interval diameter, pairwise separation and level containment. Its finite scope is explicit: it cannot certify the all-level theorem or originality.

Published assumptions, exact references and the proof are in `RESULT.md`. Independent mathematical validation has not been performed. Only self-review is recorded.
