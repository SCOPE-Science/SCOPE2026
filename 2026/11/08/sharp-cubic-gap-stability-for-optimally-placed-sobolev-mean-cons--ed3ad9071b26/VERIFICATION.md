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

# Verification of the periodic atomic Sobolev identity

The complete algebraic proof is in RESULT.md. The elementary distributional equalities and gapwise quadratic integration establish the universal identity for every allowed real placement and positive total atomic mass; no finite numerical experiment proves these universal statements.

For a reproducible independent check, run `python3 check_circle.py` with Python 3.9 or later. It checks 441 rational placements and masses, including the equal-gap equality configurations. An independent direct method solves the distributional equation for the centered point-evaluation representer, chooses the integration constant to enforce periodicity, and integrates its squared piecewise-linear derivative exactly. This independently reproduces 4,410 rational point-evaluation norms and compares their maximization with the resistance and cubic-gap expressions.

Successful diagnostic text:

```
INDEPENDENT_PERIODIC_VARIATIONAL_RATIONAL_CASES_PASSED 441
EXACT_POINT_EVALUATION_ENERGY_IDENTITIES_PASSED 4410
CUBIC_GAP_DEFICIT_AND_UNIQUE_EQUAL_SPACING_PASSED
```

The checker does not certify all real configurations, novelty, or independent mathematical review. The strict inequality for nonuniform gaps follows analytically from a positive exact sum, not from finite sampling.
