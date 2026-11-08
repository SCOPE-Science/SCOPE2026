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

# Reproducibility and verification

Use Python 3 with only standard-library dependencies: `python3 check_center_survival.py`. The actual run printed `PASS 207 supporting exact and numerical comparisons`. It evaluates polygons from explicitly clipped half-planes with the shoelace formula and compares against independently calculated normal-direction gap sums. Exact fraction-based tests include \(c=1,2,3\) and rational stabilization; numerical tests cover rational and irrational angles, normalization, and scale-independent branch survival.

The checker does not test all times, all rotation angles, or the infinite-time Diophantine criterion. Those statements are proved in `RESULT.md`, relying on elementary convergent inequalities. Tests are supporting evidence only. No independent mathematical audit or external certification has been performed.
