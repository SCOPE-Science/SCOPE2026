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

# Verification and limits

`verify_panhandle.py` runs without external dependencies. Execute `python verify_panhandle.py`; the successful result is `PANHANDLE_OUTER_BALL_EXACT_PASS 105 {'all': 28, 'mixed': 68, 'tie': 9}`.

The program enumerates every base and every vertex at the tested parameter values, computes squared Euclidean distances using exact rational arithmetic, and checks barycentric certificates, contact sets, the two piecewise radii, and the exact radius deficit. Five off-center rational probes independently test the variance lower bound in each case. These tests establish the stated checks only for the finite domain \(2\le r<p\le8\), \(2\le t\le6\); the general claim is proved symbolically in `RESULT.md`.

The geometric formulas are not affine-invariant, and no independent mathematical audit has been performed.
