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

# Reproducibility

Run `python3 checker.py` using only the Python standard library. Every polygon vertex, affine coefficient, root and trace is an exact rational or integer. Expected outputs: cell count 2337, singular cells 9, nonsingular-cell fourth-return representatives 336, primitive-four points 320, and 80 primitive cycles; 32 regular cycles trace -574, 16 trace 578, 16 trace 178, and 16 switching cycles. All four period-two line segments are checked as exceptional singular affine branches.

This is an exact finite-algebraic exhaustion. The mathematical completeness argument depends on the stated partition covering the square and its boundary, not on a test log. No independent mathematical audit has been performed.
