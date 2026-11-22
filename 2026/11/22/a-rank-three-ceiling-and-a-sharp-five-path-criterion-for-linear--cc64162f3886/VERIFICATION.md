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

# Verification of the stated theorem

Run `python verify.py` with Python 3 and no third-party packages. The checker enumerates all integer partitions through order thirteen as linear-forest isomorphism types; for each, it calculates one-point-extension patterns from induced marked pairs and tests the rank-three condition. It independently recurses on every legal one-point extension for ranks three and four through order ten. A third calculation evaluates the two labelled exponential generating functions using exact rational arithmetic and compares their coefficients with orbit-stabilizer counts of component partitions. The script prints `ALL_CHECKS_OK` on successful completion.

These finite computations are not proofs for unbounded order or countably infinite hosts; the independent-triple obstruction and explicit path witnesses in RESULT.md establish those universally. The standard exponential formula and coefficient bounds prove the exact labelled law and asymptotic. The full scientific reasoning and prior-art comparisons appear in RESULT.md and REVIEW.md.
