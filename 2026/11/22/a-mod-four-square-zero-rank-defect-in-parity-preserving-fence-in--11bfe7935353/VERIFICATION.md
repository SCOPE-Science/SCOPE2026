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

Run `python verify.py` with Python 3 and its standard library. The script enumerates disjoint domain/image subsets, creates the actual ordered partial injection, checks ordinary order, pointwise parity, both forward and inverse fence comparabilities, and evaluates the square by composition. It then compares the maximum-rank profile for every positive chain length through 13 and all three claimed exact top-stratum formulas with an independent composition-sum calculation.

The included `verification_output.txt` records the actual completed run. In particular, the exceptional maximum ranks at chain lengths 2, 6 and 10 were checked without asserting a closed formula for their counts. This is finite corroboration only; the proof for all chain lengths is in RESULT.md. No independent mathematical audit or formal verification is asserted.
