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

Run `python patch_turnover_verify.py` with NumPy and SciPy. The diagnostic script computes the exact occupancy formula, compares it with the three-state generator matrix exponential on 400 deterministic pseudo-random parameter draws, checks the signs at specified fractions of numerically located crossings, and verifies the stationary comparison. It additionally checks exact-resonance cases, including extinction-free boundaries. The recorded execution reported `CHECKS_PASS 8812` and a crossover of approximately 1.950825084705 for the displayed example.

The unique-crossing theorem is analytical, proved by the ratio monotonicity and integrating factor in RESULT.md. A finite parameter sample cannot verify the quantified statement for all real rates. The comparisons did not inspect all historical full-text articles, and no independent review has been performed.
