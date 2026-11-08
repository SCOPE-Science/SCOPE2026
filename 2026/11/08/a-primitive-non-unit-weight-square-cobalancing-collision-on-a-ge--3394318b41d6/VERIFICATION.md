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

# Reproduction and limits

Run `python checker.py` using Python 3 with no third-party dependencies. It independently evaluates square sums by both direct summation and the exact cubic formula and verifies all four endpoint values and both weighted equalities for the primitive coefficient pair \((563,11)\). It checks the corresponding cubic equations with exact integers.

The independent bounded exploration of \(n=1,\ldots,10000\) returns only the displayed indices within that finite interval. No claim is made that the full infinite set of solutions is exhausted. Smoothness of the cubic follows from the partial-derivative argument in `RESULT.md`, not from numerical enumeration. The output captured in `verification_output.txt` was produced by executing the embedded checker against the actual candidate files.

No independent audit or external validation has been performed.
