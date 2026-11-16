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

Execute `python3 check.py` with the standard library. It enumerates all normalized ordered pairs at phase-alphabet sizes 2, 3, 4, 6, 9 and 12 and checks exact modular-support criteria against nine direct complex Fourier sums, asserting agreement. Values 2 and 4 are comparative controls; the theorem's enumerative formulas concern alphabets divisible by 3. In particular, the tested divisible-by-three counts at 3, 6, 9, and 12 match the closed formulas. The code carries no external dependencies, and its floating-point tolerance is solely an independent finite diagnostic. The infinite-family proof is given in RESULT.md, not inferred from the samples.

Scientific checks include all three quantifiers (each integer alphabet divisible by 3; every normalized pair; all nine time-frequency sites) and all intersection multiplicities. The exact argument forces cube-root ratios if two translation rows contain zeros, so no unsupported two-row intermediate case is assumed. Published unrestricted three-cycle support cases are not claimed as new. No independent audit has been performed.
