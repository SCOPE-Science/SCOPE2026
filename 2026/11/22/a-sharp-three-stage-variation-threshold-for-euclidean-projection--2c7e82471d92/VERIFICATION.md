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

The cyclic difference map reduces the variation unit ball modulo constants to a hyperplane section of the finite-dimensional cross-polytope. Its exact extreme points are normalized arc indicators. The standalone `verify_cycle_tv.py` enumerates every nonempty boundary-edge set containing at least two edges, every allowable sign pattern up to global reversal, and every arc extremizer for cycles of length three, four and five. It constructs the Euclidean face projector using rational block-averaging matrices and the exact rank-one correction, so no tolerance or sampling is used.

Execution: `python3 verify_cycle_tv.py` completed with `EXACT_COMPLETE_SMALL_CYCLE_FACE_CERTIFICATE_PASS`. The exact per-face-size maxima were 0,1 for n=3; 0,1,1 for n=4; and 0,1,4/3,3/2 for n=5. The larger dimensions use an independent analytical upper bound and explicit symbolic facet witnesses, rather than extrapolation from numerical cases.

The files do not contain an independent machine-checked proof and have not undergone an external audit. Historical novelty remains qualified by inaccessible sources and indexing limitations.
