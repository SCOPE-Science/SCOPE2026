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

# Reproduction

Run `python verify_cycle_root_shells.py` with Python 3 standard library. It reconstructs every proposed projection using `fractions.Fraction`, confirms nonnegative weights summing to one, and checks both the exact squared residual and the signed-edge support condition. It fully enumerates ordered roots for all \(4\le n\le30\) and tests both arc orientations and all cyclic separations for \(31\le n\le200\). Expected terminal result:

`CYCLE_ROOT_PROJECTION_PASS exhaustive_ordered_roots=8982 long_separations=9775 reverse_separations=9775 n=4..200`

A separately written SciPy SLSQP convex-combination quadratic program independently checked 302 cases for \(4\le n\le12\); maximum squared-distance difference was about \(1.46\cdot 10^{-13}\). The numerical optimizer is not a symbolic correctness certificate and is not required to reproduce the proof.

The analytical proof verifies the necessary supporting-normal inequalities explicitly in all four regimes and uses a strict residual-variance identity for continuous equality cases. Historical priority and independent audit are not certified here.
