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

# Verification and limitations

The analytic proof of the coverage criterion and sharp rank–corank thresholds is in `RESULT.md`, including the two explicit witness vectors and every boundary equality. A standalone standard-library Python checker is supplied as `verification/check.py`. It passed 239,672 exact-rational assertions over finite grids, explicit threshold witnesses, and deterministic rational convex combinations. These checks are not an exhaustive search over real coordinates or dimensions, and the universal claim does not depend on them.

To reproduce after extracting all embedded files, run `python verification/check.py`. There are no external dependencies or stale generated paths. This work establishes no theorem for nonuniform matroid base polytopes, no uncovered-volume formula, and no independent historical-priority certificate. The available scientific assessment is a self-review only; independent review has not been performed.
